import os
import sys

# --- Configuration ---
# IMPORTANT: Replace this path with the actual path to your folder
# Use a raw string (r'...') on Windows to handle backslashes correctly
FOLDER_PATH = r'C:\Users\Koko\Desktop\New Folder'
# --- End Configuration ---

def add_txt_extension(target_dir):
    """
    Finds files without extensions in target_dir and renames them by adding .txt.
    """
    # 1. Check if the target directory exists
    if not os.path.isdir(target_dir):
        print(f"Error: Directory not found: {target_dir}")
        return False

    print(f"Scanning directory: {target_dir}")
    files_renamed_count = 0

    # 2. Iterate through all items in the directory
    try:
        for filename in os.listdir(target_dir):
            current_path = os.path.join(target_dir, filename)

            # 3. Check if it's a file and if it has NO extension
            if os.path.isfile(current_path):
                # os.path.splitext splits 'myfile.txt' into ('myfile', '.txt')
                # or 'myfile' into ('myfile', '')
                base_name, extension = os.path.splitext(filename)

                if extension == '':
                    # 4. This file has no extension, prepare to rename
                    new_filename = filename + ".txt"
                    new_path = os.path.join(target_dir, new_filename)

                    # 5. Rename the file
                    try:
                        # Safety check: Make sure a file with the new name doesn't already exist
                        if os.path.exists(new_path):
                             print(f"  Skipping rename: '{new_filename}' already exists.")
                        else:
                            os.rename(current_path, new_path)
                            print(f"  Renamed: '{filename}' -> '{new_filename}'")
                            files_renamed_count += 1

                    except OSError as rename_error:
                        print(f"  Error renaming '{filename}': {rename_error}")
                    except Exception as e:
                         print(f"  An unexpected error occurred renaming '{filename}': {e}")


    except OSError as list_error:
        print(f"Error accessing directory {target_dir}: {list_error}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred while scanning the directory: {e}")
        return False

    print(f"\nFinished. Renamed {files_renamed_count} file(s).")
    return True

# --- Run the script ---
if __name__ == "__main__":
    if not add_txt_extension(FOLDER_PATH):
        sys.exit(1) # Indicate failure