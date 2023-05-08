# Lab-93 SQLite3 Databsse API
![PyPI](https://img.shields.io/pypi/v/Lab93DatabaseSystem?label=pip%20version&style=plastic)

This package represents a repository of useful SQLite3 statements known to the Lab-93 server system.
It provides a handy interface for interacting with sqlite3.db files in a safe and reproductible manner; and can be used either as a stand-alone command line program, or with your scripts to abstract away SQLite3 boilerplate.

## Installation
```
python3 -m pip install --upgrade Lab93DatabaseSystem
```

## Usage
### Interactivity Mode
The dbsystem package provides a graphical environment for viewing, managing, and otherwise interacting with any given database.
The database manager consists of a viewing system for the selected ```.db``` file, which is selected at startup.
Once a database is selected the view introduces a selection of tabs listing each table within the file; each view consists of the the entire contents of said table.
Below the workspace window is a persistent panel describing a form meant to guide the user to making an appropriate command.
Queries and functions can be selected via a drop-down menu that actively alters the rest of the form to fit the usage scenario. ```For example, it wouldn't make sense to include a field for a second column with a function that only cares about a single column; adjust the viewpoint to match this worldview!```

### Scripting Mode
To use the api with your python scripts the package needs to be imported and initialized.
To do so, one need simply add the following to their python file:
```
from Lab93DatabaseSystem.Lab93DatabaseSystem import Lab93DatabaseSystem
databaseAPI = Lab93DatabaseSystem("./sqlite3.db")
```
Once initialized, SQLite3 actions can be executed by referencing the approptriate method.
For example, to create a new table after following the previous example you would type:
```
databaseAPI.newTable("new_table", "column_one", "TEXT")
```
