import os
import sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blood_bank_project.settings')


import django
django.setup()

from django.contrib.auth.models import User
from donor_app.models import Donor
from region_app.models import County
from random import choice, randint
from django_seed import Seed
from django.db.models import Q


if len(sys.argv) != 3:
    print("Bye!")
    exit()

command = sys.argv[1]
try:
    number = int(sys.argv[2])
except:
    number = 10

if command == 'user':
    seeder = Seed.seeder()
    seeder.add_entity(User, number)
    inserted_pks = seeder.execute()
    exit()
elif command == 'donor':


    county = list(map(lambda x: x, County.objects.all()))
    # for user_id in inserted_pks[User]:
    users = list(map(lambda x: x, User.objects.filter(~Q(username='elshad'))))

    for user in users:
        seeder = Seed.seeder()
        seeder.add_entity(Donor, 1, {
            'user': user,
            'gender': randint(1,2),
            'blood_group': choice(list(Donor.bgroup_choices.keys())),
            'county': choice(county),
            'blood_price_per_100gramm': randint(0, 100)
        })

        try:
            seeder.execute()
        except Exception as err:
            print(err)