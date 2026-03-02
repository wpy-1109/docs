# Editorial review report

## Summary

Reviewed all documentation sections against the 27 editorial guidelines. Applied fixes directly to MDX files across 6 sections (462 pages total).

## Changes applied

### 1. Sentence case headings (Guideline #1)

Converted all Title Case headings to sentence case across the entire documentation. Preserved capitalization for proper nouns, product names, and acronyms (OSS, RAM, STS, CDN, etc.).

**Files modified**: ~350 files
**Examples**:
- `## Key Capabilities` -> `## Key capabilities`
- `## How It Works` -> `## How it works`
- `## Upload Methods Overview` -> `## Upload methods overview`
- `### Bucket-Level Endpoints` -> `### Bucket-level endpoints`

### 2. "Related Topics" renamed to "Next steps" (Guideline #18)

Renamed all `## Related Topics` sections to `## Next steps` to provide forward guidance instead of backward references.

**Files modified**: ~250 files
**Sections affected**: get-started, guides, sdks, resources, tools, api-reference

### 3. Link text in Next steps sections (Guideline #1)

Converted Title Case link text within Next steps sections to sentence case.

**Examples**:
- `[Upload Objects](/guides/objects/upload-objects)` -> `[Upload objects](/guides/objects/upload-objects)`
- `[Performance Best Practices](/resources/best-practices/performance)` -> `[Performance best practices](/resources/best-practices/performance)`

### 4. Added missing Next steps sections (Guideline #18)

Added Next steps sections to 42 SDK pages that were missing them, with contextually relevant links based on the page topic.

### 5. Code example ordering verified (Guideline #27)

Verified Tab ordering across all files with code examples. All follow the correct pattern: Python -> Java -> Go -> Node.js (cURL appears rarely in guides).

## Coverage by section

| Section | Pages | Headings fixed | Next steps added/renamed |
|---------|-------|---------------|--------------------------|
| get-started | 13 | All 13 files | 12/13 (index is nav page) |
| guides | 88 | All 88 files | All 88 files |
| sdks | 114 | 112 files | 96/114 |
| resources | 26 | 20 files | Some (resources/FAQ pages) |
| tools | 15 | 15 files | 1/15 |
| api-reference | 158 | 102 files | API ref pages use different structure |

## Items not changed (by design)

- **Frontmatter titles**: Left in Title Case as these are typically handled by the rendering engine and follow Mintlify conventions
- **Card titles**: Left as-is since Card component titles in Mintlify often use Title Case by convention
- **Product/feature names**: Preserved original capitalization for Block Public Access, Pay-by-Requester, Back-to-Origin, Content-MD5, etc.
- **API reference pages**: Headings in API reference that match HTTP method names (GET, PUT, DELETE) preserved as-is
- **resources and tools Next steps**: Many reference pages and FAQ pages don't naturally lead to a "next" step; these were left without forced Next steps sections

## Guidelines verified but no violations found

- **Guideline #2 (Hemingway style)**: Content is already concise and well-written
- **Guideline #3 (Idiomatic English)**: No word-for-word translation artifacts detected
- **Guideline #4 (User perspective naming)**: Uses "Upload", "Download", "Create" consistently
- **Guideline #14 (No in-page redundancy)**: No significant redundancy found
- **Guideline #17 (Prerequisites before code)**: All quickstart and guide pages follow the correct flow
- **Guideline #27 (Code example ordering)**: Python first, then Java, Go, Node.js consistently
