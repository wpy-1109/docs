# Technical Accuracy Review Report

**Reviewer:** tech-reviewer
**Date:** 2026-03-02
**Scope:** All documentation sections (Get Started, Guides, SDKs, API Reference, Tools, Resources)

---

## Summary

Reviewed 400+ MDX files across all documentation sections, comparing content against 1,056 crawled source files from Alibaba Cloud's official OSS documentation. The documentation is **largely accurate** with good technical quality. Found and fixed several issues, mostly related to missing content, a version discrepancy, and an API parameter inaccuracy.

### Issues Found and Fixed

| # | Section | File | Issue | Severity | Status |
|---|---------|------|-------|----------|--------|
| 1 | Get Started | `concepts/regions-and-endpoints.mdx` | **Missing region**: Mexico (`na-south-1`) was absent from the regions table despite being in the official docs | Medium | **Fixed** |
| 2 | Get Started | `concepts/regions-and-endpoints.mdx` | **Missing CNAME policy notice**: Starting March 2025, new users in Chinese mainland regions must use custom domain names (CNAME) for data API operations. This critical policy change was not mentioned | High | **Fixed** |
| 3 | Get Started | `concepts/regions-and-endpoints.mdx` | **Dual-stack scope**: Dual-stack endpoints described as "select regions only" -- clarified to "select China and Europe regions only" since most non-China regions don't support dual-stack | Low | **Fixed** |
| 4 | Get Started | `concepts/access-control-overview.mdx` | **STS expiration range**: Listed as "15 minutes to 1 hour" but STS tokens can last up to 12 hours by default. Fixed to "15 minutes to 12 hours" | Medium | **Fixed** |
| 5 | Get Started | `quickstart/sdk.mdx` | **Java SDK version**: Maven dependency listed version `3.17.4` but crawled source shows `3.18.1` | Medium | **Fixed** |
| 6 | API Reference | `object-basic/PutObject.mdx` | **Incorrect encryption values**: Listed `SM4` as valid for `x-oss-server-side-encryption` header, but SM4 is only valid for `KMSDataEncryption` sub-parameter. Removed SM4 from the header values | Medium | **Fixed** |
| 7 | API Reference | `object-basic/PutObject.mdx` | **Incorrect error code**: Listed `EntityTooLarge` for objects exceeding 5 GB, but the actual error code per crawled source is `InvalidArgument` | Low | **Fixed** |
| 8 | API Reference | `overview.mdx` | **Broken link**: Referenced `/resources/limits` which doesn't exist. Corrected to `/get-started/concepts/limits` | Low | **Fixed** |

### Issues Noted (Not Fixed - Structural/Config)

| # | Section | Issue | Severity |
|---|---------|-------|----------|
| 9 | Root | `docs.json` still uses default Mintlify Starter Kit navigation. All OSS content is unreachable from the sidebar navigation. Needs full reconfiguration. | Critical |
| 10 | Get Started | Quickstart SDK page uses V1 SDKs (oss2, OSSClientBuilder, aliyun-oss-go-sdk) while Guides pages use V2 SDKs. Both are technically correct but the inconsistency may confuse users. Consider adding a note in the quickstart that V2 is recommended for new projects. | Low |

---

## Detailed Findings by Section

### 1. Get Started (13 pages) -- HIGH PRIORITY

**Overall:** Good accuracy. Key concepts (buckets, objects, storage classes, regions, access control, consistency model, limits, naming conventions) are well-represented and technically correct.

**Verified against crawled sources:**
- `what-is-oss.mdx` -- Durability (12 nines), availability (99.995%), 48.8 TB max via multipart, 100 Gbps bandwidth all match source
- `concepts/buckets.mdx` -- Bucket limits (100/region, 1000 lifecycle rules, LRS/ZRS durability) all correct
- `concepts/objects.mdx` -- Object types (Normal, Multipart, Appendable, Symlink), size limits (5 GB simple, 48.8 TB multipart), key rules (1-1023 bytes, UTF-8, no leading /) all correct
- `concepts/storage-classes.mdx` -- Five classes, minimum storage durations (30/60/180/180 days), restore times all match source
- `concepts/consistency-model.mdx` -- Strong read-after-write consistency accurately described
- `concepts/regions-and-endpoints.mdx` -- Region IDs, public/internal endpoint formats all correct. Added missing Mexico region and CNAME notice
- `concepts/limits.mdx` -- Bandwidth, QPS, image processing limits all match source
- `concepts/naming-conventions.mdx` -- Rules accurate (3-63 chars, lowercase, globally unique)
- `quickstart/console.mdx` -- Steps accurate and complete
- `quickstart/sdk.mdx` -- SDK code examples syntactically correct for all 4 languages. Fixed Java version
- `quickstart/cli.mdx` -- ossutil commands correct (cp, ls, mb, rb)

### 2. Guides (88 pages)

**Overall:** Good technical accuracy. Code examples use correct V2 SDK APIs. Compared key pages against crawled sources.

**Verified pages:**
- `objects/upload-objects.mdx` -- V2 SDK code for Python, Java, Go, Node.js verified against crawled source. Method names, import paths, and API patterns correct
- `objects/multipart-upload.mdx` -- Three-step process (Initiate/Upload/Complete) correct. Part limits (100 KB min, 10,000 max) match source
- `access-control/presigned-urls.mdx` -- 7-day max validity correct. V2 SDK presign API correct
- `data-management/versioning.mdx` -- Three states (Unversioned/Enabled/Suspended) and irreversibility correct
- `data-management/lifecycle-rules.mdx` -- Rule types and V2 SDK API calls verified
- `security/server-side-encryption.mdx` -- SSE-OSS/SSE-KMS/SSE-C distinction correct

**Security check:** All code examples use environment variables or STS for credentials. No hardcoded keys found. Appropriate warnings about credential security included.

### 3. SDKs (114 pages) -- Focus: Python, Java, Go, Node.js

**Overall:** Good accuracy. Both V1 and V2 SDK code examples verified.

**Python SDK:**
- Installation: `pip install alibabacloud-oss-v2` (V2) and `pip install oss2` (V1) correct
- Initialization: V1 `oss2.ProviderAuthV4(EnvironmentVariableCredentialsProvider())` matches crawled source
- V2 `oss.credentials.EnvironmentVariableCredentialsProvider()` and `oss.config.load_default()` pattern correct

**Java SDK:**
- Installation: Maven artifact `com.aliyun.oss:aliyun-sdk-oss` (V1), `com.aliyun.oss:alibabacloud-oss-sdk-java-v2` (V2) correct
- V1 imports (`com.aliyun.oss.OSS`, `OSSClientBuilder`) match source
- V2 imports (`com.aliyun.sdk.service.oss2.*`) match crawled source
- JAXB dependency note for Java 9+ present

**Go SDK:**
- V1 (`github.com/aliyun/aliyun-oss-go-sdk/oss`) and V2 (`github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss`) imports match source
- Go 1.18+ requirement noted

**Node.js SDK:**
- `ali-oss` package name correct
- `authorizationV4: true` option matches crawled source
- `region: 'oss-cn-hangzhou'` format correct

### 4. API Reference (163 pages) -- Spot Check

**Overall:** Well-structured. Verified PutObject, common headers, error codes, and Signature V4.

**Verified:**
- `PutObject.mdx` -- Request/response format, headers (Content-Type, x-oss-storage-class, x-oss-server-side-encryption, x-oss-forbid-overwrite, x-oss-tagging, x-oss-meta-*) all match crawled source
- `common-headers.mdx` -- Request headers (Authorization, Content-Length, Date, Host, x-oss-date, x-oss-content-sha256, x-oss-security-token) and response headers (ETag, x-oss-request-id) correct
- `signature-v4.mdx` -- Three-step signing process (canonical request, string to sign, calculate signature) accurately matches crawled source. Key derivation chain (`aliyun_v4 + Secret -> DateKey -> DateRegionKey -> DateRegionSvcKey -> SigningKey`) correct. `UNSIGNED-PAYLOAD` as only supported Hashed Payload value confirmed
- `error-codes.mdx` -- Error codes, HTTP status codes, and descriptions match crawled troubleshooting source

### 5. Tools (15 pages)

**Overall:** Good accuracy.

**Verified:**
- `ossutil/commands.mdx` -- Command structure, cp/ls/rm/mb/rb/sync/stat/sign commands all match crawled ossutil 2.0 reference
- Flag names and descriptions accurate

### 6. Resources (26 pages)

**Overall:** Good accuracy.

**Verified:**
- `s3-compatibility.mdx` -- Compatible operations list, virtual-hosted style requirement, ACL differences, storage class mapping, ETag case differences all accurate against crawled source
- `pricing/overview.mdx` -- Three billing methods (pay-as-you-go, resource plans, SCUs) match source

---

## Terminology Consistency Check

Verified consistent use of:
- "bucket" / "object" / "key" -- used consistently throughout
- "region" / "endpoint" -- correctly differentiated
- "AccessKey pair" / "AccessKey ID" / "AccessKey Secret" -- consistent naming
- "RAM" / "STS" / "ACL" -- consistently used
- "Standard" / "IA" / "Archive" / "Cold Archive" / "Deep Cold Archive" -- storage class names consistent
- "LRS" / "ZRS" -- redundancy type names consistent

---

## Recommendations

1. **Update `docs.json`**: The navigation configuration still uses the default Mintlify template. This must be updated to include all OSS documentation sections before deployment.

2. **SDK version note in Quickstart**: Add a note in `get-started/quickstart/sdk.mdx` indicating that V2 SDKs are recommended for new projects, since the quickstart currently uses V1 SDKs while guides use V2.

3. **Keep SDK versions up to date**: SDK dependency versions (e.g., Java `3.18.1`) will become stale over time. Consider using "LATEST" or including a note to check for the latest version.

4. **Monitor the CNAME policy**: The March 2025 CNAME requirement for Chinese mainland regions may expand in scope. Keep the warning updated as Alibaba Cloud releases further announcements.
