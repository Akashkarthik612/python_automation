"""
Python automation script to clean a messy folder by 
renaming files to a proper naming convention.

Advantages:
✅ Eliminates 100% of manual file renaming effort
✅ Improves accessibility and organization
"""

import os

def rename_folder(folder_path):
    files = os.listdir(folder_path)
    for i, filename in enumerate(files, start=1):
        file_ext = os.path.splitext(filename)[1]
        new_name = f"{i}_{filename}_{file_ext}"
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_name)
        os.rename(old_file, new_file)
    print("Renaming completed successfully!")

# Replace with your own folder path
rename_folder(r"E:\i_phone _14_pro")
