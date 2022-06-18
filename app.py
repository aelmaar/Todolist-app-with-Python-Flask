from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/test.db'
db = SQLAlchemy(app)

# creating the model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(120), nullable=False)

    def __repr__(self) -> str:
        return '<Task %r' % self.id

# this is the default route, where we will add tasks
@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        get_task = request.form.get("task")
        # we have to make sure that the user provide us a value
        # in order to store it
        if get_task:
            db.session.add(Task(task=get_task))
            db.session.commit()
        return redirect('/')
    else:
        tasks = db.session.query(Task).all()
        return render_template('index.html', tasks=tasks)


# delete a task
@app.route('/delete/<int:id>')
def delete(id):
    db.session.query(Task).filter(Task.id == id).delete(synchronize_session=False)
    db.session.commit()
    return redirect('/')

# update the task
@app.route('/update/<int:id>', methods=["POST", "GET"])
def update(id):
    if request.method == "POST":
        get_task = request.form.get("task")
        if get_task:
            db.session.query(Task).filter(Task.id == id).update({Task.task: get_task})
            db.session.commit()
            return redirect('/')
    else:
        return render_template('update.html', id=id)
