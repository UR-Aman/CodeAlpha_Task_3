import os
import shutil

def move_jpg_files(source, destination):
    if not os.path.exists(source):
        print("❌ Source folder does not exist. Please check the path.")
        return

    if not os.path.exists(destination):
        os.makedirs(destination)
        print(f"📁 Created destination folder: {destination}")

    moved_files = 0

    for file in os.listdir(source):
        if file.lower().endswith(('.jpg', '.jpeg')):
            src_path = os.path.join(source, file)
            dest_path = os.path.join(destination, file)
            shutil.move(src_path, dest_path)
            moved_files += 1
            print(f"✅ Moved: {file}")

    if moved_files == 0:
        print("ℹ️ No .jpg or .jpeg files found in the source folder.")
    else:
        print(f"\n🎉 Task Complete! Total files moved: {moved_files}")

# -------- Main Program --------
print("🔄 JPG File Mover — Python Automation Script")
source_folder = input("📂 Enter source folder path: ").strip()
destination_folder = input("📁 Enter destination folder path: ").strip()

move_jpg_files(source_folder, destination_folder)
