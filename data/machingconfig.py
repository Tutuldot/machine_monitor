import os
import json 

def count_files_in_directory(directory):
    return len([name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))])

def list_directories_and_file_counts(start_path='.'):
    for dirname, dirnames, filenames in os.walk(start_path):
        # Print the directory path
        print(f"Directory: {dirname}")
        # Count the number of files in this directory
        file_count = count_files_in_directory(dirname)
        # Print the file count
        print(f"File Count: {file_count}")

def get_setup_file():

    # Define the path to the JSON file
    file_path = '../config/machine_setup.json'

    data = None
    # Read and parse the JSON data
    with open(file_path, 'r') as file:
        data = json.load(file)

    return data

def get_setup_file_by_name(data,machine_name):

    for config in data:
        # Access the configuration details
        if machine_name == config['name']:
            return config     
       
def unpack_config(config):
    name = config['name']
    root = config['root']
    weekly_directory_format = config['weekly_directory_format']
    files_to_monitor = config['files_to_monitor']
    file_date_format = config['file_date_format']
    directory_filter = config['directory_filter']
            
    return name, root, weekly_directory_format, files_to_monitor, file_date_format, directory_filter      
                
def sample_usage():

    # list_directories_and_file_counts('/workspace/machine_monitor/sample_directory')
    configuration = get_setup_file()
    wirebond_config = get_setup_file_by_name(configuration,"WIREBOND")

    name, root, weekly_directory_format, files_to_monitor, file_date_format, directory_filter  = unpack_config(wirebond_config)
    # Print the information or process it as needed
    print(f"Name: {name}")
       