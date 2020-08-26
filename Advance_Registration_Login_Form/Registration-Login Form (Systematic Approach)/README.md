Please Install MySQL on your system with "root" as both Username and Password with host set to "localhost" and execute following queries:

CREATE DATABASE tkinter_projects;
USE tkinter_projects;
CREATE TABLE registration_login (
name CHAR(20),
registration_num VARCHAR(20),
username VARCHAR(20),
password VARCHAR(20),
email VARCHAR(50),
contact DOUBLE
);

Now install Tkinter and mysql-python connector on python using these commands:
pip install tkinter
python -m pip install mysql-connector-python

and now Execute the program :)