from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("database.db")

def init_db():
    conn = get_db()
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        roll TEXT,
        branch TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/save',methods=['POST'])
def save():

    name=request.form['name']
    roll=request.form['roll']
    branch=request.form['branch']

    conn=get_db()
    c=conn.cursor()

    c.execute(
        "INSERT INTO students(name,roll,branch) VALUES(?,?,?)",
        (name,roll,branch)
    )

    conn.commit()
    conn.close()

    return redirect('/students')

@app.route('/students')
def students():

    conn=get_db()
    c=conn.cursor()

    c.execute("SELECT * FROM students")

    data=c.fetchall()

    conn.close()

    return render_template("students.html",students=data)

@app.route('/delete/<int:id>')
def delete(id):

    conn=get_db()
    c=conn.cursor()

    c.execute("DELETE FROM students WHERE id=?",(id,))

    conn.commit()
    conn.close()

    return redirect('/students')

@app.route('/edit/<int:id>')
def edit(id):

    conn=get_db()
    c=conn.cursor()

    c.execute("SELECT * FROM students WHERE id=?",(id,))

    student=c.fetchone()

    conn.close()

    return render_template("edit.html",student=student)

@app.route('/update/<int:id>',methods=['POST'])
def update(id):

    name=request.form['name']
    roll=request.form['roll']
    branch=request.form['branch']

    conn=get_db()
    c=conn.cursor()

    c.execute(
        "UPDATE students SET name=?,roll=?,branch=? WHERE id=?",
        (name,roll,branch,id)
    )

    conn.commit()
    conn.close()

    return redirect('/students')

if __name__=="__main__":
    app.run(debug=True)