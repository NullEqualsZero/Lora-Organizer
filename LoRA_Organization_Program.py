import os
import shutil
import re

def extract_prefix(file_name):
    # Use regular expression to extract the prefix
    prefix_match = re.match(r'^[\w\s\-]+', file_name)
    if prefix_match:
        return prefix_match.group(0).strip()
    else:
        return None

def organize_loras(lora_folder_path):
    # Get a list of all files in the specified directory
    lora_files = os.listdir(lora_folder_path)

    # Create a dictionary to store files based on their prefixes
    file_dict = {}

    for lora_file in lora_files:
        # Get the prefix of the LoRA file
        lora_prefix = extract_prefix(lora_file)

        if lora_prefix:
            # Store the file in the dictionary based on its prefix
            if lora_prefix in file_dict:
                file_dict[lora_prefix].append(lora_file)
            else:
                file_dict[lora_prefix] = [lora_file]

    # Move files based on their prefixes
    for lora_prefix, files in file_dict.items():
        lora_folder = os.path.join(lora_folder_path, lora_prefix)
        if not os.path.exists(lora_folder):
            os.makedirs(lora_folder)

        for lora_file in files:
            lora_file_path = os.path.join(lora_folder_path, lora_file)

            # Check if the source and destination paths are different
            if os.path.abspath(lora_folder) != os.path.abspath(lora_file_path):
                shutil.move(lora_file_path, os.path.join(lora_folder, lora_file))

if __name__ == "__main__":
    lora_folder_path = input("Enter the destination directory: ")
    organize_loras(lora_folder_path)
