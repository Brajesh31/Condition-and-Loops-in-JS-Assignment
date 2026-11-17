# 🤝 Contributing Guide

Thank you for improving these JavaScript control-flow exercises. Contributions should make the assignment more accurate, easier to understand, more accessible, or easier to maintain.

## 🎯 Suitable contributions
- Correct mistakes in explanations or examples.
- Add beginner-friendly exercises for conditions and loops.
- Explain expected output and boundary conditions.
- Improve semantic HTML and image alternatives.
- Add real, reproducible validation.
- Improve diagrams, troubleshooting, and accessibility guidance.

## 🧰 Local setup
```bash
git clone https://github.com/Brajesh31/Condition-and-Loops-in-JS-Assignment.git
cd Condition-and-Loops-in-JS-Assignment
python scripts/validate-exercises.py
```
Open any `Q1.html` through `Q5.html` in a modern browser. Open Developer Tools → Console to see the existing output. Python 3 is only needed for repository validation or the optional static server.

## 🌿 Branching and commits
Use focused branches such as `docs/q2-explanation`, `fix/loop-boundary`, or `test/asset-validation`. Suggested commit prefixes:
- `docs:` documentation-only changes
- `fix:` corrections to incorrect behavior
- `test:` validation and test improvements
- `feat:` new learning examples
- `chore:` repository maintenance

## 🧑‍💻 Coding standards
- Prefer descriptive variable names in new examples.
- Use consistent indentation and readable blocks.
- Prefer strict equality when equality is intended.
- Make loop termination conditions obvious.
- Avoid unnecessary abstractions in beginner examples.
- Comment why a non-obvious decision is made, not every line.
- Do not add dependencies for tasks that plain HTML and JavaScript can handle.

## 🧪 Verification
- Run `python scripts/validate-exercises.py`.
- Open every changed HTML page in a browser.
- Check the Console for syntax errors and expected output.
- Verify relative images still load.
- Test boundary values when changing conditions or loops.
- Do not claim tests passed unless they were actually run.

## 📚 Documentation requirements
When an exercise changes, update the README assignment map and the relevant page in `docs/`. Use Mermaid for useful control-flow explanations. Keep screenshots genuine and current. Clearly label proposals and known limitations.

## 🔀 Pull request process
1. Explain the learning problem and proposed change.
2. List affected exercises and files.
3. Describe test commands and manual browser checks.
4. Include actual screenshots for visual changes.
5. Link related issues.
6. Respond to review feedback and keep the change focused.

## 🔐 Security
Never commit credentials, personal data, malicious scripts, or generated files unrelated to the assignment. Report vulnerabilities privately using [SECURITY.md](SECURITY.md).
