---
name: api-workflow-planner
description: Plans and documents API integration workflows with authentication, endpoint mapping, data transformation, and error handling for connecting services programmatically. Use when the user says "plan an API integration between [service A] and [service B]", "how do I use the [API] to automate [task]", "API workflow for [use case]", "connect [app] to my system via API", or "what API calls do I need to automate [process]". Always use this skill — API integrations without a documented workflow plan frequently break in production due to missing auth refresh logic, unhandled error states, or incorrect data mapping.
---
# API Workflow Planner Skill

## Step 1 — Gather Inputs
- **APIs involved**: (which services' APIs are being used)
- **Goal**: What should the integration accomplish?
- **Authentication type**: API Key / OAuth2 / Basic Auth / JWT
- **Data flow direction**: Push / Pull / Bidirectional / Event-driven
- **Frequency**: Real-time / Scheduled / On-demand
- **Dev environment**: Language/framework (Python / Node.js / n8n / Make)

## Step 2 — API Integration Blueprint

```
## API Workflow: [Service A] ↔ [Service B]
Goal: [What this integration does end-to-end]
Auth: [Type] | Frequency: [How often]

---

AUTHENTICATION SETUP

[Service A] API:
- Auth type: [API Key / OAuth2 / Bearer]
- Where to get credentials: [Dashboard path]
- How to use: [Header name and format]
  Header: Authorization: Bearer {api_key}
  OR: X-API-Key: {api_key}
- Rate limits: [X requests per minute/hour/day]
- Token expiry: [If OAuth2 — how long before refresh needed]

[Service A] OAuth2 Refresh (if applicable):
POST {token_url}
Body: grant_type=refresh_token&refresh_token={token}&client_id={id}&client_secret={secret}
Store new access_token and expires_in for next refresh

---

ENDPOINT MAPPING

STEP 1 — [Fetch/Get data]
Method: GET
Endpoint: {base_url}/[endpoint_path]
Headers:
  Authorization: Bearer {token}
  Content-Type: application/json
Query params:
  limit: 100
  page: {{page_number}}
  filter: [field]=[value]

Response structure:
{
  "data": [...],
  "pagination": {
    "total": 500,
    "next_cursor": "abc123"
  }
}

Extract: data[].field_name for each item

---

STEP 2 — [Transform data]
Map fields from [Source API] to [Destination API] format:

Source field → Destination field
{source.id} → external_id
{source.name} → full_name
{source.email} → email_address
{source.created_at} → created (convert: ISO8601 → Unix timestamp)
{source.tags[]} → labels (convert: array → comma-separated string)

---

STEP 3 — [Send/Create data]
Method: POST
Endpoint: {base_url}/[destination_endpoint]
Headers:
  Authorization: Bearer {token}
  Content-Type: application/json
Body:
{
  "external_id": "{{mapped_id}}",
  "full_name": "{{mapped_name}}",
  "email_address": "{{mapped_email}}"
}

Success response: 201 Created
Response body: { "id": "new_record_id" }

Store: Save [source_id → destination_id] mapping for future updates

---

STEP 4 — [Handle pagination]
If response.pagination.next_cursor exists:
  Repeat Step 1 with cursor param added
  Continue until no cursor returned

---

STEP 5 — [Update / Upsert logic]
Check if record already exists:
  GET {base_url}/records?external_id={source_id}
  If 200 and data.length > 0: PUT to update
  If 404 or empty: POST to create

---

ERROR HANDLING MATRIX
| HTTP Status | Meaning | Action |
|-------------|---------|--------|
| 200/201 | Success | Continue |
| 400 | Bad request | Log payload + error, skip record |
| 401 | Unauthorized | Refresh token and retry once |
| 403 | Forbidden | Alert — check permissions |
| 404 | Not found | Skip or create new |
| 429 | Rate limited | Wait {Retry-After} seconds, retry |
| 500/502 | Server error | Wait 30s, retry up to 3× |
| Other | Unknown | Log full response, alert |

---

IMPLEMENTATION CODE STRUCTURE
```python
import requests, time

class APIClient:
    def __init__(self, api_key):
        self.base_url = "https://api.service.com/v1"
        self.headers = {"Authorization": f"Bearer {api_key}"}
    
    def get_with_retry(self, endpoint, params=None, retries=3):
        for attempt in range(retries):
            response = requests.get(
                f"{self.base_url}{endpoint}",
                headers=self.headers,
                params=params
            )
            if response.status_code == 429:
                time.sleep(int(response.headers.get("Retry-After", 60)))
                continue
            response.raise_for_status()
            return response.json()
        raise Exception(f"Failed after {retries} retries")
```

---

LOGGING & MONITORING
Log per record:
- source_id, destination_id, status, timestamp, error_message (if any)

Alert on:
- Consecutive failures > 3
- Success rate < 95% in a batch
- Auth token expiry approaching

---

TESTING PLAN
1. Unit test: Test each API call in isolation with mock responses
2. Integration test: Run full flow with [test/sandbox environment]
3. Edge case test: Empty dataset / single record / max batch size / duplicate records
4. Production test: Run on 10 records first, verify manually, then full batch
```

Always offer: "Want me to write the complete Python implementation of this integration?"
