#!/usr/bin/env python3
"""
Crawl Alibaba Cloud OSS documentation pages and save as Markdown.
Uses urllib to fetch pages and extracts content from the HTML.
"""

import urllib.request
import urllib.error
import re
import os
import sys
import time
import json
from html.parser import HTMLParser
from html import unescape

BASE_URL = "https://www.alibabacloud.com"
OUTPUT_DIR = "/Users/peiyu/Documents/claude/docs/crawled-oss-docs"

class DocHTMLParser(HTMLParser):
    """Parse the Alibaba Cloud doc page and extract the main content area."""

    def __init__(self):
        super().__init__()
        self.in_article = False
        self.article_depth = 0
        self.content_parts = []
        self.current_tag = None
        self.tag_stack = []
        self.skip_tags = {'script', 'style', 'nav', 'footer', 'header', 'noscript'}
        self.in_skip = 0
        self.in_code = False
        self.in_pre = False
        self.in_table = False
        self.table_rows = []
        self.current_row = []
        self.current_cell = []
        self.in_th = False
        self.in_td = False
        self.in_li = False
        self.in_heading = False
        self.heading_level = 0
        self.in_a = False
        self.a_href = ""
        self.found_content = False
        self.title = ""
        self.in_title = False
        self.in_main_content = False
        self.main_content_depth = 0
        self.in_note = False
        self.note_type = ""

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        class_name = attrs_dict.get('class', '')
        id_name = attrs_dict.get('id', '')

        if tag == 'title':
            self.in_title = True
            return

        if tag in self.skip_tags:
            self.in_skip += 1
            return

        if self.in_skip > 0:
            return

        # Look for the main documentation content area
        # Use icms-help-docs-content (innermost content div) or doc-content (outer wrapper)
        if not self.in_main_content:
            if ('icms-help-docs-content' in class_name or
                'doc-content' in class_name):
                self.in_main_content = True
                self.main_content_depth = 1
                return
        else:
            self.main_content_depth += 1

        if not self.in_main_content:
            return

        if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            self.in_heading = True
            self.heading_level = int(tag[1])
            self.content_parts.append('\n' + '#' * self.heading_level + ' ')
        elif tag == 'p':
            self.content_parts.append('\n\n')
        elif tag == 'a':
            self.in_a = True
            self.a_href = attrs_dict.get('href', '')
            self.content_parts.append('[')
        elif tag == 'ul' or tag == 'ol':
            self.content_parts.append('\n')
        elif tag == 'li':
            self.in_li = True
            self.content_parts.append('\n- ')
        elif tag == 'pre':
            self.in_pre = True
            lang = ''
            if 'language-' in class_name:
                lang = class_name.split('language-')[1].split(' ')[0].split('"')[0]
            self.content_parts.append('\n\n```' + lang + '\n')
        elif tag == 'code' and not self.in_pre:
            self.in_code = True
            self.content_parts.append('`')
        elif tag == 'table':
            self.in_table = True
            self.table_rows = []
        elif tag == 'tr':
            self.current_row = []
        elif tag == 'th':
            self.in_th = True
            self.current_cell = []
        elif tag == 'td':
            self.in_td = True
            self.current_cell = []
        elif tag in ('strong', 'b'):
            self.content_parts.append('**')
        elif tag in ('em', 'i'):
            self.content_parts.append('*')
        elif tag == 'br':
            self.content_parts.append('\n')
        elif tag == 'img':
            alt = attrs_dict.get('alt', '')
            src = attrs_dict.get('src', '')
            if src:
                self.content_parts.append(f'![{alt}]({src})')
        elif tag == 'div':
            if 'notice' in class_name.lower() or 'warning' in class_name.lower() or 'note' in class_name.lower():
                if 'warning' in class_name.lower():
                    self.note_type = 'WARNING'
                elif 'important' in class_name.lower():
                    self.note_type = 'IMPORTANT'
                else:
                    self.note_type = 'NOTE'
                self.in_note = True
                self.content_parts.append(f'\n\n> **{self.note_type}**: ')

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False
            return

        if tag in self.skip_tags:
            self.in_skip -= 1
            return

        if self.in_skip > 0:
            return

        if self.in_main_content:
            self.main_content_depth -= 1
            if self.main_content_depth <= 0:
                self.in_main_content = False
                self.found_content = True

        if not self.in_main_content and not self.found_content:
            return

        if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            self.in_heading = False
            self.content_parts.append('\n')
        elif tag == 'p':
            self.content_parts.append('\n')
        elif tag == 'a':
            self.in_a = False
            href = self.a_href
            if href and not href.startswith('javascript:') and not href.startswith('#'):
                if href.startswith('/'):
                    href = BASE_URL + href
                self.content_parts.append(f']({href})')
            else:
                self.content_parts.append(']')
            self.a_href = ''
        elif tag == 'li':
            self.in_li = False
        elif tag == 'pre':
            self.in_pre = False
            self.content_parts.append('\n```\n\n')
        elif tag == 'code' and not self.in_pre:
            self.in_code = False
            self.content_parts.append('`')
        elif tag == 'table':
            self.in_table = False
            if self.table_rows:
                self.content_parts.append('\n\n')
                for i, row in enumerate(self.table_rows):
                    self.content_parts.append('| ' + ' | '.join(row) + ' |\n')
                    if i == 0:
                        self.content_parts.append('| ' + ' | '.join(['---' for _ in row]) + ' |\n')
                self.content_parts.append('\n')
            self.table_rows = []
        elif tag == 'tr':
            if self.current_row is not None:
                self.table_rows.append(self.current_row)
        elif tag == 'th':
            self.in_th = False
            self.current_row.append(' '.join(''.join(self.current_cell).split()))
        elif tag == 'td':
            self.in_td = False
            self.current_row.append(' '.join(''.join(self.current_cell).split()))
        elif tag in ('strong', 'b'):
            self.content_parts.append('**')
        elif tag in ('em', 'i'):
            self.content_parts.append('*')
        elif tag == 'div' and self.in_note:
            self.in_note = False
            self.content_parts.append('\n')

    def handle_data(self, data):
        if self.in_title:
            self.title += data
            return

        if self.in_skip > 0:
            return

        if self.in_th or self.in_td:
            self.current_cell.append(data)
        elif self.in_main_content:
            if self.in_pre:
                self.content_parts.append(data)
            else:
                text = data.strip()
                if text:
                    self.content_parts.append(data)

    def handle_entityref(self, name):
        char = unescape(f'&{name};')
        self.handle_data(char)

    def handle_charref(self, name):
        char = unescape(f'&#{name};')
        self.handle_data(char)

    def get_markdown(self):
        content = ''.join(self.content_parts)
        # Clean up excessive newlines
        content = re.sub(r'\n{4,}', '\n\n\n', content)
        # Clean up spaces
        content = re.sub(r'[ \t]+\n', '\n', content)
        # Remove empty bold/italic markers
        content = re.sub(r'\*\*\s*\*\*', '', content)
        content = re.sub(r'\*\s*\*', '', content)
        # Remove empty backtick pairs
        content = re.sub(r'``', '', content)
        # Remove empty links
        content = re.sub(r'\[\s*\]\s*', '', content)
        return content.strip()


def clean_nav_header(content):
    """Remove the navigation header noise from the extracted content."""
    # Pattern: starts with navigation breadcrumbs and search stuff
    # Find the actual content start - typically after the page title repeated
    lines = content.split('\n')
    cleaned_lines = []
    found_real_content = False
    skip_patterns = [
        r'^All Products\*?\*?$',
        r'^Search$',
        r'^- \[Document Center\]',
        r'^- \[Object Storage Service\]',
        r'^- \[User Guide\]',
        r'^- \[Developer Reference\]',
        r'^- \[API reference\]',
        r'^- \[Getting started\]',
        r'^- \[Bucket-level operations\]',
        r'^- \[Object-level operations\]',
        r'^- \[Basic operations',
        r'^- \[Multipart upload\]',
        r'^- \[.+\]\(https://www\.alibabacloud\.com/help/en/oss/',
        r'^all-products-head',
        r'^This Product\*?\*?$',
        r'^- This Product$',
        r'^- All Products$',
        r'^Object Storage Service:.+\*?\*?$',
        r'^\*?\*?$',
    ]

    # First pass: find the title line
    title_line = None
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith('# '):
            title_line = i
            break

    if title_line is None:
        return content

    # Second pass: after the title, skip nav noise until we find real content
    in_nav = True
    for i, line in enumerate(lines):
        stripped = line.strip()
        if i <= title_line:
            if i == title_line:
                cleaned_lines.append(line)
            continue

        if in_nav:
            is_nav = False
            for pattern in skip_patterns:
                if re.match(pattern, stripped):
                    is_nav = True
                    break
            if not stripped:
                continue  # skip blank lines in nav area
            if is_nav:
                continue
            else:
                in_nav = False
                cleaned_lines.append('')  # add a blank line after title
                cleaned_lines.append(line)
        else:
            cleaned_lines.append(line)

    return '\n'.join(cleaned_lines)


def fetch_page(url, retries=3):
    """Fetch a page with retries and return HTML content."""
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
            })
            with urllib.request.urlopen(req, timeout=30) as response:
                return response.read().decode('utf-8', errors='replace')
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(2 * (attempt + 1))
            else:
                print(f"  ERROR fetching {url}: {e}", file=sys.stderr)
                return None


def html_to_markdown(html_content, url):
    """Convert HTML to Markdown using the custom parser."""
    parser = DocHTMLParser()
    try:
        parser.feed(html_content)
    except Exception as e:
        print(f"  Parse error for {url}: {e}", file=sys.stderr)
        return None, None

    content = parser.get_markdown()
    title = parser.title.strip()

    # Clean up title - remove suffix
    title = re.sub(r'\s*[-|]\s*(Alibaba Cloud|Object Storage Service|Documentation Center|Document Center).*$', '', title).strip()

    if not content or len(content) < 50:
        return title, None

    # Add title as H1 if not already present
    if title and not content.startswith('# '):
        content = f'# {title}\n\n{content}'

    # Clean navigation header noise
    content = clean_nav_header(content)

    return title, content


def url_to_filepath(url_path):
    """Convert a URL path to a local file path."""
    path = url_path.replace('/help/en/oss/', '')
    path = path.rstrip('/')
    path = path.split('#')[0]
    if not path:
        path = 'index'
    return path + '.md'


def crawl_all():
    """Read URL list and crawl all pages."""
    urls_file = os.path.join(OUTPUT_DIR, 'urls.txt')

    with open(urls_file, 'r') as f:
        lines = f.readlines()

    urls = []
    for line in lines:
        line = line.strip()
        if line and not line.startswith('#'):
            clean_url = line.split('#')[0]
            if clean_url not in [u[0] for u in urls]:
                urls.append((clean_url, line))

    total = len(urls)
    print(f"Total URLs to crawl: {total}")

    results = []
    errors = []

    for i, (url_path, original_line) in enumerate(urls):
        full_url = BASE_URL + url_path
        filepath = url_to_filepath(url_path)
        full_filepath = os.path.join(OUTPUT_DIR, filepath)

        os.makedirs(os.path.dirname(full_filepath), exist_ok=True)

        print(f"[{i+1}/{total}] Crawling: {url_path}")

        html = fetch_page(full_url)
        if html is None:
            errors.append((url_path, "Failed to fetch"))
            continue

        title, content = html_to_markdown(html, full_url)

        if content is None:
            errors.append((url_path, "No content extracted"))
            content = f"# {title or url_path}\n\n*Content could not be extracted. Visit: {full_url}*\n"

        with open(full_filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        results.append((url_path, filepath, title or url_path))

        # Be polite
        time.sleep(0.5)

    print(f"\nGenerating INDEX.md...")
    generate_index(results, errors)

    print(f"\nDone! Crawled {len(results)} pages, {len(errors)} errors")
    if errors:
        print("\nErrors:")
        for url, err in errors:
            print(f"  {url}: {err}")


def generate_index(results, errors):
    """Generate the INDEX.md file."""
    index_content = "# Alibaba Cloud OSS Documentation Index\n\n"
    index_content += f"Total pages crawled: {len(results)}\n\n"

    if errors:
        index_content += f"Pages with errors: {len(errors)}\n\n"

    # Group by section
    sections = {}
    for url_path, filepath, title in results:
        parts = url_path.replace('/help/en/oss/', '').split('/')
        section = parts[0] if parts else 'root'
        if section not in sections:
            sections[section] = []
        sections[section].append((filepath, title, url_path))

    for section, pages in sections.items():
        section_title = section.replace('-', ' ').title()
        index_content += f"\n## {section_title}\n\n"
        for filepath, title, url_path in pages:
            index_content += f"- [{title}]({filepath})\n"

    if errors:
        index_content += "\n## Pages with Errors\n\n"
        for url_path, err in errors:
            index_content += f"- {url_path}: {err}\n"

    index_path = os.path.join(OUTPUT_DIR, 'INDEX.md')
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_content)


if __name__ == '__main__':
    crawl_all()
