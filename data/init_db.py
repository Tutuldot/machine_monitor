import sqlite3
import machineconfig
import hashlib


def strToMd5(str):
    # The string to be hashed
    input_string = str
    input_bytes = input_string.encode('utf-8')
    md5_hash = hashlib.md5()
    md5_hash.update(input_bytes)
    hex_md5 = md5_hash.hexdigest()

    print(f"The MD5 hash of '{input_string}' is: {hex_md5}")
    return hex_md5

# initialization of database
connection = sqlite3.connect('database.db')


with open('structure.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# creation of initial user

cur.execute("INSERT INTO users (username, pwd,userrole) VALUES (?, ?,?)",('admin', strToMd5('admin123'),'admin'))
cur.execute("INSERT INTO users (username, pwd,userrole) VALUES (?, ?,?)",('viewer', strToMd5('viewer123'),'viewer'))

# creation of initial machine setup
configuration = machineconfig.get_setup_file()
for config in configuration:
    name = config['name']
    root = config['root']
    weekly_directory_format = config['weekly_directory_format']
    files_to_monitor = config['files_to_monitor']
    file_date_format = config['file_date_format']
    directory_filter = config['directory_filter']

    for x in files_to_monitor:
        cur.execute("INSERT INTO machine_activity (machine_name, current_work_week, current_date,log_type) VALUES (?, ?, ?, ?)",(name, 0,'2024-01-01',x['type']))



connection.commit()
connection.close()