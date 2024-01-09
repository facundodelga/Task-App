from flask import Flask, render_template, request, redirect, url_for
from Models import Tasks,db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database///tasks.db"
db.init_app(app)

@app.route('/')
def index():
    tasks = Tasks.query.all()
    return render_template("index.html", tasks = tasks)

@app.route('/create-task', methods=['POST'])
def create():
    task = Tasks(task=request.form['task'])
    db.session.add(task)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/done-task/<rowid>') 
def done(rowid):
    task = Tasks.query.filter_by(rowid=int(rowid)).first()
    task.done = not(task.done)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete-task/<rowid>')
def delete(rowid):
    Tasks.query.filter_by(rowid=int(rowid)).delete()
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True, port=4000)
