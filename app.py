from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# db.create_all()

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    desc = db.Column(db.String(500), nullable=True)
    date_created = db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self):
        return str(self.id)+" "+self.title




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
    






if __name__ == '__main__':
    app.run(debug=True,port=8000)