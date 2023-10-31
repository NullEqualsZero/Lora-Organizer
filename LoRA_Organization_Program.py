import os
import shutil
import re

lora_folder_path = r"C:\Users\nulle\Lora_Org\Lora"
ignored_file = "LoRA_Organization_Program.py"  # Name of the file to be ignored

def extract_prefix(file_name):
    # Use regular expression to extract the prefix
    prefix_match = re.match(r'^[\w\s\-]+', file_name)
    if prefix_match:
        return prefix_match.group(0).strip()
    else:
        return None

def organize_loras(lora_folder_path):
    # Get a list of all files in the lora folder
    lora_files = os.listdir(lora_folder_path)

    # Create a dictionary to store files based on their prefixes
    file_dict = {}

    for lora_file in lora_files:
        if lora_file == ignored_file:
            continue  # Skip the specified file

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
            shutil.move(lora_file_path, os.path.join(lora_folder, lora_file))

organize_loras(lora_folder_path)
