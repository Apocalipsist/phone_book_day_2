from app import db
from datetime import datetime

class Address_Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(128), nullable=False, unique=True)
    last_name = db.Column(db.String(128), nullable=False,)
    phone_number = db.Column(db.String(128), nullable=False,)
    home_address = db.Column(db.String(128), nullable=False,)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __init__(self,**kwargs) -> None:
        super().__init__(**kwargs)
        db.session.add(self)
        db.session.commit()
    
    def __str__(self) -> str:
        return self.first_name +  " " + self.last_name