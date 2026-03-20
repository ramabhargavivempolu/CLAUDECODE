---
name: DRY Principle Violations in Data Visualization
description: Repeated visualization code blocks that should be extracted into reusable functions
type: feedback
---

When reviewing data visualization code, look for repeated plotting patterns that violate the DRY (Don't Repeat Yourself) principle.

**Why:** Repeating near-identical code blocks (differing only in variable names and colors) makes maintenance difficult and increases bug surface area. If a bug is fixed in one block, it must be fixed in all copies. Configuration changes require editing multiple locations.

**How to apply:**
- Identify patterns that appear 3+ times with only minor variations
- Recommend extracting into parameterized functions that accept the varying parts as arguments
- Look for repetitive blocks like:
  - Multiple visualization blocks with same structure
  - Repeated merge operations with similar column names
  - Identical groupby-aggregate-sort patterns

**Example in data visualization:**
```python
# PATTERN: This block repeats 8 times with different groupby columns and colors
sales_by_X = sales_data.groupby("column_name")["net_amount"].sum().sort_values(ascending=False)
plt.figure(figsize=(12, 6))
sales_by_X.plot(kind="bar", color="#color")
plt.title("Title", fontsize=14, fontweight="bold")
plt.xlabel("Label")
plt.ylabel("Amount ($)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "filename.png", dpi=300, bbox_inches="tight")
plt.close()

# REFACTORED: Single parameterized function
def create_bar_chart(data, group_col, value_col, title, filename, color, top_n=None):
    agg_data = data.groupby(group_col)[value_col].sum().sort_values(ascending=False)
    if top_n:
        agg_data = agg_data.head(top_n)
    # ... single plotting implementation
```

