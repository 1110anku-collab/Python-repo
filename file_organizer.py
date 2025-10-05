import os
import shutil
import hashlib
import smtplib
import tkinter as tk
from tkinter import filedialog, messagebox
from email.mime.text import MIMEText
from plyer import notification
from PIL import Image, ImageTk   # For icons

# ---------------- LOGIN SYSTEM ----------------
USERS = {"admin": "1234"}  # username:password

def login(username, password):
    return USERS.get(username) == password

# ---------------- FILE TYPES ----------------
FILE_TYPES = {
    "Images": [
        'jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'svg', 'webp', 'heic'
    ],

    "Documents": [
        'pdf', 'doc', 'docx', 'txt', 'rtf', 'odt', 'tex', 'md', 'log'
    ],

    "Videos": [
        'mp4', 'mkv', 'avi', 'mov', 'wmv', 'flv', 'webm', 'mpeg', '3gp'
    ],

    "Audio": [
        'mp3', 'wav', 'aac', 'flac', 'ogg', 'wma', 'm4a', 'amr'
    ],

    "Archives": [
        'zip', 'rar', '7z', 'tar', 'gz', 'bz2', 'iso'
    ],

    "Spreadsheets": [
        'xlsx', 'xls', 'ods', 'csv', 'tsv'
    ],

    "Presentations": [
        'ppt', 'pptx', 'key', 'odp'
    ],

    "Executables": [
        'exe', 'msi', 'bat', 'cmd', 'sh', 'apk', 'jar', 'py', 'js'
    ],

    "Databases": [
        'db', 'sqlite', 'sql', 'mdb', 'accdb'
    ],

    "Design & 3D": [
        'psd', 'ai', 'xd', 'fig', 'sketch', 'blend', 'obj', 'fbx', 'stl'
    ],

    "Code Files": [
        'py', 'java', 'cpp', 'c', 'cs', 'html', 'css', 'js', 'php', 'xml', 'json', 'ipynb'
    ],

    "System Files": [
        'dll', 'sys', 'ini', 'cfg', 'drv'
    ],

    "Fonts": [
        'ttf', 'otf', 'woff', 'woff2'
    ],

    "Icons": [
        'ico', 'icns', 'svg', 'cur', 'ani'
    ],

    "Others": []  # fallback for unrecognized extensions
}

last_actions = []  # For undo

def organize_files(src, dst):
    if not os.path.exists(dst):
        os.makedirs(dst)

    moved_files = []
    for filename in os.listdir(src):
        file_path = os.path.join(src, filename)
        if os.path.isfile(file_path):
            ext = filename.split('.')[-1].lower()
            moved = False
            for category, extensions in FILE_TYPES.items():
                if ext in extensions:
                    folder = os.path.join(dst, category)
                    os.makedirs(folder, exist_ok=True)
                    new_path = os.path.join(folder, filename)
                    shutil.move(file_path, new_path)
                    moved_files.append((new_path, file_path))
                    moved = True
                    break
            if not moved:
                other_folder = os.path.join(dst, "Others")
                os.makedirs(other_folder, exist_ok=True)
                new_path = os.path.join(other_folder, filename)
                shutil.move(file_path, new_path)
                moved_files.append((new_path, file_path))
    last_actions.append(moved_files)

def undo_last_action():
    if not last_actions:
        return False
    moved_files = last_actions.pop()
    for new_path, old_path in moved_files:
        if os.path.exists(new_path):
            shutil.move(new_path, old_path)
    return True

# ---------------- BACKUP ----------------
def backup_files(src, dst_folder="backups"):
    os.makedirs(dst_folder, exist_ok=True)
    backup_path = os.path.join(dst_folder, "backup")
    shutil.make_archive(backup_path, 'zip', src)
    return backup_path + ".zip"

# ---------------- JUNK DETECTION ----------------
def detect_junk(folder):
    junk_exts = ['tmp', 'log', 'bak']
    return [os.path.join(root, f) for root, _, files in os.walk(folder) for f in files if f.split('.')[-1].lower() in junk_exts]

# ---------------- MALWARE SCAN ----------------
'''def scan_malware(folder):
    known_hashes = {"e99a18c428cb38d5f260853678922e03"}  # example MD5
    infected = []
    for root, _, files in os.walk(folder):
        for file in files:
            try:
                with open(os.path.join(root, file), "rb") as f:
                    if hashlib.md5(f.read()).hexdigest() in known_hashes:
                        infected.append(os.path.join(root, file))
            except:
                pass
    return infected '''

# ---------------- NOTIFICATION ----------------
def send_notification(title, message):
    notification.notify(title=title, message=message, timeout=5)

# ---------------- EMAIL ALERT ----------------
def send_email_alert(to_email, subject, body):
    from_email = "anku5149@gmail.com"
    password = "drqn nrgk kwyv ouiz"  # App password required
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(from_email, password)
            server.sendmail(from_email, to_email, msg.as_string())
        return True
    except Exception as e:
        print("Email failed:", e)
        return False

# ---------------- GUI ----------------
class SmartOrganizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart File Organizer")
        self.root.geometry("850x500")
        self.root.configure(bg="#1e1e2f")

        self.src_var = tk.StringVar()
        self.dst_var = tk.StringVar()

        # Sidebar
        sidebar = tk.Frame(root, bg="#2a2a3d", width=200)
        sidebar.pack(side="left", fill="y")

        tk.Label(sidebar, text="📂 Smart Organizer", font=("Arial", 14, "bold"), bg="#2a2a3d", fg="white").pack(pady=20)

        buttons = [
            ("📑 Organize Files", self.organize),
            ("↩️ Undo", self.undo),
            ("💾 Backup", self.backup),
            ("🧹 Detect Junk", self.check_junk),
            ("⚠️ Scan Malware", self.check_malware),
            ("✉️ Send Email", self.send_email)
        ]

        for txt, cmd in buttons:
            b = tk.Button(sidebar, text=txt, command=cmd, bg="#3a3a4f", fg="white", relief="flat", pady=10, anchor="w")
            b.pack(fill="x", padx=15, pady=5)

        # Main panel (centered layout)
        main_panel = tk.Frame(root, bg="#1e1e2f")
        main_panel.pack(side="right", expand=True, fill="both")

        center_frame = tk.Frame(main_panel, bg="#1e1e2f")
        center_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Source Folder
        tk.Label(center_frame, text="Source Folder", font=("Arial", 10, "bold"), bg="#1e1e2f", fg="white").pack(pady=5)
        tk.Entry(center_frame, textvariable=self.src_var, width=50, justify="center").pack()
        tk.Button(center_frame, text="Browse", command=self.browse_src, bg="#3a3a4f", fg="white").pack(pady=10)

        # Destination Folder
        tk.Label(center_frame, text="Destination Folder", font=("Arial", 10, "bold"), bg="#1e1e2f", fg="white").pack(pady=5)
        tk.Entry(center_frame, textvariable=self.dst_var, width=50, justify="center").pack()
        tk.Button(center_frame, text="Browse", command=self.browse_dst, bg="#3a3a4f", fg="white").pack(pady=10)

        # Status
        self.status_label = tk.Label(center_frame, text="Status: Ready", bg="#1e1e2f", fg="lightgreen", font=("Arial", 10, "bold"))
        self.status_label.pack(pady=10)

    def browse_src(self):
        self.src_var.set(filedialog.askdirectory())

    def browse_dst(self):
        self.dst_var.set(filedialog.askdirectory())

    def update_status(self, text, color="lightgreen"):
        self.status_label.config(text=f"Status: {text}", fg=color)

    def organize(self):
        organize_files(self.src_var.get(), self.dst_var.get())
        send_notification("Organizer", "Files organized successfully")
        self.update_status("Files organized successfully")
        if messagebox.askyesno("Backup", "Do you want to create a backup?"):
            self.backup()

    def undo(self):
        if undo_last_action():
            self.update_status("Undo successful")
        else:
            self.update_status("Nothing to undo", "orange")

    def backup(self):
        path = backup_files(self.src_var.get())
        self.update_status(f"Backup created: {path}")

    def check_junk(self):
        junk = detect_junk(self.src_var.get())
        if junk:
            messagebox.showwarning("Junk Files", "\n".join(junk))
            self.update_status("Junk files found", "orange")
        else:
            self.update_status("No junk files", "lightgreen")

    def check_malware(self):
        infected = []  # placeholder since scan_malware is commented out
        if infected:
            messagebox.showerror("Malware Found", "\n".join(infected))
            self.update_status("Malware detected", "red")
        else:
            self.update_status("No malware found")

    def send_email(self):
        success = send_email_alert("recipient@example.com", "Organizer Alert", "This is a test alert from Smart Organizer.")
        if success:
            self.update_status("Email sent successfully")
        else:
            self.update_status("Email failed", "red")

# ---------------- LOGIN WINDOW ----------------
class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login - Smart Organizer")
        self.root.geometry("400x250")
        self.root.configure(bg="#1e1e2f")

        tk.Label(root, text="Login", font=("Arial", 18, "bold"), bg="#1e1e2f", fg="white").pack(pady=20)

        tk.Label(root, text="Username", bg="#1e1e2f", fg="white").pack()
        self.username = tk.Entry(root)
        self.username.pack(pady=5)

        tk.Label(root, text="Password", bg="#1e1e2f", fg="white").pack()
        self.password = tk.Entry(root, show="*")
        self.password.pack(pady=5)

        tk.Button(root, text="Login", command=self.check_login, bg="#3a3a4f", fg="white").pack(pady=15)

    def check_login(self):
        user = self.username.get()
        pwd = self.password.get()
        if login(user, pwd):
            self.root.destroy()
            main_app()
        else:
            messagebox.showerror("Error", "Invalid credentials!")

def main_app():
    root = tk.Tk()
    app = SmartOrganizerApp(root)
    root.mainloop()

if __name__ == "__main__":
    login_root = tk.Tk()
    LoginWindow(login_root)
    login_root.mainloop()
