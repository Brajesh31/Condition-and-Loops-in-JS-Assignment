# 🧠 JavaScript Conditions and Loops

## Boolean conditions
Comparison expressions such as greater-than, less-than, and equality evaluate to Boolean values. A conditional statement uses the result to decide which block executes.

## if and else
```js
if (condition) {
  // Runs when condition is truthy.
} else {
  // Runs when condition is falsy.
}
```

## else if chains
Branches are tested from top to bottom. The first true condition is selected. When ranges overlap, order thresholds carefully.

## switch
A switch compares an expression with case labels. Use break when execution should leave the switch after a match. A default branch handles unmatched values.

## for loop
```js
for (let counter = 0; counter < 5; counter++) {
  console.log(counter);
}
```
Initialization runs once, the condition is checked before each iteration, and the update runs after the body.

## while loop
A while loop checks its condition before running the body. It may execute zero times. Ensure the body or another control path updates state so the condition can eventually become false.

## do...while loop
A do...while loop executes its body before checking the condition, so it always executes at least once.

## break and continue
break exits the nearest loop or switch. continue skips the remainder of the current iteration and proceeds to the next condition check.

## Boundary tracing
For every loop, record:
1. Initial counter value.
2. Condition result.
3. Value logged.
4. Update.
5. Final failed condition.

The displayed value can differ from the counter, as Q4 and Q5 demonstrate.

## Complexity intuition
A simple loop over n values with constant work per iteration is O(n). Nested loops may be O(n²). These exercises use small fixed ranges and are not performance benchmarks.
