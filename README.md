# Element_Table  

by Alexander Nazimov

## Introduction

The Periodic Table of Elements application is based on the "kivy" GUI library.

The application consists of two parts: a field for displaying information and the table itself, which is made in the form 
of buttons that send a query to the database and display information about the element on the screen.

The database is based on the built-in sqlite3 library.

## Implemented features

SQLite was used as database. Package SQL contains 4 files with functions which create tables, add information to DB and 
select information from DB.  
All element's information (raw info) is in Periodic_new.csv file.  
  
Directory info contains information for kivy app like fonts or belonging to the element category.
Also in screen_info implemented functions for simple adaptability (based on screen resolution).  
  
GUI package contains kivy app.  
All elements is interactive buttons, pushing on button update information about chemical element.  

Used libs:  
Kivy v2.1.0  
screeninfo v.0.8.1  
setuptools v.65.6.3  
