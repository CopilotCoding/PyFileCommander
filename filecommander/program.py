import filecmdr

while True:

    options = ["Create folder structure", "Find duplicate files", "Move files by types and fix name conflicts", "Exit the program"]
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    selected_option = input("Select an option: ")

    if selected_option == "1":
        print("Using the root folder name and sub folders names array from file_commander.py option 1...")      
        newrootfoldername = "files"
        subdirectories = ["text", "images", "music", "videos", "documents"]  
        try:
            filecmdr.create_folders(newrootfoldername, subdirectories)
        except Exception as e:
            print("Error:", e)

    elif selected_option == "2":
        rootpath = input("Enter a path to find duplicate files inside, this will output two text files where this file_commander.py is running: ")       
        try:
            filecmdr.find_duplicate_files(rootpath)
        except Exception as e:
            print("Error:", e)

    elif selected_option == "3":
        rootpath = input("Enter a path to move files of the types array including same named files to a new folder: ")
        newpath = input("Enter the folder name for the new folder of these files: ")
        print("Using the settings array for the file extension types from file_commander.py option 3...")
        extensions = ['.txt', '.cs', '.py']
        try:
            filecmdr.move_and_fix(rootpath, newpath, extensions)
        except Exception as e:
            print("Error:", e)

    elif selected_option == "4":
            break

    else:
        print("Invalid option selected.")

print("Exiting...")
