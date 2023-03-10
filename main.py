import csv
from peewee import *


# db = PostgresqlDatabase(database ='DB_NAME'), user = config('DB_USERNAME'),
#                         password = config('PASSWORD', host = config('DB_HOST')
db = PostgresqlDatabase(database='lab_parsing', user='bermet',
                        password='1', host='localhost')


class Apartments(Model):
    # id = Column(IntegerField, primary_key = True)
    price = CharField()
    date = TextField()
    image = TextField()

    class Meta:
        database = db


def main():
    db.connect()
    db.create_tables([Apartments])
    with open ('Apart.file') as f:
        order = ['price', 'date', 'image']
        reader = csv.DictReader(f, fieldnames=order)
        apartments = list(reader)
        with db.atomic():
            for row in apartments:
                Apartments.create(**row)


if __name__ == '__main__':
    main()




