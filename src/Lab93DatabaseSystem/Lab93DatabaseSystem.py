#!/bin/python3
"""
"""

# Only import what we need from our base, just to keep it light.
from sqlite3 import connect

# Same with logging, only rename the members for readability.
from logging import getLogger, exception
from logging import info as information
from logging import debug as debugging


class Lab93DatabaseSystem:

    def __init__( self,
                  database: str="./sqlite3.db",
                  interactive_mode: bool=False  ) -> None:
        """
        """
        getLogger(); information(
            f"Initialized Lab-93 database system."
        )
        
        debugging(
            f"Beginning constants definition"
        )

        self.sql = SQLite3_Statements(
            database
        )


    class InteractiveFunctionality:
        def __init__(self, database): pass
        def viewTables(self)


    class databaseConnection:
        """
        The Lab93DatabaseSystem.databaseConnection is a throw-away class intended
        to abstract away the boiler-plate code involved with setting up the connection
        with the database.

        Given a `database` string, which is a valid filepath pointing to a .db file,
        the member objects databaseConnection.connection and databaseConnection.cursor
        are accessibile from a freshly created thread.

        All access attempts are logged by the caller.
        """

        def __init__( self,
                      database: str="./.sqlite3.db" ) -> None:

            getLogger(); information(
                f"Establishing database connection with {database}"
            )

            debugging(
                f"Attempting connection with sqlite3 database file."
            )
            try:
                self.connection = connect(
                    database
                ); self.cursor = self.connection\
                                     .cursor()

                debugging(
                    f"Database connection successful."
                )
            
            except Exception as error:
                exception(
                    f"There was an issue connecting to the {database} database;\n{error}"
                ); return error


    class SQLite3_Statements:
        """
        The SQLite3_Statements class offers a library of pre-defined
        statements that are easily accessed by a suite of functions
        co-relating with those statements.

        The class object accepts a `database` string that should be a valid
        filepath to an sqlite3.db file.  After initialization, member methods
        can be called at-will in your code to provide a simple API for database
        functionality.
        """

        def __init__( self,
                      database: str="./test.db" ) -> None:

            ''' (Linux) Filepath to an sqlite3.db file. '''
            self.database = database

            ''' Master dictionary of various sqlite3 statements. '''
            self.statements = {
                # Select a specific column from a row based on another column.
                'queryCompareColumns': "SELECT {} FROM {} WHERE  {}='{}';",

                # Add a new column to the database.
                'createNewColumn': "ALTER TABLE {} ADD {} {}",
            
                # Create a new new table within the database.
                'createNewTable': "CREATE TABLE IF NOT EXISTS {}({} {} PRIMARY KEY);",

                # Check if a specific table exists within the database.
                'queryTableExistence': "SELECT COUNT(name) FROM sqlite_master WHERE type='table' AND name='{}';",

                # Check a given table for a specific column.
                'queryColumnExistence': "SELECT COUNT(*) FROM pragma_table_info('{}') WHERE name='{}';",

                # Enumerate a list of tables within the master record.
                'queryTableList': "SELECT name FROM sqlite_schema WHERE type='table' ORDER BY name;"
            }


        def newColumn( self,
                       table: str="test_table_one",
                       column: str="test_column_one",
                       column_type: str="UNIQUE PRIMARY TEXT" ) -> None:
            """
            SQLite3_Statements.newColumn will create a new header within a table of your choosing.
            It accepts three strings; `table`, `column`, and `column_type`; where `table` is the
            target to be altered, `column` is the label applied to the header, and `column_type`
            are as many (supposedly valid) sQLite3 datatypes as you desire.

            Changes made are saved on a successful exit.
            """

            db = databaseConnection(self.database)

            db.cursor\
              .execute( self.statements['createNewColumn']\
                            .format( table.lower()\
                                          .replace(" ", "-"),

                                     column.lower()\
                                           .replace(" ", "-"),

                                     column_type.upper()       ) )

            return db.connection\
                     .commit()


        def compareColumns( self,
                            column: str="test_column_one",
                            table: str="test_table_one",
                            comparator: str="test_column_two",
                            value: str="test_value_two") -> str:
            """
            SQLite3_Statements.compareColumns describes an easy method to pull a specific
            value from any given line based on a known value within said line.  The exact
            logic behind the query goes like: "SELECT column FROM table WHERE comparator=value".

            All arguments are to be given as strings; where `column` describes what to select
            from the `table`, based on a secondary column `comparator` containing the equivalent
            of `value`.

            The contents of the `column` search results are then returned to the caller
            as a string.
            """
            return databaseConnection(
                self.database
            ).cursor\
             .execute( self.statements['queryCompareColumns']\
                           .format( column,
                                    table,
                                    comparator,
                                    value       )
                                                               )\
             .fetchall()[0][0]


        def newTable( self,
                      table: str="test_table_one",
                      column: str="test_column_one",
                      column_type: str="UNIQUE TEXT" ) -> None:
            """
            SQLite3_Statements.newTable will create a new `table` initialized with a header
            labeled as `column`; any extra datatypes can be described by `column_type`, but
            the statement includes the PRIMARY KEY types by default.

            Changes made to the table are commited upon return.
            """

            ''' Establish database connection. '''
            db = databaseConnection(self.database)

            ''' Format command string with argument input. '''
            db.cursor\
              .execute( self.statements['createNewTable']\
                            .format ( table.lower()\
                                           .replace(" ", "_"),

                                      column.lower()\
                                            .replace(" ", "_"),

                                      column_type.upper()       ) )

            ''' Save your work. '''
            return db.connection\
                     .commit()


        def checkTable( self,
                        # A collection of records to be found.
                        table: str="test_table_one"            ) -> int:
            """
            SQLite3_Statements.checkTable will query the master record for the existence of
            a `table` by the same name as the given argument.

            The search will return an integer; where anything over zero(0) describes a
            successful match.
            """
            return databaseConnection.cursor\
                                     .execute( self.statements['queryTableExistence']\
                                                   .format( table.lower() )          )\
                                     .fetchall()[0][0]


        def checkColumn( self,
                         # Record collection being searched.
                         table: str="test_table_one",
                         # Column header being searched for.
                         column: str="test_column_one"       ) -> int:
            """
            SQLite3_Statements.checkColumn queries a given `table` for the presence of a header
            labeled `column`; where any return value over zero(0) indicates a match.
            """

            return databaseConnection.cursor\
                                     .execute( self.statements['queryColumnExistence']\
                                                   .format( table.lower(),
                                                            column.lower() )            )\
                                     .fetchall()[0][0]