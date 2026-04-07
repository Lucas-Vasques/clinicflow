import json
import os


def ensure_file_exists(file_path):
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump([], file)


def load_data(file_path):
    ensure_file_exists(file_path)
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_data(file_path, data):
    ensure_file_exists(file_path)
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
