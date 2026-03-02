#!/usr/bin/env python3
"""Crawl Alibaba Cloud OSS SDK documentation from help.aliyun.com"""

import urllib.request
import re
import time
import html as html_mod
import os
import sys

base = "https://help.aliyun.com"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

def fetch(url):
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req, timeout=15)
    return resp.read().decode('utf-8')

def extract_content(html_content):
    text = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL)
    text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
    main_match = re.search(r'class="product-detail">(.*?)<div class="RecommendDoc', text, re.DOTALL)
    if not main_match:
        main_match = re.search(r'class="aliyun-docs-content">(.*?)</section>', text, re.DOTALL)
    if main_match:
        text = main_match.group(1)
    def clean_code_block(m):
        code = m.group(1)
        code = re.sub(r'<[^>]+>', '', code)
        code = html_mod.unescape(code)
        return '\n```\n' + code + '\n```\n'
    text = re.sub(r'<pre[^>]*>(.*?)</pre>', clean_code_block, text, flags=re.DOTALL)
    text = re.sub(r'<code[^>]*>(.*?)</code>', lambda m: '`' + re.sub(r'<[^>]+>', '', html_mod.unescape(m.group(1))) + '`', text, flags=re.DOTALL)
    for i in range(1, 7):
        text = re.sub(f'<h{i}[^>]*>(.*?)</h{i}>', lambda m, i=i: '\n' + '#' * i + ' ' + re.sub(r'<[^>]+>', '', m.group(1)).strip() + '\n', text, flags=re.DOTALL)
    text = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', lambda m: '[' + re.sub(r'<[^>]+>', '', m.group(2)) + '](' + m.group(1) + ')', text, flags=re.DOTALL)
    text = re.sub(r'<li[^>]*>(.*?)</li>', lambda m: '- ' + re.sub(r'<[^>]+>', '', m.group(1)).strip() + '\n', text, flags=re.DOTALL)
    text = re.sub(r'<p[^>]*>(.*?)</p>', lambda m: '\n' + m.group(1).strip() + '\n', text, flags=re.DOTALL)
    text = re.sub(r'<br\s*/?>', '\n', text)
    text = re.sub(r'<th[^>]*>(.*?)</th>', lambda m: '| ' + re.sub(r'<[^>]+>', '', m.group(1)).strip() + ' ', text, flags=re.DOTALL)
    text = re.sub(r'<td[^>]*>(.*?)</td>', lambda m: '| ' + re.sub(r'<[^>]+>', '', m.group(1)).strip() + ' ', text, flags=re.DOTALL)
    text = re.sub(r'<tr[^>]*>(.*?)</tr>', lambda m: m.group(1).strip() + '|\n', text, flags=re.DOTALL)
    text = re.sub(r'<[^>]+>', '', text)
    text = html_mod.unescape(text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

def get_next_page(html_content):
    match = re.search(r'<a\s+href="([^"]+)"[^>]*>下一篇[：:]', html_content)
    if match:
        href = match.group(1)
        if href.startswith('/'):
            return base + href
        return href
    return None

def get_title(html_content):
    match = re.search(r'<title>([^<]+)</title>', html_content)
    if match:
        return match.group(1).split('-')[0].strip()
    return "Unknown"

def crawl_sdk(start_path, output_dir, sdk_name, stop_markers):
    """Crawl an SDK section starting from the given path"""
    os.makedirs(output_dir, exist_ok=True)

    # Clean old files
    for f in os.listdir(output_dir):
        if f.endswith('.md'):
            os.remove(os.path.join(output_dir, f))

    start_url = base + start_path
    current_url = start_url
    page_count = 0
    max_pages = 120

    while current_url and page_count < max_pages:
        try:
            slug = current_url.rstrip('/').split('/')[-1]

            # Check stop markers
            if page_count > 0 and any(marker in current_url for marker in stop_markers):
                print(f"  Reached end of {sdk_name} section")
                break

            print(f"  [{page_count}] {current_url}")
            content = fetch(current_url)
            title = get_title(content)

            filename = f"{page_count:02d}-{slug}.md"
            md_content = extract_content(content)
            full_content = f"# {title}\n\nSource: {current_url}\n\n---\n\n{md_content}"

            filepath = os.path.join(output_dir, filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(full_content)

            print(f"       {title} ({len(md_content)} chars)")
            page_count += 1

            next_url = get_next_page(content)
            if next_url:
                current_url = next_url
            else:
                break

            time.sleep(0.3)

        except Exception as e:
            print(f"       ERROR: {e}")
            break

    print(f"  Total {sdk_name}: {page_count} pages\n")
    return page_count


# SDK configurations: (start_path, output_dir, sdk_name, stop_markers)
sdks = {
    "php-v2": (
        "/zh/oss/developer-reference/manual-for-php-v2/",
        "/Users/peiyu/Documents/claude/docs/crawled-oss-docs/sdk-php",
        "PHP SDK V2",
        ["/preface-4/", "/preface-3/", "/nodejs-sdk/", "/oss-sdk-for-c-2-0/"]
    ),
    "dotnet-v2": (
        "/zh/oss/developer-reference/oss-sdk-for-c-2-0/",
        "/Users/peiyu/Documents/claude/docs/crawled-oss-docs/sdk-dotnet",
        "C# SDK V2",
        ["/nodejs-sdk/", "/preface-4/", "/browser-js/"]
    ),
    "browser": (
        "/zh/oss/developer-reference/browser-js/",
        "/Users/peiyu/Documents/claude/docs/crawled-oss-docs/sdk-browser",
        "Browser.js SDK",
        ["/kotlin/", "/android/", "/introduction/", "/oss-kotlin-sdk"]
    ),
    "android": (
        "/zh/oss/developer-reference/introduction/",
        "/Users/peiyu/Documents/claude/docs/crawled-oss-docs/sdk-android",
        "Android SDK",
        ["/preface-5/", "/ios/"]
    ),
    "ios": (
        "/zh/oss/developer-reference/preface-5/",
        "/Users/peiyu/Documents/claude/docs/crawled-oss-docs/sdk-ios",
        "iOS SDK",
        ["/preface-2/", "/c-sdk/", "/oss-tools"]
    ),
}

if __name__ == "__main__":
    if len(sys.argv) > 1:
        sdk_key = sys.argv[1]
        if sdk_key in sdks:
            config = sdks[sdk_key]
            crawl_sdk(*config)
        else:
            print(f"Unknown SDK: {sdk_key}. Available: {list(sdks.keys())}")
    else:
        for key, config in sdks.items():
            print(f"\n=== Crawling {config[2]} ===")
            crawl_sdk(*config)
