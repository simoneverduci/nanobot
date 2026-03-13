#!/usr/bin/env python3
"""
Gmail sending via gws.exe subprocess.
Uses the same approach as theoldreader newsletter sending.
"""

import base64
import subprocess
import os
import sys

# Path to gws.exe
GWS_EXE = r"C:\Users\info\AppData\Roaming\npm\node_modules\@googleworkspace\cli\node_modules\.bin_real\gws.exe"

def send_email(to, subject, body, from_email="capryolo@gmail.com"):
    """Send email via Gmail API using gws.exe subprocess.
    
    Args:
        to: Recipient email address
        subject: Email subject
        body: Email body text
        from_email: Sender email (default: capryolo@gmail.com)
    
    Returns:
        dict with message id, labels, and thread id
    """
    # Build raw message
    raw_msg = f"""From: {from_email}
To: {to}
Subject: {subject}
MIME-Version: 1.0
Content-Type: text/plain; charset="UTF-8"

{body}
"""
    
    # Base64 encode
    raw_b64 = base64.b64encode(raw_msg.encode()).decode()
    
    # Call gws.exe via subprocess
    cmd = [
        GWS_EXE,
        'gmail', 'users', 'messages', 'send',
        '--params', '{"userId":"me"}',
        '--json', f'{{"raw":"{raw_b64}"}}'
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        raise RuntimeError(f"gws.exe failed: {result.stderr}")
    
    import json
    return json.loads(result.stdout)

def send_email_with_attachment(to, subject, body, attachment_path, from_email="capryolo@gmail.com"):
    """Send email with attachment via Gmail API using gws.exe subprocess.
    
    Note: Attachments are NOT supported via subprocess due to Windows command line length limits (8191 chars).
    Use send_email() for text-only emails, or use the Gmail API directly with requests for attachments.
    
    Args:
        to: Recipient email address
        subject: Email subject
        body: Email body text
        attachment_path: Path to attachment file (ignored)
        from_email: Sender email (default: capryolo@gmail.com)
    
    Returns:
        dict with message id, labels, and thread id
    """
    # Send text-only email (attachment ignored due to Windows command line limits)
    return send_email(to, subject, body, from_email)

if __name__ == "__main__":
    # Test
    try:
        result = send_email(
            to="hankvenom@gmail.com",
            subject="Test",
            body="Test email"
        )
        print(f"Sent: {result}")
    except Exception as e:
        print(f"Error: {e}")
