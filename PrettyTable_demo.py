#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     :usage of PrettyTable
@Date     :2021/04/28 10:31:23
@Author      :xbMa
'''

from prettytable import PrettyTable

############################
# Init a table
x = PrettyTable()
x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]

print("\nThis is a origin table:")
x.add_row(["Adelaide", 1295, 1158259, 600.5])
x.add_row(["Brisbane", 5905, 1857594, 1146.4])
x.add_row(["Darwin", 112, 120900, 1714.7])
x.add_row(["Hobart", 1357, 205556, 619.5])
x.add_row(["Sydney", 2058, 4336374, 1214.8])
x.add_row(["Melbourne", 1566, 3806092, 646.9])
x.add_row(["Perth", 5386, 1554769, 869.4])
print(x)

############################
# Delete a row 
print("\nDelete a row of index 0:")
x.del_row(0)
print(x)

############################
# Data Sort
print("\nTable sorted by population of is True:")
x.sortby = "Population"
x.reversesort = True
print(x)

print("\nTable sorted by population of is False:")
x.sortby = "Population"
x.reversesort = False
print(x)

# Algin with left right center
print("\nTable algin, [City name] is left, [Area] is right, Default is center:")
x.align["City name"] = "l"
x.align["Area"] = "r"
x.align["Annual Rainfall"] = "r"
print(x)

############################
# Set a title
print("\nTable with title:")
x.title = "Australian cities"
print(x)
# print(x.get_string(title="Australian cities"))

############################
# Choice print rows
print("\nTable print start 2 and end 5 rows:")
x.start = 2
x.end = 5
print(x)
# print(x.get_string(start=1, end=4))

############################
# Clear all rows
print("\nClear all rows, retain filed name")
x.clear_rows()
print(x)

############################
# From csv read 
'''
from prettytable import from_csv
with open("data.csv", "r") as fp: 
    x = from_csv(fp)
'''

############################
# From sql read
'''
import sqlite3 as lite
from prettytable import from_db_cursor

con = lite.connect('data.db')

with con:

    cur = con.cursor()    
    cur.execute('SELECT * FROM Cities')   

    x = from_db_cursor(cur) 
'''

############################
# From html 
'''
from prettytable import from_html_one

with open("data.html", "r") as fp: 
    html = fp.read()

x = from_html_one(html)
'''
