import requests
from models import db, User


class UserService:
    API_URL = "https://randomuser.me/api/"

    @classmethod
    def fetch_users(cls, count=1):
        response = requests.get(f"{cls.API_URL}?results={count}")
        data = response.json()
        return data.get("results", [])

    @classmethod
    def save_users(cls, users_data):
        users = []
        for user_data in users_data:
            user = User(
                gender=user_data["gender"],
                first_name=user_data["name"]["first"],
                last_name=user_data["name"]["last"],
                phone=user_data["phone"],
                cell=user_data.get("cell", ""),  # Added cell
                email=user_data["email"],
                street=f"{user_data['location']['street']['number']} {user_data['location']['street']['name']}",
                city=user_data["location"]["city"],
                state=user_data["location"]["state"],
                country=user_data["location"]["country"],  # Added country
                postcode=str(user_data["location"]["postcode"]),
                picture_thumbnail=user_data["picture"]["thumbnail"],
                picture_large=user_data["picture"]["large"],
            )
            users.append(user)

        db.session.bulk_save_objects(users)
        db.session.commit()
        return len(users)

    @classmethod
    def get_random_user(cls):
        return User.query.order_by(db.func.random()).first()

    @classmethod
    def get_users_paginated(cls, page=1, per_page=20):
        return User.query.paginate(page=page, per_page=per_page, error_out=False)

    @classmethod
    def get_user_count(cls):
        return db.session.query(User).count()
