#!/bin/python3
"""
 _          _           ___ _____   ____        _        _                    
| |    __ _| |__       / _ \___ /  |  _ \  __ _| |_ __ _| |__   __ _ ___  ___ 
| |   / _` | '_ \ ____| (_) ||_ \  | | | |/ _` | __/ _` | '_ \ / _` / __|/ _ \
| |__| (_| | |_) |_____\__, |__) | | |_| | (_| | || (_| | |_) | (_| \__ \  __/
|_____\__,_|_.__/        /_/____/  |____/ \__,_|\__\__,_|_.__/ \__,_|___/\___|
                                                                              
 ____            _                 
/ ___| _   _ ___| |_ ___ _ __ ___  
\___ \| | | / __| __/ _ \ '_ ` _ \ 
 ___) | |_| \__ \ ||  __/ | | | | |
|____/ \__, |___/\__\___|_| |_| |_|
       |___/
"""


''' In-House framework for interacting with database objects. '''
from submodules.DatabaseAPI import SQLite3


def buildAdministratorDatabase( database: str="./sqlite3.db", **config ):
    """
    """

    # Default configuration for the Lab-93 database system used by
    # other in-house software kits.
    #
    # Each key in the dict represents a table within the database,
    # and contains the metadata to configure the setup to suit
    # our needs.
    if not config:
        config = { "credentials": { "username": "TEXT",

                                    "columns":  { "telegram_admin": "BYTES",
                                                  "alpaca_key":     "BYTES",
                                                  "alpaca_secret":  "BYTES",
                                                },
                                  },

                   "contacts": { "first_name": "REQUIRED TEXT",

                                 "columns": { "last_name":     "REQUIRED TEXT",
                                              "email_address": "TEXT":,
                                              "phone_number":  "TEXT",
                                              "github":        "TEXT",
                                              "website":       "TEXT",
                                            },
                               },
                 }

    # Iterate through every top-level key and validate it's existence.
    #NOTE:
    ''' Each key must also be a dictionary containing:

            1.  - A key representing the name of the default column within the
                  table, with a value describing it's SQLite3 datatype.

            2.  - A 'columns' key that is ALSO a dictionary who's keys function
                  exactly the same as the first key, with the key itself
                  describing the column name and the value stating the type.
    '''
    for table in config.keys():

        # If the table exists;
        if SQLite3.checkTable( database, 
                               table=str(table) ) > 0: print(
            f"  --{str(table).title()} table exists."
        )

        # If the table does not exist;
        else:

            ''' The first key in the table dict is the default column. '''
            default_column = [ column for column in config[table].keys() ][0]

            ''' Plug the string value of the key into the SQLite3.newTable
            function, along with the table string. '''
            SQLite3.newTable( database,
                              table=str(table),
                              column=str(default_column),
                              column_type=config[table][default_column] ); print(
                f"  --{str(table).title()} table created."
            )


        # Iterate through the columns dictionary inside the table dictionary.
        for column in config[table]["columns"].keys():

            # If the column exists;
            if SQLite3.checkColumn( database,
                                    table=str(table),
                                    column=str(column)) > 0: print(
                f"    --{str(column).title()} column exists."
            )

            # If the column does not exist;
            else:
                column_type = config[table]["columns"][column]
                SQLite3.newColumn( database,
                                   table=str(table),
                                   column=str(column),
                                   column_type=column_type, ); print(
                    f"    --{str(column).title()} column created."
                )

if __name__ == "__main__":
    buildAdministratorDatabase()
