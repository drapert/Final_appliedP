import sqlite3

db = sqlite3.connect('assignment2.db')
cursor = db.cursor()
cursor.execute('drop table if exists STUDENT')
cursor.execute('drop table if exists INSTRUCTOR')
cursor.execute('drop table if exists ADMIN')
cursor.execute('drop table if exists COURSE')

# Create student table
command = """CREATE TABLE STUDENT(
ID 		INT 	PRIMARY KEY 	NOT NULL,
PASS        TEXT    NOT NULL,
FNAME        TEXT    NOT NULL,
LNAME		TEXT 	NOT NULL,
GRADYEAR	INT 	NOT NULL,
MAJOR		CHAR(4) NOT NULL,
EMAIL		text	NOT NULL, 
COURSES     TEXT)
;"""
cursor.execute(command) # Add student table

# Student values
cursor.execute("""INSERT INTO STUDENT VALUES(1111, '1', 'Connor', 'Adams', 2023, 'BSCS', 'adamsc', '');""") 
cursor.execute("""INSERT INTO STUDENT VALUES(1112,'1', 'Drew', 'Hesse', 2022, 'BSCE', 'hessea', '');""") 
cursor.execute("""INSERT INTO STUDENT VALUES(1113, '1', 'Ryan', 'Murray', 2021, 'BSME', 'murrayr', '');""") 
cursor.execute("""INSERT INTO STUDENT VALUES(1114, '1', 'Seth', 'Bannish', 2018, 'BSEE', 'bannishs', '');""") 
cursor.execute("""INSERT INTO STUDENT VALUES(1115, '1', 'Paige', 'Murphy', 2015, 'BCSS', 'murphyp', '');""") 
cursor.execute("""INSERT INTO STUDENT VALUES(1116, '1', 'Riley', 'Lynch', 2012, 'BSAB', 'lynchr', '');""") 
cursor.execute("""INSERT INTO STUDENT VALUES(1117, '1','Drew', 'Potter', 2026, 'BSDA', 'potterd', '');""") 
cursor.execute("""INSERT INTO STUDENT VALUES(1118, '1','Mackenzie', 'Morrison', 2025, 'BSCB', 'morrisonm', '');""") 
cursor.execute("""INSERT INTO STUDENT VALUES(1119, '1','Ryan', 'Love', 2019, 'BSFP', 'lover', '');""") 
cursor.execute("""INSERT INTO STUDENT VALUES(1120, '1','Jordan', 'Johnny', 1918, 'BCOS', 'jordanj', '');""") 
cursor.execute("""insert into STUDENT values(1121, '1', 'Phoenix', 'Stebbins', 2022, 'BSCO', 'stebbinsp', '');""")
cursor.execute("""insert into STUDENT values(1122, '1', 'MisteR', 'Peanut', 2013, 'NUTT', 'misterp', '');""")

# Create instructor table
command = """CREATE TABLE INSTRUCTOR (  
ID 		    INT 	PRIMARY KEY 	NOT NULL,
PASS        TEXT    NOT NULL,
FNAME		TEXT	NOT NULL,
LNAME		TEXT 	NOT NULL,
TITLE		TEXT 	NOT NULL,
DEPT		CHAR(4) NOT NULL,
EMAIL		text	NOT NULL,
YEAR	INT 	NOT NULL,
COURSES     TEXT)
;"""
cursor.execute(command) # Add instructor table

# Instructor values
cursor.execute("""INSERT INTO INSTRUCTOR VALUES(2111, '1', 'Andrew', 'Wise', 'Full Prof.', 1996, 'BSCT', 'wisea', '');""") 
cursor.execute("""INSERT INTO INSTRUCTOR VALUES(2112, '1', 'Craig', 'Douty', 'Full Prof.', 1984, 'BAAA', 'doutyc', '');""") 
cursor.execute("""INSERT INTO INSTRUCTOR VALUES(2113, '1', 'Jeff', 'Sweigard', 'Full Prof.', 1970, 'BOWC', 'sweigardj', '');""") 
cursor.execute("""INSERT INTO INSTRUCTOR VALUES(2114, '1', 'Rob', 'Quinlan', 'Associate Prof.', 2020, 'BSAP', 'quinlanr', '');""") 
cursor.execute("""INSERT INTO INSTRUCTOR VALUES(2115, '1', 'Tarra', 'Marchetti', 'Assistant Prof.', 2010, 'BCOS', 'marchettit', '');""") 
cursor.execute("""INSERT INTO INSTRUCTOR VALUES(2116, '1', 'Dorian', 'Mandinova', 'Associate Prof.', 1980, 'BSBE', 'mandinovad', '');""")


# Create admin table
command =  """CREATE TABLE ADMIN (  
ID 		INT 	PRIMARY KEY 	NOT NULL,
PASS        TEXT    NOT NULL,
FNAME		TEXT	NOT NULL,
LNAME		TEXT 	NOT NULL,
TITLE		TEXT 	NOT NULL,
EMAIL		TEXT	NOT NULL,
OFFICE		TEXT 	NOT NULL)
;"""
cursor.execute(command) 
# Add admin table

# Admin values
cursor.execute("""INSERT INTO ADMIN VALUES(3111,'1', 'Barack', 'Obama', 'Past President', 'obamab', 'Dobbs 1600');""") 
cursor.execute("""INSERT INTO ADMIN VALUES(3112, '1','Joe', 'Biden', 'President', 'bidenj', 'Wentworth 101');""") 

# Create course table
command = """CREATE TABLE COURSE(
                    TITLE           varchar (30)    not null,
                    CRN             char(10)        not null    primary key,
                    DEPARTMENT      varchar(20)     not null,
                    INSTRUCTOR      varchar(30)     not null,
                    START_TIME      int(4)         not null,
                    END_TIME        int(4)         not null,
                    DAYS_OF_WEEK    varchar(5)      not null,
                    SEMESTER        char(3)         not null,
                    YEAR            int(4)          not null,
                    CREDITS         int(1)          not null,
                    STUDENT_LIST    TEXT 
                ); """
    
cursor.execute(command) # Add course table

# Add courses
cursor.execute("""insert into COURSE values("Embedded Sensor Networks", 4050, "ELEC", "Douglas Dow", 1500, 1650, 'M W', 'SUM', 2021, 4, '')""")
cursor.execute("""insert into COURSE values("Signals & Systems", 3650, "ELEC", "Suarav Basnet", 1000, 1150, 'M W', 'SUM', 2021, 4, '')""")
cursor.execute("""insert into COURSE values("Advanced Digital Circuit Design", 4100, "ELEC", "Pilin Junsangsri", 1000, 1150, 'F', 'SUM', 2021, 4, '')""")
cursor.execute("""insert into COURSE values("Applied Programming Concepts", 3750, "ELEC", "Bruce Decker", 1300, 1450, 'W', 'SUM', 2021, 4, '')""")
cursor.execute("""insert into COURSE values("Computer Networks", 3700, "ELEC", "Wayne Bynoe", 1300, 1450, 'F', 'SUM', 2021, 4, '')""")

db.commit()
db.close()
