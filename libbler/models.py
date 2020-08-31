from app import db
from datetime import datetime

class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(10), nullable=True)
    person = db.Column(db.String(10), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return '<Event: %r>' % self.description

    def __init__(self, str, **kwargs):
        super(Events, self).__init__(**kwargs)
        self.description = str.split('#')[0].rstrip()
        self.category = str.split('#')[1].split('@')[0].rstrip()
        self.person = str.split('@')[1]