import csv
import sqlite3

from SQL.create_tables import create_table
from SQL.add_info import add_info

with open("Periodic_new.csv") as f:
    rows = csv.reader(f, delimiter=",")
    elements = list(rows)
    for element in elements:
        element.pop(0)

with sqlite3.connect('PeriodicTable.db') as db:
    curr = db.cursor()

    create_table(curr)
    for element in elements:
        add_info(curr, AN=element[0], E=element[1],
                 S=element[2], AM=element[3],
                 P=element[4], D=element[5],
                 Y=element[6], NOS=element[7])
