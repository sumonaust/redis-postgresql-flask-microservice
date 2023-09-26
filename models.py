from app import db


class Students(db.Model):
    __tablename__ = "poridhian"
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    data = db.Column(db.Text)

    def __init__(self, data):
        self.data = data