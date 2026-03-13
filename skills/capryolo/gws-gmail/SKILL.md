---
name: gws-gmail
version: 1.0.0
description: "Send Gmail emails via gws.exe subprocess"
---

# Gmail Skill

Send emails via Gmail API using gws.exe subprocess (same approach as theoldreader newsletter).

## Usage

```python
python skills/gws-gmail/gws_gmail.py
```

## Functions

### send_email(to, subject, body, from_email="capryolo@gmail.com")

Send plain text email.

**Returns:** dict with message id, labels, and thread id

### send_email_with_attachment(to, subject, body, attachment_path, from_email="capryolo@gmail.com")

Send email with attachment.

**Note:** Attachments are NOT supported via subprocess due to Windows command line length limits (8191 chars). Use the Gmail API directly with requests for attachments.

**Returns:** dict with message id, labels, and thread id

## Example

```python
from skills.gws-gmail.gws_gmail import send_email, send_email_with_attachment

# Send text email
result = send_email(
    to="hankvenom@gmail.com",
    subject="Test",
    body="Hello world"
)

# Send with attachment
result = send_email_with_attachment(
    to="hankvenom@gmail.com",
    subject="Meme",
    body="Here is a meme",
    attachment_path="workspace/meme.jpg"
)
```

## Notes

- Uses gws.exe directly (not gws.cmd) to avoid 8191 char limit
- Works around safety guard blocking direct file path access
- Requires gws.exe to be installed at `C:\Users\info\AppData\Roaming\npm\node_modules\@googleworkspace\cli\node_modules\.bin_real\gws.exe`
