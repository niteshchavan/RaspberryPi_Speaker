import os
import re

def clean_filename(filename):
    # Remove non-English characters and symbols
    cleaned_name = re.sub(r'[^\x00-\x7F]+', '', filename)
    
    # Replace consecutive underscores with a single underscore
    cleaned_name = re.sub(r'_+', '_', cleaned_name)
    
    return cleaned_name

def rename_files(folder_path):
    for filename in os.listdir(folder_path):
        old_path = os.path.join(folder_path, filename)
        
        if os.path.isfile(old_path):
            new_filename = clean_filename(filename)
            new_path = os.path.join(folder_path, new_filename)
            
            os.rename(old_path, new_path)
            print(f"Renamed '{filename}' to '{new_filename}'")

if __name__ == "__main__":
    folder_path = "/home/nitesh/oled/mp4/"
    rename_files(folder_path)
