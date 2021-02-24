import argparse
import os
from os import path
from database import Database
from exam import Exam
from question import Question

parser = argparse.ArgumentParser(description='App manager.')
parser.add_argument('command', metavar="cmd", type=str, help='command to manage the app')

args = parser.parse_args()


def create_database():
    db = Database()
    with db.get_cursor() as cursor:
        cursor.execute("CREATE TABLE exam (examno serial PRIMARY KEY, examname VARCHAR(50), numberofquestions INTEGER, question VARCHAR(100), a VARCHAR(100), b VARCHAR(100), c VARCHAR(100), d VARCHAR(100), e VARCHAR(100));")
        #cursor.execute("CREATE TABLE questions ( questionno serial PRIMARY KEY, examname VARCHAR(100), question VARCHAR(100), a VARCHAR(100), b VARCHAR(100), c VARCHAR(100), d VARCHAR(100), e VARCHAR(100), FOREIGN KEY (examname) REFERENCES exam (examname) ON UPDATE CASCADE ON DELETE CASCADE);")
    db.commit()
    print("Finished creating table")


def fill_database():
    db = Database()
    with db.get_cursor() as cursor:
        cursor.execute("INSERT INTO exam (examname, numberofquestions, question, a, b, c, d, e) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);", ("Cloud Exam",    5, "CloudQuestion1content",    "CloudQuestion1a",    "CloudQuestion1b",    "CloudQuestion1c",    "CloudQuestion1d",    "CloudQuestion1e"))
        cursor.execute("INSERT INTO exam (examname, numberofquestions, question, a, b, c, d, e) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);", ("Database Exam", 5, "DatabaseQuestion1content", "DatabaseQuestion1a", "DatabaseQuestion1b", "DatabaseQuestion1c", "DatabaseQuestion1d", "DatabaseQuestion1e"))
        cursor.execute("INSERT INTO exam (examname, numberofquestions, question, a, b, c, d, e) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);", ("Software Exam", 5, "SoftwareQuestion1content", "SoftwareQuestion1a", "SoftwareQuestion1b", "SoftwareQuestion1c", "SoftwareQuestion1d", "SoftwareQuestion1e"))
        
        '''
        cursor.execute("INSERT INTO questions (examname, question, a, b, c, d, e) VALUES (%s, %s, %s, %s, %s, %s, %s);", ("Cloud Exam", "CloudQuestion1content", "CloudQuestion1a", "CloudQuestion1b", "CloudQuestion1c", "CloudQuestion1d", "CloudQuestion1e"))
        cursor.execute("INSERT INTO questions (examname, question, a, b, c, d, e) VALUES (%s, %s, %s, %s, %s, %s, %s);", ("Cloud Exam", "CloudQuestion2content", "CloudQuestion2a", "CloudQuestion2b", "CloudQuestion2c", "CloudQuestion2d", "CloudQuestion2e"))
        cursor.execute("INSERT INTO questions (examname, question, a, b, c, d, e) VALUES (%s, %s, %s, %s, %s, %s, %s);", ("Cloud Exam", "CloudQuestion3content", "CloudQuestion3a", "CloudQuestion3b", "CloudQuestion3c", "CloudQuestion3d", "CloudQuestion3e"))
        cursor.execute("INSERT INTO questions (examname, question, a, b, c, d, e) VALUES (%s, %s, %s, %s, %s, %s, %s);", ("Cloud Exam", "CloudQuestion4content", "CloudQuestion4a", "CloudQuestion4b", "CloudQuestion4c", "CloudQuestion4d", "CloudQuestion4e"))
        cursor.execute("INSERT INTO questions (examname, question, a, b, c, d, e) VALUES (%s, %s, %s, %s, %s, %s, %s);", ("Cloud Exam", "CloudQuestion5content", "CloudQuestion5a", "CloudQuestion5b", "CloudQuestion5c", "CloudQuestion5d", "CloudQuestion5e"))

        cursor.execute("INSERT INTO questions (examname, question, a, b, c, d, e) VALUES (%s, %s, %s, %s, %s, %s, %s);", ("Database Exam", "DatabaseQuestion1content", "DatabaseQuestion1a", "DatabaseQuestion1b", "DatabaseQuestion1c", "DatabaseQuestion1d", "DatabaseQuestion1e"))
        cursor.execute("INSERT INTO questions (examname, question, a, b, c, d, e) VALUES (%s, %s, %s, %s, %s, %s, %s);", ("Database Exam", "DatabaseQuestion2content", "DatabaseQuestion2a", "DatabaseQuestion2b", "DatabaseQuestion2c", "DatabaseQuestion2d", "DatabaseQuestion2e"))
        cursor.execute("INSERT INTO questions (examname, question, a, b, c, d, e) VALUES (%s, %s, %s, %s, %s, %s, %s);", ("Database Exam", "DatabaseQuestion3content", "DatabaseQuestion3a", "DatabaseQuestion3b", "DatabaseQuestion3c", "DatabaseQuestion3d", "DatabaseQuestion3e"))
        cursor.execute("INSERT INTO questions (examname, question, a, b, c, d, e) VALUES (%s, %s, %s, %s, %s, %s, %s);", ("Database Exam", "DatabaseQuestion4content", "DatabaseQuestion4a", "DatabaseQuestion4b", "DatabaseQuestion4c", "DatabaseQuestion4d", "DatabaseQuestion4e"))
        cursor.execute("INSERT INTO questions (examname, question, a, b, c, d, e) VALUES (%s, %s, %s, %s, %s, %s, %s);", ("Database Exam", "DatabaseQuestion5content", "DatabaseQuestion5a", "DatabaseQuestion5b", "DatabaseQuestion5c", "DatabaseQuestion5d", "DatabaseQuestion5e"))
    
        cursor.execute("INSERT INTO questions (examname, question, a, b, c, d, e) VALUES (%s, %s, %s, %s, %s, %s, %s);", ("Software Exam", "SoftwareQuestion1content", "SoftwareQuestion1a", "SoftwareQuestion1b", "SoftwareQuestion1c", "SoftwareQuestion1d", "SoftwareQuestion1e"))
        cursor.execute("INSERT INTO questions (examname, question, a, b, c, d, e) VALUES (%s, %s, %s, %s, %s, %s, %s);", ("Software Exam", "SoftwareQuestion2content", "SoftwareQuestion2a", "SoftwareQuestion2b", "SoftwareQuestion2c", "SoftwareQuestion2d", "SoftwareQuestion2e"))
        cursor.execute("INSERT INTO questions (examname, question, a, b, c, d, e) VALUES (%s, %s, %s, %s, %s, %s, %s);", ("Software Exam", "SoftwareQuestion3content", "SoftwareQuestion3a", "SoftwareQuestion3b", "SoftwareQuestion3c", "SoftwareQuestion3d", "SoftwareQuestion3e"))
        cursor.execute("INSERT INTO questions (examname, question, a, b, c, d, e) VALUES (%s, %s, %s, %s, %s, %s, %s);", ("Software Exam", "SoftwareQuestion4content", "SoftwareQuestion4a", "SoftwareQuestion4b", "SoftwareQuestion4c", "SoftwareQuestion4d", "SoftwareQuestion4e"))
        cursor.execute("INSERT INTO questions (examname, question, a, b, c, d, e) VALUES (%s, %s, %s, %s, %s, %s, %s);", ("Software Exam", "SoftwareQuestion5content", "SoftwareQuestion5a", "SoftwareQuestion5b", "SoftwareQuestion5c", "SoftwareQuestion5d", "SoftwareQuestion5e"))
        '''
    db.commit()
    print("3 ders tablosu eklendi.")


def drop_database():
    db = Database()
    with db.get_cursor() as cursor:
        cursor.execute("DROP TABLE IF EXISTS exam;")
    db.commit()
    print("Finished dropping tables")


if args.command == "init":
    if path.exists("initialized.txt"):
        print("This project already initialized")
    else:
        try:
            create_database()
            fill_database()
            open("initialized.txt", "w+")
            print("project initialized")
        except Exception as inst:
            print("cannot initialize project: " + str(inst))

elif args.command == "destroy":
    drop_database()
    if path.exists("initialized.txt"):
        os.remove("initialized.txt")

def add_exam(self, exam):
    self._last_exam_key += 1
    self.exams[self._last_exam_key] = exam
    return self._last_exam_key

def delete_exam(self, exam_key):
        if exam_key in self.exams:
            del self.exams[exam_key]

def get_exam(self, exam_key):
    exam = self.exams.get(exam_key)
    if exam is None:
        return None
    exam_ = Exam(exam.exam_name, numberofquestions=exam.numberofquestions, question=exam.question, a=exam.a, b=exam.b, c=exam.c, d=exam.d, e=exam.e )
    return exam_

def get_exams(self):
    exams = []
    for exam_key, exam in self.exams.items():
        exam_ = Exam(exam.exam_name, numberofquestions=exam.numberofquestions, question=exam.question, a=exam.a, b=exam.b, c=exam.c, d=exam.d, e=exam.e )
        exams.append((exam_key, exam_))
    return exams