from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent

#SQL LITE
SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
#RDS AWS
MYSQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sigt2-dv-db',
        'USER': 'sigt2dvroot',
        'PASSWORD': 'd4v0t3mc4l12022#',
        'HOST': 'sigt2-dv-db.cdzrbpue6b6i.us-east-1.rds.amazonaws.com',
        'PORT': '3306',
    }
}