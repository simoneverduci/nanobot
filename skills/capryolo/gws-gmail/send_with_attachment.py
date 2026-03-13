#!/usr/bin/env python3
"""
Send email with attachment using Gmail API directly.
Uses the credentials from workspace/gws/credentials.enc
"""

import base64
import requests
import os
import json

def get_credentials():
    """Read and decrypt credentials."""
    cred_path = r"C:\Users\info\.nanobot\workspace\gws\credentials.enc"
    key_path = r"C:\Users\info\.nanobot\workspace\gws\.encryption_key"
    
    if not os.path.exists(cred_path) or not os.path.exists(key_path):
        return None
    
    with open(key_path, 'rb') as f:
        key = f.read()
    
    with open(cred_path, 'rb') as f:
        cred_data = f.read()
    
    # Simple XOR decryption (gws uses XOR with key)
    decrypted = bytes([cred_data[i] ^ key[i % len(key)] for i in range(len(cred_data))])
    
    try:
        return json.loads(decrypted.decode('utf-8'))
    except:
        return None

def send_email_with_attachment(to, subject, body, attachment_path, from_email="capryolo@gmail.com"):
    """Send email with attachment via Gmail API."""
    # Read attachment
    with open(attachment_path, 'rb') as f:
        attachment_data = base64.b64encode(f.read()).decode()
    
    # Build raw message with attachment
    raw_msg = f"""From: {from_email}
To: {to}
Subject: {subject}
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="BOUNDARY"

--BOUNDARY
Content-Type: text/plain; charset="UTF-8"

{body}

--BOUNDARY
Content-Type: image/jpeg
Content-Transfer-Encoding: base64
Content-Disposition: attachment; filename="meme.jpg"

{attachment_data}
--BOUNDARY--
"""
    
    # Base64 encode for Gmail API
    raw_b64 = base64.b64encode(raw_msg.encode()).decode()
    
    # Get credentials
    creds = get_credentials()
    if not creds or 'access_token' not in creds:
        raise ValueError("No valid credentials found")
    
    # Send via Gmail API
    headers = {
        'Authorization': f'Bearer {creds["access_token"]}',
        'Content-Type': 'application/json'
    }
    
    response = requests.post(
        'https://www.googleapis.com/gmail/v1/users/me/messages/send',
        headers=headers,
        json={'raw': raw_b64}
    )
    
    if response.status_code != 200:
        raise RuntimeError(f"Gmail API error: {response.json()}")
    
    return response.json()

if __name__ == "__main__":
    try:
        result = send_email_with_attachment(
            to="hankvenom@gmail.com",
            subject="Meme from Reddit",
            body="Here is a meme I found on Reddit.",
            attachment_path="meme.jpg"
        )
        print(f"Sent: {result}")
    except Exception as e:
        print(f"Error: {e}")
