# Editorial Review Guidelines

## I. Writing Style

### 1. Sentence case for English headings
No Title Case. Product names and proper nouns keep original capitalization.

### 2. Hemingway style
Short sentences. No fluff. No redundancy. Chinese source material is reference only — output must be English.

### 3. Natural, concise translation
No word-for-word translation. Use idiomatic target-language expressions while keeping it concise.

---

## II. Naming & Terminology

### 4. User perspective naming, not platform perspective
- **Upload** a model > **Import** a model
- **Get** an API key > **Issue** an API key
- **Deploy** a model > **Provision** a deployment

### 5. Plain words over academic terms
- "Text to speech" > "Speech Synthesis"
- Use well-known abbreviations directly (e.g., OCR)

### 6. Technical abbreviation format
- Abbreviation first if widely known: SFT (supervised fine-tuning)
- Description first if more intuitive: Control pronunciation (SSML)

### 7. Question/action-oriented headings
- "Which model should I use?" > "Model selection guide"

---

## III. Information Architecture

### 8. Separate Guides from API Reference
API Reference describes interfaces. Guides teach strategy and best practices.

### 9. Organize by user scenario, not by model/feature
Group docs by user tasks/scenarios. One scenario may involve multiple models.

### 10. One classification dimension per level
Don't mix capability dimension with lifecycle dimension at the same navigation level.

### 11. No group wrapper for single pages
If a group contains only one page, remove the group level.

### 12. Merge related content, elevate title abstraction
Combine similar features into one doc with a higher-level title.

### 13. Keep related content adjacent in navigation
Similar groups should be neighbors, not separated by unrelated content.

### 14. Eliminate in-page information redundancy
Don't repeat the same information in different sections of the same page.

### 15. Treat all models equally
Users don't care if a model is first-party or third-party. Present selection comparisons uniformly.

---

## IV. Page Structure

### 16. Guide structure: Why → Get started → Get great
Don't put "How it works" first. Lead with value.

### 17. Prerequisites before code examples
Page flow: Overview → Models → Setup → Code → Next steps.

### 18. End every page with Next Steps
Recommend related advanced content to guide users forward.

---

## V. Content Quality

### 19. Beyond "it works" — help users achieve excellence
Getting started is the baseline. Good guides provide optimization strategies, creative architectures, and production-grade patterns.

### 20. Comparison tables over opinionated recommendations
When options are close, give comparison tables with detailed criteria. Don't make subjective recommendations.

### 21. Experience over description
Interactive examples, audio samples, and demos beat walls of text.

### 22. Cross-functional optimization
Don't just document single API usage. Show systematic optimization combining multiple tools.

### 23. Verify latest info for model recommendations
Models iterate fast. Recommendations must be current.

---

## VI. Methodology

### 24. Research competitors before design decisions
When naming or architecture is debatable, research 2-3 competitors (AWS, GCP, Azure) first.

### 25. Self-verify after changes
Run/check actual results after making changes. Don't claim completion without verification.

---

## VII. Tool Preferences

### 26. Prefer MCP Fetch for web requests
Do not use WebFetch(url, prompt). Use local `agent-browser` CLI as fallback.

### 27. API code example language order
cURL → Python → Node.js first. Others by AI development language popularity.
