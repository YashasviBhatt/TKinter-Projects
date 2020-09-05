Please Install MySQL on your system with "root" as both Username and Password with host set to "localhost" and execute following queries:
<br>
```CREATE DATABASE tkinter_projects;```
```USE tkinter_projects;```
```CREATE TABLE registration_login (
name CHAR(20),
registration_num VARCHAR(20),
username VARCHAR(20),
password VARCHAR(20),
email VARCHAR(50),
contact DOUBLE
);```
<br>
Now install Tkinter and mysql-python connector on python using these commands:
<br>
```pip install tkinter```
<br>
```python -m pip install mysql-connector-python```
<br>
and now Execute the program :)