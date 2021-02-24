from datetime import datetime
from database import Database
from flask import Flask, stream_with_context, render_template, flash, request, Response, redirect, url_for

def stream_template(template_name, **context):
    app = Flask(__name__)
    app.update_template_context(context)
    t = app.jinja_env.get_template(template_name)
    rv = t.stream(context)
    rv.disable_buffering()
    return rv

def login():
    x = datetime.now()
    date = x.strftime("%x")
    day_name = x.strftime("%A")
    time = x.strftime("%X")
    return render_template("login.html", date = date, day_name = day_name, time = time)

def logout():
    x = datetime.now()
    date = x.strftime("%x")
    day_name = x.strftime("%A")
    time = x.strftime("%X")
    return render_template("logout.html", date = date, day_name = day_name, time = time)

def index():
    x = datetime.now()
    date = x.strftime("%x")
    day_name = x.strftime("%A")
    time = x.strftime("%X")
    return render_template("index.html", date = date, day_name = day_name, time = time)

def list_exams():

    def generate():  # our generator for list items
        db = Database()
        with db.get_cursor() as cursor:
            cursor.execute("SELECT * FROM exam;")
            rows = cursor.fetchall()
            for row in rows:
                # yield returns iterable handle of this loop
                yield {"examno": int(row[0]), "examname": str(row[1]), "noq": int(row[2])}

    ''' 
        this is just an example for 'flash' usage
        in practical usage this operation would result query twice
        for 1 listing operation
    '''
    count = sum(1 for item in generate())  # count generator
    flash("Loaded {} items from database".format(count))  # show message

    # stream with context helps us to return iterable as response
    x = datetime.now()
    date = x.strftime("%x")
    day_name = x.strftime("%A")
    time = x.strftime("%X")
    return Response(stream_with_context(stream_template("listexams.html", rows=generate(), date = date, day_name = day_name, time = time)))

def create_exam():
    if request.method == "POST":  # add exam
        exam_name = request.form["exam_name"]
        q1 = request.form["question1"]
        q2 = request.form["question2"]
        q3 = request.form["question3"]
        q4 = request.form["question4"]
        q5 = request.form["question5"]

        q1a =request.form["question1-a"]
        q1b =request.form["question1-b"]
        q1c =request.form["question1-c"]
        q1d =request.form["question1-d"]
        q1e =request.form["question1-e"]

        q2a =request.form["question2-a"]
        q2b =request.form["question2-b"]
        q2c =request.form["question2-c"]
        q2d =request.form["question2-d"]
        q2e =request.form["question2-e"]
        
        q3a =request.form["question3-a"]
        q3b =request.form["question3-b"]
        q3c =request.form["question3-c"]
        q3d =request.form["question3-d"]
        q3e =request.form["question3-e"]
        
        q4a =request.form["question4-a"]
        q4b =request.form["question4-b"]
        q4c =request.form["question4-c"]
        q4d =request.form["question4-d"]
        q4e =request.form["question4-e"]

        q5a =request.form["question5-a"]
        q5b =request.form["question5-b"]
        q5c =request.form["question5-c"]
        q5d =request.form["question5-d"]
        q5e =request.form["question5-e"]

        error = None
        if not exam_name:
            error = "Exam Name is required"
        elif not q1 :
            error = "Question 1 is required"
        elif not q2:
            error = "Question 2 is required"
        elif not q3:
            error = "Question 3 is required"
        elif not q4:
            error = "Question 4 is required"
        elif not q5:
            error = "Question 5 is required"

        if error is None:
            db = Database()
            with db.get_cursor() as cursor:
                cursor.execute("INSERT INTO exam (examname, numberofquestions) VALUES (%s, %s);", (exam_name, 5))
            db.commit()
            return redirect(url_for("list_items"))

        flash(error)

    x = datetime.now()
    date = x.strftime("%x")
    day_name = x.strftime("%A")
    time = x.strftime("%X")
    return render_template("create.html", date = date, day_name = day_name, time = time)


def home_page():
    x = datetime.now()
    date = x.strftime("%x")
    day_name = x.strftime("%A")
    time = x.strftime("%X")
    return render_template("home.html", date = date, day_name = day_name, time = time)


def movies_page():
    return render_template("movies.html")