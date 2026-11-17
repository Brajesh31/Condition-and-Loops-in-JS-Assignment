# ⚠️ Error Handling

The current examples use fixed values and simple console output. They do not define a shared error-handling layer or process untrusted user input.

## Current failure modes
- A syntax error can prevent a page's inline script from executing.
- A broken relative image path can prevent an instructional image from loading.
- An incorrect loop update can cause unexpected output or a non-terminating loop.
- A mistaken comparison boundary can select the wrong branch or omit a displayed value.

## Debugging process
1. Read the browser Console error and source line.
2. Check nearby brackets, parentheses, quotes, and comparison operators.
3. Trace variable values at each condition.
4. Verify that the loop update changes the state used by its condition.
5. Re-run the page and compare observed output with expected behavior.

Future exercises that accept user input should validate it explicitly and explain invalid cases.
