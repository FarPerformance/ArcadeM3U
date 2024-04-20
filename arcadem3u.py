import os
import argparse
import zipfile
import xml.etree.ElementTree as ET

# Function to clean folder name from invalid characters and remove content within parentheses at the end
def clean_folder_name(name):
    invalid_chars = r':*?"<>|'
    cleaned_name = ''.join(c for c in name if c not in invalid_chars)
    cleaned_name = cleaned_name.split(' (', 1)[0]  # Remove content within parentheses at the end
    cleaned_name = cleaned_name.replace('/', '-')  # Replace '/' with '-'
    return cleaned_name.strip()  # Strip leading/trailing whitespace

# Function to create folder based on description, create .m3u file, and move .zip file
def create_folder_and_m3u_file_and_move_zip(description, zip_folder_path, zip_file_name):
    cleaned_folder_name = clean_folder_name(description)
    folder_path = os.path.join(zip_folder_path, cleaned_folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Created folder: {folder_path}")
    else:
        print(f"Folder already exists: {folder_path}")

    m3u_file_path = os.path.join(folder_path, f"{cleaned_folder_name}.m3u")
    with open(m3u_file_path, "w") as m3u_file:
        m3u_file.write(zip_file_name)
    print(f"Created .m3u file: {m3u_file_path}")

    zip_file_path = os.path.join(zip_folder_path, zip_file_name)
    zip_file_destination = os.path.join(folder_path, zip_file_name)
    os.rename(zip_file_path, zip_file_destination)
    print(f"Moved {zip_file_name} to {folder_path}")

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Process XML data and organize ZIP files.")
    parser.add_argument("zip_folder_path", help="Path to the folder containing the .zip files")
    parser.add_argument("xml_file_path", help="Path to the XML file")
    args = parser.parse_args()

    # Load the XML file
    xml_tree = ET.parse(args.xml_file_path)
    xml_root = xml_tree.getroot()

    # Create a dictionary to store machine and game names and descriptions
    descriptions = {}

    # Iterate through each "machine" or "game" element
    for element in xml_root.findall(".//machine"):
        name = element.attrib.get("name")
        description = element.find("description").text
        descriptions[name] = description
    for element in xml_root.findall(".//game"):
        name = element.attrib.get("name")
        description = element.find("description").text
        descriptions[name] = description

    # Loop through each .zip file
    for zip_file_name in os.listdir(args.zip_folder_path):
        if zip_file_name.endswith(".zip"):
            base_name = os.path.splitext(zip_file_name)[0]
            if base_name in descriptions:
                description = descriptions[base_name]
                create_folder_and_m3u_file_and_move_zip(description, args.zip_folder_path, zip_file_name)
            else:
                print(f"No description found for machine or game '{base_name}'.")
