import sqlite3
from flask import Flask, render_template, request, g, redirect

app = Flask(__name__)

DATABASE_FILE = 'database.db'

# Get a useable connection to the database
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE_FILE)
        db.row_factory = sqlite3.Row
    return db

# Close the database connection when the app shuts down
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# return the results from a database query
def db_query(query, args=()):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return rv

# execute a database query
def db_execute(script):
    conn = get_db()
    conn.executescript(script)
    conn.commit()
    conn.close()
    return True

def get_scores_from_db(student_id):
    query = f"""
SELECT assignment_scores.score, assignments.name, assignments.points
FROM assignment_scores
JOIN assignments ON assignments.id = assignment_scores.assignment_id
WHERE assignment_scores.student_id = {student_id};
"""
    return db_query(query)

def get_student_from_db(student_id):
    results = db_query(f"SELECT * FROM students WHERE id = {student_id}")
    if results:
        return results[0]
    else:
        return None

def get_students_from_db():
    return db_query("SELECT * FROM students")

def update_student_name(student_id, name):
    query = f"""
UPDATE students
SET name = '{name}'
WHERE students.id = {student_id};
"""
    return db_execute(query)

@app.get('/')
def index():
    students = get_students_from_db()
    return render_template('students.html', students=students)

@app.get('/scores/<student_id>')
def student_scores(student_id):
    student = get_student_from_db(student_id)
    scores = get_scores_from_db(student_id)
    return render_template("scores.html", student=student, scores=scores)

@app.get('/change_name')
def change_name():
    student_id = request.args.get('student_id')
    name = request.args.get('name')
    update_student_name(student_id, name)
    return redirect(f'/')
