
import os
import shutil

def organize_files_by_extension(directory):
    """
    Organizes files in the specified directory into subdirectories based on their file extensions.
    
    Args:
        directory (str): The path to the directory to be organized.
    """
    if not os.path.isdir(directory):
        print(f"The directory {directory} does not exist.")
        return

    # List all files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    for file_name in files:
        # Get the file extension
        file_ext = file_name.split('.')[-1] if '.' in file_name else 'no_extension'
        
        # Define the target directory based on file extension
        target_dir = os.path.join(directory, file_ext.upper())
        
        # Create the target directory if it does not exist
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        
        # Move the file to the target directory
        src = os.path.join(directory, file_name)
        dst = os.path.join(target_dir, file_name)
        shutil.move(src, dst)
        print(f"Moved: {file_name} -> {target_dir}")

    print("File organization complete.")

# Specify the directory to be organized
directory_to_organize = 'C:\\Users\\khush\\OneDrive\\Documents\\KHUSHBOOO IMP'  # Replace with the path to your directory

# Call the function to organize files
organize_files_by_extension(directory_to_organize)







