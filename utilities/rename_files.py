import os
import sys

def rename_files(folder_path):
    if not os.path.isdir(folder_path):
        print("Error: Folder path doesn't exist.")
        return

    folder_name = os.path.basename(folder_path)
    files = os.listdir(folder_path)
    
    for index, file_name in enumerate(files, start=0):
        old_path = os.path.join(folder_path, file_name)
        if os.path.isfile(old_path):
            file_extension = os.path.splitext(file_name)[1]
            new_file_name = f"{index}_{folder_name}{file_extension}"
            new_path = os.path.join(folder_path, new_file_name)
            os.rename(old_path, new_path)
            print(f"Renamed: {file_name} -> {new_file_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <folder_path>")
    else:
        folder_path = sys.argv[1]
        rename_files(folder_path)
