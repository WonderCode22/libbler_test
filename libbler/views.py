from .models import Events, db


def receive_events(content):
    event = Events(content)
    db.session.add(event)
    db.session.commit()

def get_events(**kwargs):
    if 'amount' in kwargs:
        amount = kwargs['amount']
    else:
        amount = 10

    if 'category' in kwargs:
        events = Events.query.filter_by(category=kwargs['category']).order_by(Events.created_at)[-amount:]
    elif 'person' in kwargs:
        events = Events.query.filter_by(person=kwargs['person']).order_by(Events.created_at)[-amount:]
    else:
        events = Events.query.order_by(Events.created_at)[-amount:]

    return events