import sys
import shutil

def create_backup(file_name):
    try:
        shutil.copy(file_name, f"{file_name}.bak")
        print(f"Backup of {file_name} created successfully.")
    except FileNotFoundError:
        print(f"Error: File {file_name} not found.")
    except PermissionError:
        print(f"Error: Permission denied. Unable to create backup of {file_name}.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_name>")
        sys.exit(1)

    file_to_backup = sys.argv[1]
    create_backup(file_to_backup)
