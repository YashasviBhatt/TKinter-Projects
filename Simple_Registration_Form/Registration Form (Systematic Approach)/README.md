Please Install MySQL on your system with "root" as both Username and Password with host set to "localhost" and execute following queries:

CREATE DATABASE tkinter_projects;
USE tkinter_projects;
CREATE TABLE registration (name char(20), city char(20), reg_num int, nationality char(20));

Now install Tkinter and mysql-python connector on python using these commands:
pip install tkinter
python -m pip install mysql-connector-python

and now Execute the program :)