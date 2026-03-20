---
name: Avoid Script-Level Code Execution
description: Module-level code execution prevents reusability and testability of visualization scripts
type: feedback
---

When reviewing data processing and visualization scripts, flag module-level code execution as a critical issue.

**Why:** Scripts that run logic at import time (outside of `if __name__ == "__main__":`) cannot be imported by other modules without triggering side effects. This makes testing impossible and prevents code reuse. It violates the fundamental Python principle of separating concerns between module functionality and script execution.

**How to apply:**
- When you see pandas operations, matplotlib calls, or data processing at the module level, recommend wrapping all logic in a `main()` function
- Suggest using `if __name__ == "__main__":` guard to separate script execution from importable functions
- Flag hard-coded paths at module level as preventing dynamic configuration
- Recommend accepting paths as command-line arguments or configuration

**Example patterns to watch for:**
```python
# BAD: Runs immediately on import
df = pd.read_parquet("fixed/path/data.parquet")
result = df.groupby(...).sum()
plt.savefig("chart.png")

# GOOD: Can be imported and tested
def main(data_path: Path, output_path: Path):
    df = pd.read_parquet(data_path)
    # ...

if __name__ == "__main__":
    main()
```

