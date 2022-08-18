from datetime import datetime
from notes import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    desc = db.Column(db.String(500), nullable=True)
    date_created = db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self):
        return str(self.id)+" "+self.title