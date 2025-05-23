from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(10))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    phone = db.Column(db.String(20))
    cell = db.Column(db.String(20))
    email = db.Column(db.String(100))
    street = db.Column(db.String(100))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    country = db.Column(db.String(50))
    postcode = db.Column(db.String(20))
    picture_thumbnail = db.Column(db.String(200))
    picture_large = db.Column(db.String(200))

    def to_dict(self):
        return {
            "id": self.id,
            "gender": self.gender,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone": self.phone,
            "cell": self.cell,
            "email": self.email,
            "street": self.street,
            "city": self.city,
            "state": self.state,
            "country": self.country,
            "postcode": self.postcode,
            "picture_thumbnail": self.picture_thumbnail,
            "picture_large": self.picture_large,
        }
