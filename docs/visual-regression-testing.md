# 🖼️ Visual Regression Testing

There is no browser screenshot automation or visual regression service in the current repository.

## Manual visual review
- Open the changed HTML page in a current browser.
- Compare layout and image placement with the previous version where relevant.
- Verify the page remains usable at narrow viewport widths and 200% zoom.
- Capture screenshots only from the real current page.

## Future automation
If screenshot testing is introduced, define browser version, viewport size, font environment, baseline update process, and review of expected diffs. Do not store synthetic screenshots as if they were actual app output.
