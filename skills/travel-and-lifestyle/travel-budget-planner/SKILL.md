---
name: travel-budget-planner
description: Estimates trip costs by category, builds a daily spend target, and helps travelers stay on budget with money-saving strategies. Use this skill whenever the user wants to budget a trip or says things like "how much will [destination] cost", "trip budget for [place]", "daily budget for [country]", "is [destination] expensive", "help me plan my travel budget", "how much money should I bring", or "travel cost estimate for [trip]". Also trigger when the user asks how to travel cheaply or wants to compare costs between destinations. Always use this skill — most trips go over budget due to poor planning, and a realistic upfront estimate prevents financial stress mid-trip.
---

# Travel Budget Planner Skill

Build a realistic, category-by-category travel budget before you go.

## Step 1 — Gather Inputs

Ask in one message if not provided:
- **Destination(s)**
- **Duration**: How many nights?
- **Travel party**: Solo / Couple / Group of X
- **Budget style**: Backpacker / Budget / Mid-range / Comfort / Luxury
- **Origin city**: (for flight cost estimates)
- **Travel dates or season**: (affects flight prices significantly)
- **Accommodation preference**: Hostel / Budget hotel / Mid-range / Boutique / Luxury
- **Trip type**: City break / Beach / Adventure / Multiple countries

---

## Step 2 — Destination Cost Level

```
## 💰 Destination Cost Overview: [Country/City]

**Overall cost level**: 💰 Budget / 💰💰 Mid-range / 💰💰💰 Expensive / 💰💰💰💰 Very expensive

**Currency**: [Name + symbol]
**Approx. exchange rate**: 1 USD = [X local currency]

**Daily budget benchmarks** (per person):
| Style | Daily Budget |
|-------|-------------|
| 🎒 Backpacker | $XX–XX/day |
| 💰 Budget traveler | $XX–XX/day |
| 💰💰 Mid-range | $XX–XX/day |
| 💰💰💰 Comfort | $XX–XX/day |
| 💰💰💰💰 Luxury | $XXX+/day |

**Your target style**: [User's style] → ~$XX–XX/day
```

---

## Step 3 — Full Budget Breakdown

```
## 📊 Trip Budget: [Destination] — [X] Nights
**Party**: [X person(s)] | **Style**: [Budget style]
*All estimates in USD — adjust for actual exchange rates*

---

### ✈️ Flights

| Route | Estimate | Notes |
|-------|----------|-------|
| [Origin] → [Destination] | $XXX–XXX | [Economy / direct vs. connecting] |
| Return flight | [Included above / separate] | |
| **Subtotal flights** | **$XXX–XXX** | Per person |

**Flight savings tips**:
- Book 6–8 weeks ahead for short-haul; 3–6 months for long-haul
- Flexible dates: mid-week (Tue/Wed) 15–30% cheaper than weekends
- Use Google Flights price calendar to find cheapest days
- Consider nearby airports
- Budget airlines for short hops — but factor in bag fees

---

### 🏨 Accommodation

| Type | Cost/Night | X Nights | Subtotal |
|------|-----------|---------|---------|
| [Hotel/hostel/Airbnb type] | $XX | X | $XXX |
| **Total accommodation** | | | **$XXX** |

*[If couple/group: shared room cost ÷ party size]*

**Accommodation savings tips**:
- Book directly with hotels — often 5–10% cheaper than OTAs
- Hostels for solo travelers: private rooms still cheaper than hotels
- Apartments for 7+ nights: significantly cheaper per night
- Check-in Sunday/Monday: often cheapest nights

---

### 🍽️ Food & Drink

| Meal | Cost/Person | × Meals | Subtotal |
|------|------------|---------|---------|
| Breakfast | $X–X | X (skip 2 = hotel incl.) | $XX |
| Lunch | $X–XX | X | $XX |
| Dinner | $XX–XX | X | $XX |
| Coffee/snacks/drinks | $X–X/day | X days | $XX |
| **Total food** | | | **$XXX** |

**Food savings tips**:
- Lunch is the big meal in many countries — cheaper and larger than dinner
- Markets and street food cut costs by 60–70% vs. restaurants
- One splurge dinner per trip is worth it — skip 2 budget lunches to fund it
- Grocery stores for breakfast items: saves $X–X/day

---

### 🚌 Local Transport

| Item | Cost | Qty | Subtotal |
|------|------|-----|---------|
| Airport transfers (each way) | $XX | 2 | $XX |
| Metro/bus daily pass | $X | X days | $XX |
| Taxis/ride-hailing (estimate) | $X–X/ride | X rides | $XX |
| Day trips / excursions transport | $XX | X | $XX |
| **Total transport** | | | **$XXX** |

---

### 🎭 Activities & Attractions

| Activity | Cost/Person | Qty | Subtotal |
|----------|------------|-----|---------|
| [Major attraction 1] | $XX | 1 | $XX |
| [Major attraction 2] | $XX | 1 | $XX |
| [Walking tour / guided tour] | $XX | 1 | $XX |
| [Experience — cooking class, boat trip, etc.] | $XX | 1 | $XX |
| Free activities (parks, markets, beaches) | $0 | — | $0 |
| **Total activities** | | | **$XXX** |

**Activity savings tips**:
- Many museums free on first Sunday of month
- City tourist cards: calculate if worth it based on what you'll actually use
- Free walking tours: tip-based, usually excellent
- Book online in advance: 10–20% discount at many attractions

---

### 🛍️ Shopping & Souvenirs

| Category | Estimate |
|----------|---------|
| Souvenirs | $XX–XX |
| Personal shopping (clothes, etc.) | $XX |
| [Destination-specific — e.g., spices, crafts] | $XX |
| **Total shopping** | **$XX–XXX** |

---

### 💊 Health & Misc

| Item | Cost |
|------|------|
| Travel insurance | $XX–XX |
| Visas / entry fees | $XX |
| SIM card / data | $XX |
| Vaccinations (if needed) | $XX |
| Laundry | $X–X |
| Tips | $XX |
| **Total misc** | **$XXX** |

---

## 💵 Total Budget Summary

| Category | Low Estimate | High Estimate |
|----------|-------------|--------------|
| Flights | $XXX | $XXX |
| Accommodation | $XXX | $XXX |
| Food & drink | $XXX | $XXX |
| Local transport | $XX | $XX |
| Activities | $XX | $XX |
| Shopping | $XX | $XX |
| Health & misc | $XX | $XX |
| **TOTAL** | **$X,XXX** | **$X,XXX** |
| **Per person** | **$X,XXX** | **$X,XXX** |
| **Per day** | **$XX** | **$XX** |

**+ 15% contingency buffer** (always): $XXX
**Recommended total to bring**: $X,XXX

---

## 💡 Budget vs. Actual: Money Management Tips

```
**Before you go**:
- Notify your bank of travel dates
- Get a no-foreign-transaction-fee card (saves 2–3% on every purchase)
- Withdraw local cash at ATMs on arrival — airport exchange = terrible rates
- Note: credit cards offer better exchange rates than cash exchange bureaus

**Daily tracking**:
- Set a daily spend target ($XX/day)
- Track in a simple notes app or travel app (Trail Wallet, TravelSpend)
- If over one day, under-spend the next — not the whole trip

**Emergency fund**:
- Always keep $200–300 equivalent accessible but separate
- Store in different location from main wallet

**Best value hacks for [destination]**:
- [Destination-specific tip 1]
- [Destination-specific tip 2]
- [Destination-specific tip 3]
```

Always offer: "Want me to compare this budget against a similar destination?" or "Want a day-by-day spend plan based on the itinerary?"
