import os
import json

def get_cleaner_exception_list():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    raw_data = open(os.path.join(script_dir, '../config.json'))
    json_data = json.load(raw_data)

    return json_data["clean_exceptions"]

def list_files(directory):
    cleaner_exception_list = get_cleaner_exception_list()
    for root, dirs, files in os.walk(directory):
        for name in files:
            # dumb but works
            if name == 'Makefile' or name.endswith('.c') or name.endswith('.h'):
                continue
            
            # create extension here
            if any(name.endswith('.' + ext) for ext in cleaner_exception_list):
                continue

            os.remove(os.path.join(root, name))

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    dir_path = os.path.join(script_dir, '../ldd-usb')
    list_files(dir_path)