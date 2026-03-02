# Mintlify Best Practices Research

## Overview

Mintlify is an AI-native documentation platform designed for developers, offering beautiful out-of-the-box themes, a web editor, and rich interactive components. Documentation is written in MDX (Markdown + JSX) and configured through a central `docs.json` file.

---

## 1. Available Components

### Content Display

| Component | Purpose | Usage |
|-----------|---------|-------|
| **Card** | Clickable element with title, icon, and optional link | Feature highlights, navigation shortcuts |
| **CardGroup** | Container for grouping multiple cards | Landing pages, feature overviews |
| **Columns** | Multi-column layout | Side-by-side comparisons, paired content |
| **Tabs / Tab** | Switchable content panels | Language-specific content, OS-specific instructions |
| **CodeGroup** | Tabbed code examples across languages | Multi-language SDK examples |
| **Steps / Step** | Numbered step-by-step guides | Tutorials, setup instructions |
| **Accordion / AccordionGroup** | Collapsible content sections | FAQs, optional details |
| **Expandable** | Collapsible long code blocks | Lengthy code examples |

### Callout Boxes

| Component | Purpose | Visual Style |
|-----------|---------|-------------|
| **`<Info>`** | Informational context | Blue/neutral |
| **`<Warning>`** | Caution or irreversible actions | Yellow/orange |
| **`<Tip>`** | Helpful hints and shortcuts | Green |
| **`<Note>`** | General supplementary notes | Gray/neutral |

### Code & Diagrams

| Component | Purpose |
|-----------|---------|
| **Fenced code blocks** | Syntax-highlighted code with file names, line highlighting |
| **Expandable code blocks** | Long code that can be collapsed/expanded |
| **Mermaid diagrams** | Flowcharts, sequence diagrams, etc. via mermaid code blocks |
| **LaTeX** | Mathematical expressions |
| **Frame** | Embed iframes or visual content |

### Example: Tabs with Code

```mdx
<Tabs>
  <Tab title="Python">
    ```python
    import oss2
    auth = oss2.Auth('access_key_id', 'access_key_secret')
    bucket = oss2.Bucket(auth, 'endpoint', 'bucket-name')
    ```
  </Tab>
  <Tab title="Java">
    ```java
    OSS ossClient = new OSSClientBuilder().build(endpoint, accessKeyId, accessKeySecret);
    ```
  </Tab>
</Tabs>
```

### Example: Steps

```mdx
<Steps>
  <Step title="Create a Bucket">
    Navigate to the OSS console and click "Create Bucket".
  </Step>
  <Step title="Upload an Object">
    Use the console or SDK to upload your first file.
  </Step>
  <Step title="Set Permissions">
    Configure access control policies for your bucket.
  </Step>
</Steps>
```

### Example: Cards

```mdx
<Card title="Quick Start" icon="rocket" href="/quickstart">
  Get up and running with OSS in minutes.
</Card>
```

---

## 2. Navigation Configuration

Mintlify uses `docs.json` for all navigation configuration. Key patterns:

### Tabs

Top-level navigation tabs to separate major documentation sections:

```json
{
  "navigation": {
    "tabs": [
      {
        "tab": "Documentation",
        "groups": [...]
      },
      {
        "tab": "API Reference",
        "openapi": "openapi.json"
      }
    ]
  }
}
```

### Groups

Organize pages within tabs into logical groups:

```json
{
  "group": "Getting Started",
  "icon": "rocket",
  "pages": [
    "index",
    "quickstart",
    "installation"
  ]
}
```

### Dropdowns

Alternative to tabs for more complex navigation:

```json
{
  "navigation": [
    {
      "language": "en",
      "dropdowns": [
        {
          "dropdown": "Docs",
          "icon": "book",
          "description": "Product documentation",
          "pages": [
            {
              "group": "Getting Started",
              "pages": ["index", "quickstart"]
            }
          ]
        }
      ]
    }
  ]
}
```

### Multi-Language Support

```json
{
  "navigation": {
    "languages": [
      {
        "language": "en",
        "tabs": [...]
      },
      {
        "language": "zh",
        "tabs": [...]
      }
    ]
  }
}
```

---

## 3. docs.json Configuration Options

### Core Settings

```json
{
  "name": "Alibaba Cloud OSS",
  "logo": {
    "light": "/logo-light.svg",
    "dark": "/logo-dark.svg",
    "href": "https://www.alibabacloud.com"
  },
  "favicon": "/favicon.png",
  "colors": {
    "primary": "#FF6A00",
    "light": "#FF8C33",
    "dark": "#CC5500"
  }
}
```

### Navbar Configuration

```json
{
  "navbar": {
    "links": [
      {
        "label": "Community",
        "href": "https://community.example.com"
      }
    ],
    "primary": {
      "type": "button",
      "label": "Get Started",
      "href": "https://example.com/start"
    }
  }
}
```

### Footer Configuration

```json
{
  "footer": {
    "socials": {
      "github": "https://github.com/example",
      "x": "https://x.com/example"
    },
    "links": [
      {
        "header": "Resources",
        "items": [
          { "label": "Blog", "href": "https://example.com/blog" }
        ]
      }
    ]
  }
}
```

### Integrations

```json
{
  "integrations": {
    "ga4": { "measurementId": "G-XXXXXXXXXX" },
    "telemetry": { "enabled": true }
  }
}
```

### Error Pages

```json
{
  "errors": {
    "404": {
      "redirect": false,
      "title": "Page Not Found",
      "description": "The page you are looking for does not exist."
    }
  }
}
```

### Contextual Menu

```json
{
  "contextual": {
    "options": ["copy", "view", "chatgpt", "claude"]
  }
}
```

---

## 4. API Reference Setup & OpenAPI Integration

### Automatic Generation

Mintlify can auto-generate API reference pages from OpenAPI/Swagger specs:

```json
{
  "navigation": {
    "groups": [
      {
        "group": "API Reference",
        "openapi": "openapi.json"
      }
    ]
  }
}
```

### Dedicated API Tab

```json
{
  "navigation": {
    "tabs": [
      {
        "tab": "API Reference",
        "openapi": "https://example.com/api/v3/openapi.json"
      }
    ]
  }
}
```

### Selective Endpoints

```json
{
  "navigation": {
    "groups": [
      {
        "group": "API Reference",
        "openapi": "/path/to/openapi.json",
        "pages": [
          "GET /users",
          "POST /users"
        ]
      }
    ]
  }
}
```

### Features
- Built-in API playground for testing endpoints
- Auto-generated request/response examples
- Authentication configuration
- Support for OpenAPI 3.0 and Swagger 2.0
- Interactive parameter editing

---

## 5. Snippets & Reusable Content

### Creating Snippets

Create reusable content in a `/snippets` directory:

```mdx
// snippets/prerequisites.mdx
<Info>
  Before you begin, ensure you have:
  - An Alibaba Cloud account
  - An AccessKey pair (AccessKey ID and AccessKey Secret)
  - OSS activated in your account
</Info>
```

### Using Snippets

Import and use snippets in any page:

```mdx
import Prerequisites from '/snippets/prerequisites.mdx';

# Quick Start

<Prerequisites />

## Step 1: Create a Bucket
...
```

### Best Practices for Snippets
- Use for repeated content (prerequisites, warnings, setup steps)
- Keep snippets focused and single-purpose
- Name clearly to indicate content
- Store in a dedicated `/snippets` directory

---

## 6. SEO & Metadata Configuration

### Page-Level Frontmatter

```yaml
---
title: "Upload Objects to OSS"
sidebarTitle: "Upload Objects"
description: "Learn how to upload objects to Alibaba Cloud OSS using the console, CLI, or SDK."
"og:title": "Upload Objects to Alibaba Cloud OSS"
"og:description": "Step-by-step guide for uploading objects to OSS."
"og:image": "/images/upload-og.png"
---
```

### Built-in SEO Features
- Automatic sitemap generation
- Canonical URL handling
- Open Graph and Twitter card metadata
- Meta tags configurable globally or per-page
- Clean URL structure

---

## 7. Theming & Branding

### Color Configuration

```json
{
  "colors": {
    "primary": "#FF6A00",
    "light": "#FF8C33",
    "dark": "#CC5500",
    "background": {
      "light": "#FFFFFF",
      "dark": "#0D0D0D"
    }
  }
}
```

### Logo & Favicon

```json
{
  "logo": {
    "light": "/logo-light.svg",
    "dark": "/logo-dark.svg",
    "href": "https://www.alibabacloud.com"
  },
  "favicon": "/favicon.png"
}
```

### Features
- Built-in dark/light mode toggle
- Custom CSS overrides supported
- Custom font configuration
- Topbar, sidebar, and footer customization
- Responsive design out of the box

---

## 8. Search Configuration

- Built-in full-text search across all documentation
- AI-powered search capabilities
- No additional configuration required for basic search
- Search results show page title, description, and content preview
- Integrates with Mintlify's AI chatbot for conversational search

---

## 9. Deployment & Custom Domain

### Git-Based Deployment
- Connect a GitHub repository
- Auto-deploy on push to main branch
- Preview deployments for pull requests
- CLI (`mintlify dev`) for local development

### Custom Domain Setup
1. Add CNAME record pointing to Mintlify servers
2. Configure in Mintlify dashboard
3. SSL certificates provisioned automatically
4. Example: `docs.alibabacloud.com`

### Development Workflow
1. Write content in MDX files
2. Preview locally with `mintlify dev`
3. Push to GitHub
4. Automatic deployment
5. Preview URLs for PRs

---

## 10. Content Organization Best Practices

### Recommended Directory Structure

```
docs/
  docs.json              # Central configuration
  index.mdx              # Landing page
  quickstart.mdx         # Getting started guide
  concepts/              # Conceptual documentation
    buckets.mdx
    objects.mdx
    regions.mdx
  guides/                # How-to guides
    upload.mdx
    download.mdx
    access-control.mdx
  api-reference/         # API documentation
    openapi.json
  sdk/                   # SDK documentation
    python.mdx
    java.mdx
    nodejs.mdx
  snippets/              # Reusable content
    prerequisites.mdx
    common-errors.mdx
  images/                # Static assets
  logo-light.svg
  logo-dark.svg
  favicon.png
```

### Content Writing Guidelines
- Use frontmatter for metadata on every page
- Start each page with a clear title and description
- Use components (Steps, Tabs, Cards) to break up long content
- Include code examples for every SDK operation
- Use callout boxes for warnings, tips, and important notes
- Keep pages focused on a single topic
- Cross-link related pages extensively
- Use CodeGroup for multi-language examples
