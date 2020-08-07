from django.core.management.base import BaseCommand
from user.models import CustomUser, Activity
from datetime import timedelta
from django.db import connection
from django.utils.timezone import now


class Command(BaseCommand):

    def handle(self, *args, **options):
        cursor = connection.cursor()
        cursor.execute("PRAGMA foreign_keys = OFF;")
        cursor.execute("delete from users")
        cursor.execute("delete from user_activity")
        cursor.execute("PRAGMA foreign_keys = ON;")
        current_time = now()
        user_data = [
            {
                "first_name": "Egon",
                "last_name": "Spengler",
                "email": "test@gmail.com",
                "username": "test@gmail.com",
                "password": "test"
            },
            {
                "first_name": "Glinda",
                "last_name": "Southgood",
                "email": "test1@gmail.com",
                "username": "test1@gmail.com",
                "password": "test1"
            }
        ]
        for data in user_data:
            self.stdout.write(self.style.WARNING(f"Creating New User {data['first_name']}"))
            new_user = CustomUser.objects.create_user(username=data["username"], email=data["email"],
                                                      password=data["password"], first_name=data["first_name"],
                                                      last_name=data["last_name"])
            user_activity_data = []
            for i in range(0, 2):
                user_activity_data.append(Activity(user=new_user, start_time=current_time - timedelta(hours=i * 2 + 2),
                                                   end_time=current_time - timedelta(hours=i * 2)))
            Activity.objects.bulk_create(user_activity_data)
            api_key = CustomUser.objects.generate_api_key(user_id=new_user.pk)
            self.stdout.write(self.style.SUCCESS(f"Successfully Created User with ID: {new_user.pk} and API_Key: "
                                                 f"{api_key}"))
