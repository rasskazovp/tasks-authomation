import os
import shutil
import json


def read_json(file_name: str) -> dict:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(script_dir, file_name)
    with open(json_path, "r") as file:
        return json.load(file)


def organize_folder(folder, file_types):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1].lower()
            for folder_name, extensions in file_types.items():
                if ext in extensions:
                    target_folder = os.path.join(folder, folder_name)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_folder, filename))
                    print(f"Moved {filename} to {folder_name}")


if __name__ == "__main__":
    folder_path = os.path.expanduser(r"~\Downloads")
    file_types = read_json("config.json")
    organize_folder(folder_path, file_types)
