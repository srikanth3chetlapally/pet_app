from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(100), nullable=False)
    breed = db.Column(db.String(100), nullable=True)  # Added breed for a different design

    def __repr__(self):
        return f'<Pet {self.name}>'
