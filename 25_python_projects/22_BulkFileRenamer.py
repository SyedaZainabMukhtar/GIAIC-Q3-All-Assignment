import os

def bulk_file_renamer():
    folder_path = input("Enter folder path: ")
    prefix = input("Enter prefix for new filenames: ")
    
    try:
        files = os.listdir(folder_path)
        for i, filename in enumerate(files, 1):
            old_path = os.path.join(folder_path, filename)
            if os.path.isfile(old_path):
                extension = os.path.splitext(filename)[1]
                new_filename = f"{prefix}_{i}{extension}"
                new_path = os.path.join(folder_path, new_filename)
                os.rename(old_path, new_path)
                print(f"Renamed {filename} to {new_filename}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    bulk_file_renamer()