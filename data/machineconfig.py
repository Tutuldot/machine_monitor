import os
import json 
import pandas

def count_files_in_directory(directory):
    return len([name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))])

def list_directories_and_file_counts(start_path='.'):
    for dirname, dirnames, filenames in os.walk(start_path):
        # Print the directory path
       
        # Count the number of files in this directory
        file_count = count_files_in_directory(dirname)
        # Print the file count
        print(f"Directory: {dirname} Files : {file_count}")

def list_directories_and_filenames_to_dataframe(start_path='.'):
    # Initialize an empty list to store the directory and file data
    directory_files_data = []
    
    for dirname, dirnames, filenames in os.walk(start_path):
        # For each file in the directory, append the directory path and file name
        for filename in filenames:
            directory_files_data.append((dirname, filename))
    
    # Create a DataFrame from the list of tuples
    df = pd.DataFrame(directory_files_data, columns=['Directory', 'Filename'])
    
    return df



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
                
def sample_usage_using_config():

    # list_directories_and_file_counts('/workspace/machine_monitor/sample_directory')
    configuration = get_setup_file()
    wirebond_config = get_setup_file_by_name(configuration,"ACAI")

    name, root, weekly_directory_format, files_to_monitor, file_date_format, directory_filter  = unpack_config(wirebond_config)
    # Print the information or process it as needed
    for x in files_to_monitor:
        print(x['type'])


list_directories_and_file_counts('/workspace/machine_monitor/sample_directory/acai/17')
    


       