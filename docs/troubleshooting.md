# 🧰 Troubleshooting

## No output appears
The examples primarily use `console.log`. Open Developer Tools → Console and reload the page.

## An image is missing
Open the page in its original assignment directory. The images are referenced using relative paths under `asset/`. Moving a page requires updating its references.

## A syntax error appears
Use the file and line number reported in Console. Check quotes, braces, parentheses, and comparison operators near that line.

## A loop never stops
Check whether the loop body updates the same variable used by the condition. Confirm the update can make the condition false.

## A final number looks unexpected
Trace the counter and printed expression separately. Q4 adds one to the counter. Q5 subtracts one in the descending output.

## The validator cannot run
Confirm Python 3 is installed and run the command from the repository root:
```bash
python scripts/validate-exercises.py
```

## Static server port is occupied
Choose another port, for example `python -m http.server 8081`, then open port 8081 in the browser.
