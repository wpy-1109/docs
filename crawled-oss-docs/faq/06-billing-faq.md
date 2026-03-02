# OSS Billing and Cost FAQ

Source: https://help.aliyun.com/zh/oss/faq-overview

## Billing Model FAQ

### How is OSS billed?

OSS uses a **pay-as-you-go** model by default. You can also purchase **resource packages** (subscriptions) for discounted rates.

| Billing Item | Charged By | Notes |
|---|---|---|
| Storage | GB/month by storage class | Standard > IA > Archive > Cold Archive |
| Outbound Traffic | GB of internet egress | Internal/inbound traffic is free |
| API Requests | Per 10,000 requests | GET and PUT are priced differently |
| Data Retrieval | GB (IA/Archive only) | Charged when reading IA/Archive data |
| Data Processing | Per request/GB | Image processing, video snapshots |
| Transfer Acceleration | GB of accelerated traffic | Additional to normal traffic |

### Is inbound traffic free?
Yes, uploading data to OSS (internet ingress) is **free**. Only outbound internet traffic is charged.

### Is internal traffic free?
Yes, traffic between OSS and other Alibaba Cloud services (ECS, Function Compute, etc.) in the **same region** using internal endpoints is free.

### How much does CDN back-to-origin cost?
CDN back-to-origin traffic to OSS is charged at a lower rate than direct internet outbound traffic. The exact rate depends on the region.

## Cost Reduction FAQ

### How do I avoid unexpected high bills?

1. **Set budget alerts** in Billing Console
2. **Enable Block Public Access** to prevent unauthorized public use
3. **Configure anti-hotlinking** to prevent bandwidth theft
4. **Monitor traffic** with CloudMonitor alerts
5. **Use lifecycle rules** to transition/delete cold data
6. **Clean up multipart fragments** (they consume storage)

### What are resource packages and when should I buy them?

Resource packages are prepaid quotas at discounted rates:
- **Storage packages**: Offset storage fees (20-30% savings)
- **Downstream traffic packages**: Offset outbound traffic fees
- **Request packages**: Offset API request fees

Buy when: You have predictable, sustained usage patterns.

### How do I identify what's costing the most?

1. Check **Billing Console > Bill Details** for breakdown by item
2. Use **CloudLens for OSS** to analyze per-Bucket usage
3. Export CSV usage reports for detailed analysis
4. Enable **Bucket inventory** for storage audits

### How does Intelligent Tiering work?

Intelligent Tiering automatically moves objects between access tiers based on access patterns:
- Frequently accessed objects stay in Standard tier
- Objects not accessed for 30+ days move to IA tier
- When accessed again, objects move back to Standard tier
- No retrieval fees (unlike manual IA storage)
- Small monitoring fee per object

### When is Archive storage cost-effective?

Archive storage costs ~75% less than Standard but has:
- 60-day minimum storage requirement
- Retrieval fees and restore time (~1 minute with Direct Read)
- Best for data accessed less than once per quarter
- Consider Cold Archive for even less frequent access (90%+ savings)
