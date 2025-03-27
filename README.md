# EQPolly

**2025/03/26**  
With modern AI voice models available, there are now better ways to handle voiceovers in EverQuest. This repo is being kept online for nostalgia purposes only.

## Overview

EQPolly adds voiceovers to NPCs in EverQuest using Amazon's Polly TTS system.  
Check out `ExampleVideo.mp4` for a demo.

This Python script uses Amazon Polly (free tier) to parse EverQuest NPC interaction logs and play generated speech. Each NPC race and gender is assigned a Polly voice defined in `eqpollyvoices.csv`.

> **Disclaimer:**  
> This was a proof-of-concept and my first real experience with AWS. The code works but isn't optimized.

---

## Requirements

- Windows with Python 3.10  
- AWS account (free tier is sufficient)

Python packages:
- `pipwin` (used to install precompiled `pyaudio`)
- `pyaudio`
- `pygamer`
- `boto3`

---

## Setup

### 1. Install Dependencies

```bash
pip install boto3 pygamer pipwin
pipwin install pyaudio
```

### 2. AWS Setup

1. Create an AWS account and log in.
2. Go to **IAM**:
   - Create a user (e.g., `polly_user`)
   - Create a group (e.g., `polly_group`)
   - Assign the `AmazonPollyFullAccess` permission to the group
   - Add `polly_user` to the group
3. Under **polly_user → Security Credentials**, create an **Access Key**
4. Add credentials to `%USERPROFILE%\.aws\credentials`:

```
[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
```

---

### 3. EverQuest Logging

- Make sure logging is enabled in-game:

```
/log on
```

- Locate the log file:  
  `EverQuest\Logs\eqlog_<character>_<server>.txt`

---

### 4. Running the Script

```bash
python C:\EQPOLLY\eqpolly.py C:\EQPOLLY\eqpollyvoices.csv C:\GAMES\EVERQUEST\LOGS\eqlog_user_agnarr.txt
```

As NPCs speak in-game, the script will play a voiceover based on their race/gender.

---

## Customization

- To update or add new NPC voices, edit `eqpollyvoices.csv`.
- Over **14,800 NPCs** currently have predefined voices.

---

Enjoy the nostalgia!
