Please Install MySQL on your system with "root" as both Username and Password with host set to "localhost" and execute following queries:

CREATE DATABASE tkinter_projects;
USE tkinter_projects;
CREATE TABLE simple_registration (name char(20), city char(20), reg_num int, nationality char(20));
SELECT * FROM simple_registration;