import os
import shutil
import hashlib

def create_folders(root_folder, subdirectories):
    # Create the root folder if it doesn't exist
    if not os.path.exists(root_folder):
        os.mkdir(root_folder)

    # Create the subdirectories if they don't exist
    for subdir in subdirectories:
        if not os.path.exists(os.path.join(root_folder, subdir)):
            try:
                os.mkdir(os.path.join(root_folder, subdir))
            except Exception as e:
                print(f"Error creating directory {subdir}: {e}")

def find_duplicate_files(root_dir):
    # Dictionary to store file names and their paths
    file_dict = {}
    # Dictionary to store file hashes and their paths
    hash_dict = {}

    # Traverse the directory tree
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            # Get the full path of the file
            file_path = os.path.join(dirpath, filename)
            # Compute the hash of the file
            with open(file_path, 'rb') as f:
                file_hash = hashlib.md5(f.read()).hexdigest()

            # Check if the file name already exists in the dictionary
            if filename in file_dict:
                # Append the path to the existing file name
                file_dict[filename].append(file_path)
            else:
                # Add the file name and path to the dictionary
                file_dict[filename] = [file_path]

            # Check if the file hash already exists in the dictionary
            if file_hash in hash_dict:
                # Append the path to the existing file hash
                hash_dict[file_hash].append(file_path)
            else:
                # Add the file hash and path to the dictionary
                hash_dict[file_hash] = [file_path]

    # Write the file names and paths to a text file
    with open('duplicate_files_by_name.txt', 'w') as f:
        for filename, paths in file_dict.items():
            if len(paths) > 1:
                f.write(f'{filename}:\n')
                for path in paths:
                    f.write(f'\t{path}\n')

    # Write the file hashes and paths to a text file
    with open('duplicate_files_by_hash.txt', 'w') as f:
        for file_hash, paths in hash_dict.items():
            if len(paths) > 1:
                f.write(f'{file_hash}:\n')
                for path in paths:
                    f.write(f'\t{path}\n')

def move_and_fix(root_folder, new_folder, extensions):
    # Create the new folder if it doesn't exist
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)

    # Walk through the root folder and its subdirectories
    for foldername, subfolders, filenames in os.walk(root_folder):
        for filename in filenames:
            # Check if the file has an extension in the list
            if any(filename.endswith(ext) for ext in extensions):
                # Get the full path of the file
                file_path = os.path.join(foldername, filename)
                # Construct the destination path
                dst_path = os.path.join(new_folder, filename)
                i = 1
                while os.path.exists(dst_path):
                    name, ext = os.path.splitext(filename)
                    dst_path = os.path.join(new_folder, f"{name}{i}{ext}")
                    i += 1
                # Move the file to the new folder with the resolved filename
                shutil.move(file_path, dst_path)
