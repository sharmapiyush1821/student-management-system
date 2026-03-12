import mysql.connector
import random

# database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="piyush1821@@@",
    database="stu_db"
)

cursor = conn.cursor()

names = [
"Aman","Rahul","Rohit","Piyush","Karan","Ankit","Suresh","Mahesh",
"Ravi","Arjun","Vikas","Deepak","Neeraj","Mohit","Tarun","Ajay"
]

courses = ["BCA","MCA","BBA","BSc","MBA"]

# 500 students insert
for i in range(500):
    name = random.choice(names)
    age = random.randint(18,25)
    course = random.choice(courses)
    marks = random.randint(50,100)

    sql = "INSERT INTO students (name, age, course, marks) VALUES (%s,%s,%s,%s)"
    val = (name, age, course, marks)

    cursor.execute(sql, val)

conn.commit()

print("500 Students Inserted Successfully")