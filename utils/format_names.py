import os

def rename_files_and_folders(path):
    for root, dirs, files in os.walk(path, topdown=False):
        # Rename files
        for name in files:
            old_path = os.path.join(root, name)
            new_name = name.replace(' ', '_').replace('-', '_')
            new_path = os.path.join(root, new_name)
            if old_path != new_path:
                os.rename(old_path, new_path)
                print(f"Renamed file: {old_path} -> {new_path}")

        # Rename directories
        for name in dirs:
            old_path = os.path.join(root, name)
            new_name = name.replace(' ', '_').replace('-', '_')
            new_path = os.path.join(root, new_name)
            if old_path != new_path:
                os.rename(old_path, new_path)
                print(f"Renamed directory: {old_path} -> {new_path}")

if __name__ == '__main__':
    path = 'autumn_intern_23'
    rename_files_and_folders(path)
    print("Renaming complete.")