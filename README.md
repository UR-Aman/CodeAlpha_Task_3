# CodeAlpha_ImageMover 🖼️

This project is submitted as part of the **Python Programming Internship at CodeAlpha**.  
It is a Python script that automates the task of moving all `.jpg` and `.jpeg` files from one folder to another.

---

## 📦 Description

This automation script helps you organize image files by:
- Asking the user to enter a **source folder** and a **destination folder**
- Moving all `.jpg` or `.jpeg` files found in the source to the destination
- Automatically creating the destination folder if it doesn't exist

---

## ⚙️ Features

- ✅ Detects `.jpg` and `.jpeg` files
- 📂 Creates destination folder if needed
- 📦 Moves files using `shutil`
- 🧠 Gives total moved file count
- ❌ Shows helpful messages if paths are wrong

---

## 🛠️ Technologies Used

- `os` for file system interaction
- `shutil` for moving files

---

## ▶️ How to Run

1. Open terminal or command prompt
2. Run the script:
```bash
python "Image mover.py"

It will ask:

📂 Enter source folder path: C:\Users\YourName\Downloads\Photos
📁 Enter destination folder path: C:\Users\YourName\Pictures\JPGs



