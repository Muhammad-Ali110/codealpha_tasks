import os
import shutil
import sys

def organize_files(source_directory):
    """
    This program Scans the source_directory for image files and moves them 
    into a subfolder named 'Organized_Images'.
    """
    
    if not os.path.exists(source_directory):
        print(f"❌ Error: The directory '{source_directory}' does not exist.")
        return

    destination_folder = os.path.join(source_directory, "Organized_Images")
    
    if not os.path.exists(destination_folder):
        try:
            os.makedirs(destination_folder)
            print(f"📁 Created new folder: {destination_folder}")
        except OSError as e:
            print(f"❌ Error creating folder: {e}")
            return
    else:
        print(f"ℹ️  Folder already exists: {destination_folder}")

    image_extensions = ('.jpg', '.jpeg', '.png')
    
    files_moved = 0
    
    print(f"\nScanning '{source_directory}' for files...")
    
    for filename in os.listdir(source_directory):
        source_path = os.path.join(source_directory, filename)
        
        if os.path.isfile(source_path):
            if filename.lower().endswith(image_extensions):
                destination_path = os.path.join(destination_folder, filename)
                
                if os.path.exists(destination_path):
                    base, extension = os.path.splitext(filename)
                    counter = 1
                    new_filename = f"{base}_{counter}{extension}"
                    destination_path = os.path.join(destination_folder, new_filename)
                    while os.path.exists(destination_path):
                        counter += 1
                        new_filename = f"{base}_{counter}{extension}"
                        destination_path = os.path.join(destination_folder, new_filename)
                    print(f"⚠️  File exists. Renaming to: {new_filename}")

                try:
                    shutil.move(source_path, destination_path)
                    print(f"✅ Moved: {filename}")
                    files_moved += 1
                except Exception as e:
                    print(f"❌ Failed to move {filename}: {e}")

    print("-" * 30)
    if files_moved == 0:
        print("No image files found to move.")
    else:
        print(f"🎉 Success! Moved {files_moved} files to 'Organized_Images'.")

if __name__ == "__main__":
    print("🤖 AUTO-FILE ORGANIZER 🤖")
    print("This script moves .jpg, .jpeg, and .png files into a separate folder.")
    print("-" * 50)
    
    user_path = input("Enter the full path of the folder to organize: ").strip()
    
    user_path = user_path.replace('"', '')
    
    organize_files(user_path)