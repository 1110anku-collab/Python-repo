Overview

Features

GUI details

Setup & installation

Step-by-step usage

Email alert setup

Folder structure

Troubleshooting

Screenshots (placeholders)

Credits & license


# 🧠 Smart File Organizer

A complete **Python-based Smart File Organizer** with a secure login system, intuitive GUI, and intelligent file management capabilities.  
It automatically organizes files by type, provides undo and backup options, detects junk files, sends desktop notifications, and even allows sending email alerts.

---

## 🌟 Overview

This Smart File Organizer is built with **Tkinter (GUI)** and **Python’s standard libraries**, making it lightweight, fast, and easy to run on any system.  
It helps users manage cluttered folders by categorizing files into dedicated directories such as *Images, Documents, Audio, Videos, Archives,* and more.  

The program is designed for everyday users, office workers, and developers who want a **single-click file organization system** with smart automation and backup features.

---

## ✨ Features

### 🧩 Core Features
| Feature | Description |
|----------|-------------|
| 🔐 **Login System** | Secure access with username and password validation. |
| 📁 **File Organizer** | Automatically classifies files by type into pre-defined categories. |
| ↩️ **Undo Option** | Restores recently organized files back to their original location. |
| 💾 **Backup Manager** | Creates ZIP archives of source folders for quick recovery. |
| 🧹 **Junk File Detection** | Finds and lists unwanted files like `.tmp`, `.log`, and `.bak`. |
| 🔔 **Desktop Notifications** | Real-time system notifications after major actions. |
| ✉️ **Email Alerts** | Send email alerts (e.g., backup confirmations or alerts). |
| 💻 **Dark Modern GUI** | Clean, centered, and easy-to-use interface built with Tkinter. |

---

## 🪶 GUI Design

- Built using **Tkinter** and styled for a modern dark theme (`#1e1e2f` background).  
- **Left Sidebar**: Quick-access buttons for all operations.  
- **Main Panel (Center Aligned)**:
  - **Source Folder** and **Destination Folder** inputs (bold labels).  
  - Browse buttons for folder selection.  
  - Status bar showing live operation status.  

🖼 **Layout Example:**

| 📂 Smart Organizer | Source Folder |
| [Organize Files] | [Browse] |
| [Undo] | Destination |
| [Backup] | [Browse] |
| [Detect Junk] | Status: Ready |
| [Send Email] | |


---

## 🧰 Supported File Categories

The app automatically sorts your files into these categories:

| Category | Example Extensions |
|-----------|--------------------|
| **Images** | jpg, png, gif, bmp, tiff, svg, webp, heic |
| **Documents** | pdf, doc, docx, txt, rtf, odt, tex, md, log |
| **Videos** | mp4, mkv, avi, mov, flv, webm, 3gp |
| **Audio** | mp3, wav, flac, wma, aac, ogg, m4a |
| **Archives** | zip, rar, 7z, tar, gz, iso |
| **Spreadsheets** | xlsx, xls, csv, ods, tsv |
| **Presentations** | ppt, pptx, key, odp |
| **Executables** | exe, msi, bat, cmd, sh, apk, py, jar |
| **Databases** | db, sqlite, sql, mdb, accdb |
| **Design & 3D** | psd, ai, fig, blend, obj, stl |
| **Code Files** | py, java, cpp, c, cs, html, css, js, xml, json, php |
| **Fonts** | ttf, otf, woff, woff2 |
| **Icons** | ico, icns, cur, ani, svg |
| **Others** | Files that don’t match any known extension. |

---

## ⚙️ Installation

### 🧩 1. Clone or Download
Download this repository or copy the script file:
```bash
git clone https://github.com/yourusername/smart-file-organizer.git
cd smart-file-organizer

Or just save the Python file:
smart_file_organizer.py




2. Install Dependencies

Install required packages:
pip install pillow plyer

These libraries handle:

Pillow → image and icon support.

Plyer → desktop notifications.


3. Run the Application

python smart_file_organizer.py

Login Credentials
Username	Password
admin	1234

You can modify these credentials in the code:

USERS = {"admin": "1234"}

🚀 How to Use

Run the program.

Enter login credentials (default: admin / 1234).

In the main interface:

Select a Source Folder (where files currently are).

Select a Destination Folder (where you want organized folders created).

Click “📑 Organize Files”.

The app automatically creates subfolders for each file type.

When prompted, choose Yes/No for creating a backup.

Optional:

Click Undo to revert changes.

Click Detect Junk to find unnecessary files.

Click Send Email to trigger an alert email.

💾 Backup System

After organization, you can create a backup ZIP file of your destination folder.
Backups are stored by default in a /backups/ directory, which is automatically created if it doesn’t exist.

✉️ Email Alert Setup (Optional)

To enable email alerts:

Enable 2-Step Verification in your Google Account.

Generate an App Password under “Security → App Passwords”.

Replace your email and app password in the code:

from_email = "your_email@gmail.com"
password = "your_app_password"


Update the recipient email:

send_email_alert("recipient@example.com", "Smart Organizer", "Your files were organized successfully!")

🧹 Junk File Detection

Automatically detects:

Temporary files (.tmp)

Log files (.log)

Backup files (.bak)

You’ll receive a popup alert listing all detected junk files.

🖥 Desktop Notifications

Desktop notifications appear in the system tray area when:

Files are organized

Backups are created

Undo actions succeed

Email alerts are sent

These are powered by the plyer module.

📁 Folder Structure
SmartFileOrganizer/
│
├── smart_file_organizer.py    # Main Application Code
├── README.md                  # Project Documentation
├── /backups/                  # (Generated automatically)
│     └── backup.zip
├── /organized_files/          # Destination Folder (User Defined)
└── /icons/                    # (Optional - for future icon support)

🔧 Troubleshooting
Issue	Possible Fix
Email failed	Check Gmail App Password and enable “Allow less secure apps” if necessary.
Notification not showing	Ensure plyer is installed and notifications are enabled on your system.
Permission denied	Run the program as Administrator.
Files not organizing	Verify source and destination folders are correctly selected.


(Add actual screenshots in a screenshots/ folder for GitHub or reports.)

🧑‍💻 Developer Information

Author: Ankita Kamble
Language: Python 3.10+
Libraries Used: Tkinter, shutil, plyer, pillow, smtplib
License: MIT
Project Type: Desktop Application (GUI)
Platform: Windows / macOS / Linux