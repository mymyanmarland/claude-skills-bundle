---
name: trip-itinerary-builder
description: Creates a detailed, day-by-day travel itinerary for any destination with timing, transport, food recommendations, and insider tips. Use this skill whenever the user is planning a trip or says things like "plan my trip to [destination]", "itinerary for [city/country]", "what should I do in [place]", "help me plan my vacation", "3 days in [city]", "travel plan for [destination]", or "things to do in [place]". Also trigger for honeymoons, family trips, solo travel, and multi-city routes. Always use this skill — a well-structured itinerary maximizes time and prevents the paralysis of too many options once you're actually there.
---

# Trip Itinerary Builder Skill

Build a practical, immersive, day-by-day travel plan that fits the traveler's style.

## Step 1 — Gather Inputs

Ask in one message if not provided:
- **Destination(s)**: City, country, or region
- **Duration**: How many days/nights?
- **Travel style**: Relaxed / Balanced / Packed / Adventure / Cultural / Foodie / Family / Romantic
- **Budget level**: Budget / Mid-range / Luxury
- **Who's traveling**: Solo / Couple / Family with kids (ages) / Group
- **Interests**: History, food, nightlife, nature, art, shopping, off-the-beaten-path
- **Any must-sees or must-avoids**: Specific attractions or experiences
- **Mobility considerations**: (affects walking-heavy days)

---

## Step 2 — Pre-Trip Essentials

```
## ✈️ [Destination] Travel Essentials

**Best time to visit**: [Month range + why — weather, crowds, festivals]
**Current season during your trip**: [Season + what to expect]
**Currency**: [Currency name + approximate exchange rate]
**Language**: [Primary language + key phrases]
**Time zone**: [GMT±X]
**Visa required**: [Yes/No/On arrival — check official source for your passport]
**Power outlets**: [Type + voltage — adapter needed?]
**Emergency numbers**: Police [X] | Ambulance [X] | Tourist helpline [X]
**Getting from airport**: [Best options + approximate cost + time]
```

---

## Step 3 — Day-by-Day Itinerary

```
## 🗓️ [X]-Day [Destination] Itinerary
**Travel style**: [Style] | **Budget**: [Level] | **Party**: [Who]

---

### 📅 Day 1 — [Theme, e.g., "Arrival & Old City Exploration"]

**Morning**
| Time | Activity | Notes |
|------|----------|-------|
| 09:00 | [Activity/Attraction] | [Tip — book tickets in advance / best entrance / what to look for] |
| 10:30 | [Activity] | [Practical note] |

**☕ Breakfast/Coffee**: [Specific café recommendation + what to order]

**Afternoon**
| Time | Activity | Notes |
|------|----------|-------|
| 13:00 | [Lunch spot] | [Dish to try + why this place] |
| 14:30 | [Attraction] | [Insider tip] |
| 16:00 | [Activity] | [Timing note — e.g., golden hour here is stunning] |

**Evening**
| Time | Activity | Notes |
|------|----------|-------|
| 18:30 | [Neighborhood stroll / sunset spot] | [Why this timing] |
| 20:00 | [Dinner restaurant] | [Cuisine, price range, reservation needed?] |
| 21:30 | [Optional evening activity] | [Nightcap, show, rooftop, etc.] |

**🚌 Transport today**: [How to get between these spots — walk / metro / taxi]
**💰 Estimated spend today**: $XX–XX (excl. accommodation)
**💡 Local tip**: [One piece of insider knowledge for this day]

---

### 📅 Day 2 — [Theme]

[Same structure]

---

### 📅 Day [X] — [Final Day Theme, e.g., "Hidden Gems & Departure"]

[Same structure — note departure logistics if flying out]

---
```

---

## Step 4 — Neighborhood Guide

```
## 🗺️ Neighborhood Breakdown

| Neighborhood | Vibe | Best For | Don't Miss |
|-------------|------|----------|------------|
| [Area 1] | [Atmosphere] | [Type of traveler] | [Specific spot] |
| [Area 2] | | | |
| [Area 3] | | | |

**Where to stay** (by budget):
- 💰 Budget: [Area + 1–2 hotel/hostel recommendations]
- 💰💰 Mid-range: [Area + recommendations]
- 💰💰💰 Luxury: [Area + recommendations]
```

---

## Step 5 — Food & Drink Guide

```
## 🍽️ Essential Food Experiences

**Must-try dishes**:
1. [Dish name] — [What it is + where to try it]
2. [Dish name] — [Description + recommendation]
3. [Dish name] — [Description + recommendation]

**Restaurant picks by meal**:
| Meal | Restaurant | Type | Price | Must-Order |
|------|-----------|------|-------|------------|
| Breakfast | [Name] | [Cuisine] | $X/person | [Dish] |
| Lunch | [Name] | [Cuisine] | $XX/person | [Dish] |
| Dinner (special) | [Name] | [Cuisine] | $XX/person | [Dish] |
| Street food | [Market/stall] | [Type] | $X | [Item] |

**Drinks to try**: [Local beer, wine, coffee culture, street drink]
**Dietary note**: [Vegetarian/vegan/halal/kosher options — how easy is the destination?]
```

---

## Step 6 — Practical Tips

```
## 💡 [Destination] Practical Tips

**Getting around**:
- Best app: [Local ride-hailing / metro app]
- Metro/bus: [Cost + how to buy tickets]
- Taxi: [Approximate fare for common routes + avoid tourist traps]
- Walking: [How walkable is it? Best areas to walk]

**Money**:
- Cash vs. card: [Which is more accepted]
- ATM tips: [Use bank ATMs, avoid airport rates, etc.]
- Tipping culture: [Expected? Amount? Situations]

**Safety**:
- [Specific neighborhoods to be cautious in, if any]
- [Common tourist scams in this destination]
- [General safety level for solo travelers / women travelers]

**Connectivity**:
- SIM card: [Where to buy + best local carrier + approximate cost]
- eSIM options: [Airalo or local digital options]
- Free WiFi: [Common or uncommon? Best places]

**Booking tips**:
- [What needs advance booking — popular sites sell out weeks ahead]
- [What's better done spontaneously]
- [Best booking platforms for this destination]
```

---

## Step 7 — Day Trip Options

```
## 🚌 Day Trips from [City] (if time allows)

| Destination | Distance | How to Get There | Best For | Time Needed |
|-------------|---------|-----------------|----------|-------------|
| [Place 1] | X km | [Transport + time + cost] | [Why go] | Half day / Full day |
| [Place 2] | X km | [Transport] | [Why go] | Full day |
```

Always offer: "Want me to build a packing list for this trip?" or "Want a budget breakdown for the full itinerary?"
