---
name: excel-recipe-meal-planning
description: Teaches using Excel for recipe management and meal planning. Use when the user says things like 'recipe spreadsheet Excel', 'meal planning Excel', 'nutrition tracker Excel'.
---

# Recipe and Meal Planning Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level
- Specific task
- Data type
- Intended output

## Step 2 — Core Output

Recipe and meal planning: Recipe database (recipe name / servings / prep time / cook time / calories / source) → Ingredients list (recipe / ingredient / quantity / unit) → Shopping list (SUMIF: sum the quantity of each ingredient across selected recipes for the week) → Meal planner (7-day grid / dropdown of recipe names / pulls nutrition data via XLOOKUP) → Nutrition summary (SUMIF of calories/protein/fat/carbs for the day) → Scaling (=original_quantity × (desired_servings/original_servings)) → Ingredient inventory (what is in the cupboard vs what is needed — subtract to get the shopping list).

## Step 3 — Quality & Polish

- SUMIF for shopping list: adds up quantities of the same ingredient across multiple recipes
- XLOOKUP to pull recipe data into the meal planner: type the recipe name and all data populates
- Scaling formula: =qty*(desired/original) — scales every ingredient proportionally

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features may vary between versions. Always test formulas on sample data and back up your data before running bulk operations.
