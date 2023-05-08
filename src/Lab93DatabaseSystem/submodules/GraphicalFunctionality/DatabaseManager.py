from tkinter import Tk, ttk
from submodules.DatabaseAPI import SQLite3

def mainpage():
    root = Tk()
    root.title("Lab-93 Database Management System")
    tab_control = ttk.Notebook(root)

    table_list = self.sql.listTables()

    tab_list = []


    for table in table_list:
        tab_list.appoend( ttk.Frame( tab_control ) )
    
    
    for tab in tab_list:
        for table in table_list:
            tab_control.add( tab, 
                             text=str(table).title()\
                                            .replace("_", " ") )

    tab_control.pack(expand=1, fill="both")

    for tab in tab_list:
        grid_x = 0
        grid_y = 0
        table_headers = self.sql\
                            .listHeaders()

        for column in table_headers:
            ttk.Label( tab,
                       text=f"{column}" )\
                .grid( column=grid_y+1,
                       row=grid_x,
                       padx=3,
                       pady=4 ); grid_y += 1

        grid_x += 1

        for line in table_contents:
            grid_y = 0
            for field in line:
                ttk.Label( tab,
                           text=f"{field}" )\
                   .grid( column = grid_y+1,
                          row=grid_x,
                          padx=3,
                          pady=4 ); grid_y += 1

