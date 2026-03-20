# Code Reviewer Memory Index

## Feedback & Patterns

- **[feedback_visualization_patterns.md](feedback_visualization_patterns.md)** - Flag module-level code execution in scripts as critical reusability/testability issue. Always recommend wrapping in `main()` with `if __name__ == "__main__":` guard.

- **[pattern_code_duplication.md](pattern_code_duplication.md)** - DRY principle violations in data visualization: flag repeating plot/groupby/save blocks (3+ occurrences) and recommend extracting to parameterized functions.

