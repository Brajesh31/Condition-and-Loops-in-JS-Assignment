# ⚡ Performance Considerations

The current exercises use small, fixed loop ranges and constant-time console operations. They are instructional examples, not performance benchmarks.

## Complexity
A single loop over n items with constant work per iteration is generally O(n). Nested loops over n-sized ranges may be O(n²). The current fixed examples are too small to support meaningful performance claims.

## Practical guidance
- Keep teaching loops bounded.
- Avoid unnecessary DOM updates inside large loops.
- Do not use console logging as a benchmark.
- If examples are expanded to large ranges, explain the cost and browser responsiveness implications.

No benchmark or performance test has been run for this repository.
