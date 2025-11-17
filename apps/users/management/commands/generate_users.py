from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils import timezone

from faker import Faker
import random
from datetime import datetime


User = get_user_model()


class Command(BaseCommand):
    help = "Generate 10,000 fake CustomUser records"

    def handle(self, *args, **options):
        fake = Faker()

        total_users = 10000
        batch_size = 1000

        departments = [
            "IT",
            "HR",
            "Finance",
            "Sales"
        ]

        roles = [
            "admin",
            "manager",
            "employee",
        ]

        dummy_user = User()
        dummy_user.set_password("12345")
        hashed_password = dummy_user.password

        self.stdout.write(self.style.NOTICE("Generating users..."))

        users_batch = []
        created_count = 0

        for i in range(total_users):

            birth_date = fake.date_between(
                start_date=datetime(1975, 1, 1),
                end_date=datetime(2005, 12, 31)
            )

            user = User(
                email=fake.unique.email(),
                username=fake.unique.user_name(),

                first_name=fake.first_name(),
                last_name=fake.last_name(),

                phone=fake.phone_number(),
                city=fake.city(),
                country=fake.country(),

                department=random.choice(departments),
                role=random.choice(roles),

                salary=random.randint(500, 5000),

                birth_date=birth_date,
                password=hashed_password,
                is_active=True,
                is_staff=False,
            )

            users_batch.append(user)

            if len(users_batch) >= batch_size:
                User.objects.bulk_create(users_batch, batch_size=batch_size)
                created_count += len(users_batch)
                self.stdout.write(f"Inserted {created_count} users...")
                users_batch = []

        if users_batch:
            User.objects.bulk_create(users_batch, batch_size=batch_size)
            created_count += len(users_batch)

        self.stdout.write(self.style.SUCCESS(f"Done! Created {created_count} users."))
