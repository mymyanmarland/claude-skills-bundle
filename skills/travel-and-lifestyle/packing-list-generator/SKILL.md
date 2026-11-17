---
name: packing-list-generator
description: Builds a complete, trip-specific packing list based on destination, duration, weather, activities, and traveler type. Use this skill whenever the user is packing for a trip or says things like "what should I pack for [destination]", "packing list for [trip type]", "help me pack for [weather/activity]", "what to bring to [place]", "I always forget something when I travel", or "packing for [X] days". Also trigger for specific trip types like beach holidays, skiing, business travel, backpacking, or camping. Always use this skill — a tailored packing list prevents both overpacking and forgetting essentials.
---

# Packing List Generator Skill

Build a smart, trip-specific packing list — nothing forgotten, nothing unnecessary.

## Step 1 — Gather Inputs

Ask in one message if not provided:
- **Destination**: City/country/region
- **Duration**: How many nights?
- **Weather/season**: Hot / Warm / Mild / Cold / Rainy / Mixed
- **Trip type**: Beach / City / Business / Adventure / Skiing / Backpacking / Camping / Cruise / Multi-destination
- **Activities planned**: (hiking, swimming, formal dinners, etc.)
- **Carry-on only or checked bag?**
- **Who's traveling**: Solo adult / Couple / Family with kids (ages) / Baby

---

## Step 2 — Generate the Packing List

```
## 🧳 Packing List: [Destination] — [X] Nights
**Weather**: [Type] | **Trip**: [Type] | **Bag**: [Carry-on / Checked]

---

### 👕 Clothing

**Formula for clothing** (carry-on rule: pack for 5 days max, re-wear or launder):
- Tops: [X] (1 per day minus 1–2 for re-wears)
- Bottoms: [X] (can re-wear 2–3 times)
- Underwear: 1 per day + 1 spare
- Socks: 1 per day + 1 spare

| Item | Qty | Notes |
|------|-----|-------|
| [T-shirts / shirts] | X | [Neutral colors = more outfit combos] |
| [Pants / shorts / skirts] | X | [One pair that can dress up/down] |
| [Underwear] | X | |
| [Socks] | X | [Merino wool = odor resistant, faster drying] |
| [Sleepwear] | 1 | |
| [Light jacket / cardigan] | 1 | [Layers for AC and cool evenings] |
| [Warm layer — fleece/sweater] | 1 | [Cold destination only] |
| [Rain jacket / packable] | 1 | [Rainy/mixed weather] |
| [Swimsuit] | [X] | [Beach/pool trips] |
| [Formal outfit] | 1 set | [Business/fancy dinners] |
| [Active wear] | [X sets] | [Hiking, gym, sport] |

**Shoes** (the heaviest items — minimize):
| Shoes | When |
|-------|------|
| [Walking/casual shoes] | Everyday — wear on plane |
| [Sandals/flip flops] | Beach, hostel showers |
| [Dress shoes] | Formal occasions only |
| [Hiking boots] | [Adventure trips only] |
| [Snow boots] | [Cold/winter destinations] |

**Accessories**:
- [ ] Belt
- [ ] Sunglasses
- [ ] Hat (sun or warm — depending on weather)
- [ ] Scarf (warmth + modesty cover in religious sites)
- [ ] Watch / jewelry (minimal — leave valuables at home)

---

### 🧴 Toiletries

*Carry-on rule: all liquids ≤ 100ml in one clear zip-lock bag*

| Item | Notes |
|------|-------|
| [ ] Toothbrush + toothpaste | Travel size |
| [ ] Deodorant | Solid stick = no liquid rules |
| [ ] Shampoo + conditioner | Most hotels provide — check first |
| [ ] Body wash / soap bar | Soap bar = no liquid restrictions |
| [ ] Face wash + moisturizer | Travel sizes |
| [ ] Sunscreen SPF 30+ | [Beach/outdoor trips — buy at destination if bulky] |
| [ ] Lip balm with SPF | |
| [ ] Razor | [Safety razor if carry-on only] |
| [ ] Feminine hygiene products | [Bring own — reliability varies by destination] |
| [ ] Nail clippers | [Checked bag only] |
| [ ] Hair ties / brush | |
| [ ] Perfume / cologne | [Small rollerball — ≤ 100ml] |

---

### 💊 Health & Medical

| Item | Notes |
|------|-------|
| [ ] Prescription medications | Bring more than needed + in carry-on |
| [ ] Pain reliever (ibuprofen / paracetamol) | |
| [ ] Antihistamine | Allergies + helps with sleep on overnight flights |
| [ ] Anti-diarrheal (loperamide) | [Especially important for developing countries] |
| [ ] Antacid | |
| [ ] Motion sickness tablets | [Boats, winding roads] |
| [ ] Rehydration sachets | [Hot climates, adventure travel] |
| [ ] Band-aids + antiseptic wipes | |
| [ ] Blister plasters | [New shoes + walking-heavy trips] |
| [ ] Insect repellent | [Tropical / rural destinations] |
| [ ] Malaria prophylaxis | [High-risk regions — consult doctor] |
| [ ] First aid kit | [Camping / remote destinations] |

---

### 📱 Tech & Electronics

| Item | Notes |
|------|-------|
| [ ] Phone + charger | |
| [ ] Universal power adapter | [Check destination outlet type] |
| [ ] Portable power bank | 10,000–20,000 mAh |
| [ ] Laptop / tablet | [Work or long trips] |
| [ ] Headphones / earbuds | Noise-cancelling = flights |
| [ ] E-reader | [Better than books for weight] |
| [ ] Camera + memory cards | [Optional — phone often sufficient] |
| [ ] Watch charger | [Smartwatch users] |
| [ ] Multi-port USB charger | Charge everything from one plug |
| [ ] Voltage converter | [Some destinations: 110V vs 220V] |

---

### 🎒 Bag & Travel Accessories

| Item | Notes |
|------|-------|
| [ ] Main bag (suitcase/backpack) | [Checked or carry-on] |
| [ ] Day bag / backpack | [For daily exploring] |
| [ ] Packing cubes | Game-changer for organization |
| [ ] Luggage lock | [TSA-approved if flying US] |
| [ ] Luggage tag with contact info | |
| [ ] Packable tote bag | Grocery shopping, beach, overflow |
| [ ] Dry bag | [Beach / water activities] |
| [ ] Money belt / hidden pouch | [High pickpocket risk destinations] |
| [ ] Neck pillow | [Long flights] |
| [ ] Sleep mask + earplugs | [Flights + hostel dorms] |
| [ ] Reusable water bottle | [Collapsible saves space] |

---

### 📄 Documents & Money

| Item | Notes |
|------|-------|
| [ ] Passport | Check expiry — 6 months validity needed for most countries |
| [ ] Visa / entry documents | Printed + digital copy |
| [ ] Travel insurance docs | Policy number + emergency contact |
| [ ] Flight/hotel confirmations | Printed + offline on phone |
| [ ] Driver's license | If renting a car |
| [ ] International driving permit | [Required in some countries] |
| [ ] Credit/debit cards (2+) | Notify bank before travel |
| [ ] Local currency cash | [Some destinations are cash-heavy] |
| [ ] Emergency cash (USD/EUR) | [Backup — widely accepted globally] |
| [ ] Copies of all documents | Store separately from originals |
| [ ] Vaccination certificate | [Required for some destinations] |
| [ ] Travel SIM or eSIM | |

---

### 🌊 Activity-Specific Add-Ons

**Beach trips**:
- [ ] Beach towel (quick-dry microfiber)
- [ ] Waterproof phone case
- [ ] Snorkel gear (if not renting)
- [ ] Water shoes
- [ ] After-sun lotion

**Hiking / Adventure**:
- [ ] Trekking poles
- [ ] Gaiters
- [ ] Headlamp + spare batteries
- [ ] Whistle + compass
- [ ] High-energy snacks
- [ ] Blister kit

**Cold / Ski trips**:
- [ ] Thermal base layers (top + bottom)
- [ ] Ski gloves / mittens
- [ ] Wool or fleece hat
- [ ] Hand warmers
- [ ] Ski socks (tall, padded)
- [ ] Goggles (if not renting)

**Business travel**:
- [ ] Iron / wrinkle spray (or choose wrinkle-resistant fabrics)
- [ ] Business cards
- [ ] Presentation clicker
- [ ] Extra formal shirt/blouse
- [ ] Shoe bags

**Family with young kids**:
- [ ] Snacks (airport + flight)
- [ ] Compact stroller or carrier
- [ ] Car seat (if renting a car)
- [ ] Kids' entertainment (tablet, headphones, activities)
- [ ] Extra change of clothes for kids (×2)
- [ ] Wet wipes (double the amount you think)
- [ ] Kids' medications
- [ ] Night light (portable)
```

---

## Step 3 — Packing Strategy Tips

```
## 💡 Packing Tips

**Weight & space**:
- Roll clothes instead of folding — saves 30% space + reduces wrinkles
- Wear your heaviest items on travel day (boots, jacket)
- Stuff socks inside shoes
- Pack heaviest items closest to wheels / your back

**Carry-on strategy**:
- Valuables, medications, documents, change of clothes ALWAYS in carry-on
- Assume checked bag may be delayed — pack 1 day's essentials in carry-on

**The "maybe" pile test**:
If you haven't worn it at home in the last month, you won't wear it traveling.
If it only goes with one outfit, leave it.

**Leave room for**:
Souvenirs — pack one collapsible bag or leave 20% of bag empty going outward.
```

Always offer: "Want me to estimate the total weight of this packing list?" or "Want a condensed version for carry-on only?"
