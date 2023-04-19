# Lab-93 SQLite3 Databsse API
![PyPI](https://img.shields.io/pypi/v/Lab93DatabaseSystem?label=pip%20version&style=plastic)

This package represents a repository of useful SQLite3 statements known to the Lab-93 server system.
It provides a handy interface for interacting with sqlite3.db files in a safe and reproductible manner; and can be used either as a stand-alone command line program, or with your scripts to abstract away SQLite3 boilerplate.

## Installation
```
python3 -m pip install --upgrade Lab93DatabaseSystem
```

## Usage
### Interactive CLI-Mode
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
