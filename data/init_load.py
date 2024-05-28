import sqlite3
import machineconfig


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