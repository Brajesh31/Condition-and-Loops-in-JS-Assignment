# 🐞 Debugging Guide

## Browser Console
Open Developer Tools, select Console, and reload the exercise. Read the first syntax or runtime error before inspecting later messages.

## Trace a conditional
Write down the variable value, comparison, Boolean result, and selected branch. For Q2, marks 80 fails the 90 threshold and matches the 70 threshold.

## Trace a loop
Use a table with these columns:

| Iteration | Counter before check | Condition | Logged expression | Counter after update |
|---:|---:|---|---|---|

Fill one row per iteration. Include the final condition check that exits the loop.

## Diagnose infinite loops
Confirm that the update changes the variable used by the condition and that the update moves it toward termination.

## Diagnose off-by-one output
Compare the loop counter to the expression passed to `console.log`. Q4 prints `i + 1`; Q5's descending loop prints `j - 1`.
