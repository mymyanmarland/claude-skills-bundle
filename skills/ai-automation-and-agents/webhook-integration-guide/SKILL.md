---
name: webhook-integration-guide
description: Guides users through setting up, testing, and debugging webhook integrations between any two services for real-time automation triggers. Use when the user says "set up a webhook for", "webhook between [app A] and [app B]", "how do webhooks work", "my webhook isn't firing", "webhook for [trigger event]", or "connect [service] to [service] with a webhook". Always use this skill — webhooks are the backbone of real-time automation and most errors come from payload structure mismatches, authentication issues, or incorrect endpoint configuration.
---
# Webhook Integration Guide Skill

## Step 1 — Gather Inputs
- **Sending service**: (where the webhook originates — Stripe / GitHub / Shopify / Typeform / custom app)
- **Receiving service**: (where data goes — n8n / Make / Zapier / your server / custom endpoint)
- **Trigger event**: (what action fires the webhook — payment completed / form submitted / repo pushed / etc.)
- **Goal**: What should happen when the webhook fires?
- **Authentication method**: None / Secret header / HMAC signature / Basic auth / Bearer token
- **Environment**: Development / Production

## Step 2 — Webhook Setup Guide

```
## Webhook Integration: [Sender] → [Receiver]
Trigger: [Event] | Auth: [Method]

---

STEP 1: GET YOUR WEBHOOK ENDPOINT URL

In [receiving service — e.g., n8n]:
1. Create new workflow
2. Add Webhook node as trigger
3. Set method: POST (almost always POST)
4. Copy the webhook URL:
   Test URL: https://[your-n8n]/webhook-test/[path]
   Production URL: https://[your-n8n]/webhook/[path]

Note: Use TEST URL while building; switch to PRODUCTION URL when live.

---

STEP 2: CONFIGURE THE SENDING SERVICE

In [sending service — e.g., Stripe]:
1. Go to: [Exact navigation path — e.g., Dashboard → Developers → Webhooks]
2. Click: "Add endpoint" / "Create webhook"
3. Paste your webhook URL
4. Select events to listen for:
   - [Event 1: e.g., payment_intent.succeeded]
   - [Event 2: e.g., customer.subscription.deleted]
5. [If secret available]: Copy the webhook signing secret — you'll need this

---

STEP 3: AUTHENTICATE THE WEBHOOK

[If HMAC signature verification — e.g., Stripe, GitHub]:
The sender signs each request with a secret key.
In your receiver, verify the signature before processing:

n8n: Add "Header Auth" with secret in Webhook node settings
Custom endpoint:
```python
import hmac, hashlib
def verify_signature(payload, signature, secret):
    expected = hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(f"sha256={expected}", signature)
```

[If Bearer token]:
Add header: Authorization: Bearer [your-token]
In n8n: Set Header Auth → Token

[If no auth — only for internal/trusted sources]:
Consider adding IP allowlisting instead

---

STEP 4: UNDERSTAND THE PAYLOAD STRUCTURE

[Sender] sends this JSON payload on [event]:
```json
{
  "id": "evt_[unique_id]",
  "type": "[event.name]",
  "data": {
    "object": {
      "[field_1]": "[value]",
      "[field_2]": "[value]",
      "[nested_object]": {
        "[field]": "[value]"
      }
    }
  },
  "created": 1234567890
}
```

Key fields you'll use:
- [Field path 1]: {{ $json.data.object.field_name }}
- [Field path 2]: {{ $json.data.object.nested.field }}
- [Event type check]: {{ $json.type }}

---

STEP 5: TEST THE WEBHOOK

Method A — Sender's test tool:
[Service name] → [Navigate to webhook settings] → "Send test event"
Watch for the payload arriving in your receiver's test execution.

Method B — Use webhook.site:
1. Go to webhook.site — get a temporary URL
2. Paste it as your webhook endpoint in the sender
3. Trigger the event manually
4. Inspect the full payload structure before building your workflow

Method C — curl (for custom endpoints):
```bash
curl -X POST https://your-endpoint.com/webhook \
  -H "Content-Type: application/json" \
  -H "X-Signature: [test-sig]" \
  -d '{"test": "payload", "field": "value"}'
```

---

STEP 6: BUILD THE RESPONSE LOGIC

[Receiving service] workflow after webhook fires:

Webhook → [Your processing nodes] → [Action]

Important: Always return HTTP 200 immediately.
If processing takes time, queue it asynchronously — the sender will retry if no 200 received within [X] seconds.

Quick 200 response in n8n: Set "Response Mode" to "Immediately"
```

## Step 3 — Debugging Common Webhook Problems

| Problem | Likely cause | Fix |
|---------|-------------|-----|
| Webhook not firing | Event not selected / wrong URL | Verify event is enabled in sender settings |
| 401 Unauthorized | Auth header wrong | Check secret key matches exactly |
| 400 Bad Request | Payload format mismatch | Log raw payload, check Content-Type header |
| Webhook fires but no action | Workflow not active | Switch n8n/Make workflow to Active |
| Duplicate events | No idempotency check | Store event IDs, check before processing |
| Retries piling up | Slow processing / no 200 | Respond 200 immediately, process async |
| Signature verification failing | Timing attack protection | Use constant-time comparison function |

## Step 4 — Webhook Security Checklist
- [ ] Always verify signature if the sender provides one
- [ ] Return 200 before processing (prevents retries)
- [ ] Log all incoming webhooks for debugging
- [ ] Implement idempotency (same event_id = ignore)
- [ ] Use HTTPS endpoints only (never HTTP in production)
- [ ] Rotate webhook secrets if compromised

Always offer: "Want me to write the exact n8n node configuration for this webhook?"
