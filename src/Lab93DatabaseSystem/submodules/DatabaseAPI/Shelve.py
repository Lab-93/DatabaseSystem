#!/bin/python3
"""
 _          _           ___ _____   ____  _          _           
| |    __ _| |__       / _ \___ /  / ___|| |__   ___| |_   _____ 
| |   / _` | '_ \ ____| (_) ||_ \  \___ \| '_ \ / _ \ \ \ / / _ \
| |__| (_| | |_) |_____\__, |__) |  ___) | | | |  __/ |\ V /  __/
|_____\__,_|_.__/        /_/____/  |____/|_| |_|\___|_| \_/ \___|
                                                                 
 ___                 _                           _        _   _             
|_ _|_ __ ___  _ __ | | ___ _ __ ___   ___ _ __ | |_ __ _| |_(_) ___  _ __  
 | || '_ ` _ \| '_ \| |/ _ \ '_ ` _ \ / _ \ '_ \| __/ _` | __| |/ _ \| '_ \ 
 | || | | | | | |_) | |  __/ | | | | |  __/ | | | || (_| | |_| | (_) | | | |
|___|_| |_| |_| .__/|_|\___|_| |_| |_|\___|_| |_|\__\__,_|\__|_|\___/|_| |_|
              |_|                                                           
    A simple key: value database for fast, scriptable data-storage capabilities.
"""

import shelve

def newLine( database: str="./.database.db",
             table: str="administrator",
             index: str="credentials",
             value: str="test_credentials"):

    with shelve.open(database) as  shelf:
        shelf = {
            str(table): {
                str(index): value
            }
        }

        print(shelf)

def readLine( database: str="./.database.db",
              table: str="administrator",
             index: str="credentials"         ):

    with shelve.open(database) as  shelf:
        print(shelf[table])