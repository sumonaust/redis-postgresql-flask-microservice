from app import db
from models import Students
from app import redis_db


def inserting(data):
    variable = Students(data)
    db.session.add(variable)
    db.session.commit()
    return variable

def getData():
    results = Students.query.all()
    return results

def setRedisCache(data):
    redis_db.set("key", data)
    return

def getRedisCache():
    value = redis_db.get('key')
    return value

def delRedisCache():
    redis_db.delete('key')
    return