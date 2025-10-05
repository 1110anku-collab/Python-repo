📘 Smart File Organizer — User Guide
🧩 Version

Smart File Organizer v1.0.0

🧑‍💻 Developed by

Ankita Kamble

🏠 Table of Contents

Introduction

System Requirements

Installation Guide

Launching the Application

Login Screen

Main Interface Overview

Feature-by-Feature Instructions

1. Organize Files

2. Undo Changes

3. Backup Manager

4. Junk File Detection

5. Harmful File Scan

6. Email Alerts

Notifications

Supported File Types

Backup Folder Information

Troubleshooting

Frequently Asked Questions (FAQ)

Safety and Privacy Notes

Credits & License

🧠 Introduction

The Smart File Organizer is a desktop application that helps you automatically manage, categorize, and back up files with just one click.

It’s designed to:

Keep your folders neat and organized.

Detect unnecessary (junk) files.

Provide undo and backup options for safety.

Send email alerts and system notifications for updates.

You don’t need any technical knowledge — the interface is simple, modern, and intuitive.

💻 System Requirements
Component	Minimum Requirement
Operating System	Windows 10 / 11, macOS, or Linux
Python Version	Python 3.8 or later
RAM	4 GB or higher
Storage	At least 100 MB free space
Libraries	Tkinter, shutil, plyer, Pillow, smtplib
⚙️ Installation Guide
Step 1: Download the Project

Download or clone the folder from your source:

git clone https://github.com/yourusername/smart-file-organizer.git


Or manually download the .zip and extract it.

Step 2: Install Required Libraries

Open Command Prompt (Windows) or Terminal (Mac/Linux) and type:

pip install pillow plyer

Step 3: Run the Application

Use this command:

python smart_file_organizer.py

🚪 Launching the Application

After running the command, a login screen will appear.

🔐 Login Screen

Purpose: To secure access to the organizer.

Default Credentials

Username: admin

Password: 1234

💡 You can change these credentials in the code under the variable USERS.

If login is successful → The main organizer window opens.
If credentials are wrong → You’ll see a “Login Failed” message.

🖥 Main Interface Overview

Once logged in, you’ll see two main areas:

🔸 Left Sidebar

Contains all action buttons:

📑 Organize Files

↩️ Undo

💾 Backup

🧹 Detect Junk

⚠️ Scan Malware

✉️ Send Email

🔸 Right Main Panel (Centered)

Contains:

Source Folder (bold text) — Folder where your unorganized files are.

Destination Folder (bold text) — Folder where organized files will be stored.

Status Bar — Displays live status messages (e.g., “Status: Ready” or “Organizing Complete”).

🧩 Feature-by-Feature Instructions
1️⃣ Organize Files

Purpose: Automatically sorts all files from the source folder into categorized subfolders in the destination folder.

Steps:

Click Browse beside “Source Folder” and select your input folder.

Click Browse beside “Destination Folder” and choose where organized files should go.

Click 📑 Organize Files.

Wait a few seconds — progress will be shown in the status line.

A popup will ask:

Do you want to create a backup of organized files? (Yes/No)


Yes → Creates a ZIP backup.

No → Skips backup.

Result:

Your destination folder now contains subfolders like:

Images/
Documents/
Videos/
Audio/
Archives/
Others/

2️⃣ Undo Changes

Purpose: Restores files that were recently moved back to their original location.

Steps:

Click ↩️ Undo.

Wait until the status bar shows Undo Completed.

Tip:

Undo works only for the last organization action done in the same session.

3️⃣ Backup Manager

Purpose: Creates a compressed ZIP file of all organized files.

Steps:

Click 💾 Backup.

Choose where to save your backup (destination path).

A .zip file will be created automatically.

Result:

A folder named /backups/ appears in your project directory.

4️⃣ Junk File Detection

Purpose: Detects and lists temporary or unnecessary files.

Detects:

.tmp

.log

.bak

Steps:

Click 🧹 Detect Junk.

A popup shows a list of junk files.

You can manually delete them after review.

5️⃣ Harmful File Scan

Purpose: Flags potentially harmful files (executables or scripts) for manual review.

Detects:

.exe, .bat, .cmd, .sh, .jar, .vbs, .js

Steps:

Click ⚠️ Scan Malware.

The system will display suspicious files.

You can review and delete them manually.

⚠️ Note: This is not a virus scanner; it only identifies potentially risky file types.

6️⃣ Email Alerts

Purpose: Send email notifications for backup or organization updates.

Requirements:

Enable 2-Step Verification in Gmail.

Generate an App Password.

Update credentials in the script:

from_email = "your_email@gmail.com"
password = "your_app_password"

Steps:

Click ✉️ Send Email.

A message box confirms if the mail was sent successfully.

🔔 Notifications

Smart File Organizer uses desktop notifications to keep you informed of:

Task completion (organization, undo, backup).

Errors or missing folders.

Email success/failure.

Example:

✅ Files organized successfully!

📂 Supported File Types

The application supports over 100+ file extensions, grouped into categories:

Images (jpg, png, gif, heic, etc.)

Documents (pdf, txt, docx, md, etc.)

Audio / Video

Archives

Spreadsheets

Executables

Design Files

Fonts

Others (Unrecognized)

All extensions are listed in the FILE_TYPES dictionary inside the code.

💾 Backup Folder Information
Backup Location	Format	Description
/backups/	.zip	Compressed copy of organized files
Default Name	backup_YYYYMMDD_HHMM.zip	Timestamped for uniqueness
🧹 Junk and Harmful File Indicators
Icon	Meaning
🧹	Temporary or log files detected
⚠️	Suspicious executable files found
🧰 Troubleshooting
Problem	Possible Cause	Solution
App not starting	Missing libraries	Run pip install pillow plyer
Login fails	Wrong username/password	Use default: admin / 1234
Notifications not showing	System notifications off	Enable system notifications
Email not sent	Invalid Gmail setup	Use App Password, not your real password
Undo not working	Restarted program	Undo works only within same session
❓ FAQ

Q1: Can I organize files from multiple folders at once?
A: Currently, you can organize one folder at a time.

Q2: Can I change folder categories or add new ones?
A: Yes, you can edit the FILE_TYPES dictionary in the code.

Q3: Does this delete files?
A: No. It only moves or copies them.

Q4: Can I change the theme?
A: Yes, you can modify the background color (#1e1e2f) in the GUI section.

🔒 Safety and Privacy Notes

Your login credentials are stored locally (not online).

The program does not upload or share any user data.

Always scan unknown files with antivirus software before opening them.

Email credentials should be protected and not shared.

👩‍💻 Credits & License

Author: Ankita Kamble
Language: Python 3.10+
Libraries Used: Tkinter, shutil, plyer, pillow, smtplib
License: MIT
Category: Desktop Utility Tool
Platform: Windows / macOS / Linux

🪄 Summary

The Smart File Organizer is a powerful and secure desktop tool to keep your system neat and efficient.
It provides a clean, centered interface, automatic backups, and full control over your file management workflow.

Smart. Organized. Secure. Simplify your digital life.