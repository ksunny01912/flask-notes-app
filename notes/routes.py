from flask import render_template,request,redirect
from notes import app,db
from notes.models import Todo

@app.route("/",methods=['GET', 'POST'])
def home():
    if request.method =="POST":
        title = request.form.get('title')
        desc = request.form.get('desc')
        obj = Todo(title=title, desc = desc)
        db.session.add(obj)
        db.session.commit()

    todos = Todo.query.all()
    return render_template('index.html',todos=todos)

@app.route("/delete/<int:pk>/",methods=['GET', 'POST'])
def delete(pk):
    print('delete')
    print('pk',pk)
    obj = Todo.query.filter_by(id=pk).first()
    db.session.delete(obj)
    db.session.commit()
    return redirect('/')


@app.route("/update/<int:pk>/",methods=['GET', 'POST'])
def update(pk):
    obj = Todo.query.filter_by(id=pk).first()
    if request.method =="POST":
        obj.title = request.form.get('title')
        obj.desc = request.form.get('desc')
        db.session.add(obj)
        db.session.commit()
        return redirect('/')
    todos = Todo.query.all()
    return render_template('index.html',todos=todos,title=obj.title,desc=obj.desc)