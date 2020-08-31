from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

db.create_all()

from libbler.views import receive_events, get_events

@manager.option('-e', '--event', dest='content', default='I just won a lottery #update @all')
def create_events(content):
    receive_events(content)

@manager.option('-c', '--category', dest='category')
@manager.option('-p', '--person', dest='person')
@manager.option('-a', '--amount', dest='amount', default=10)
def get_events(category, person, amount):
    if category:
        print(get_events(category=category, amount=int(amount)))
    elif person:
        print(get_events(person=person, amount=int(amount)))
    else:
        print(get_events(amount=int(amount)))
