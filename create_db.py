from models import base_class, Catalog, Choice
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from os import getenv
import json

engine = create_engine(getenv('db_uri'))
base_class.metadata.create_all(engine)
session_class = sessionmaker(bind=engine)
session = session_class()

with open('catalog_fixtures.json', 'r') as json_file:
    catalog = json.load(json_file)

for item in catalog:
    new_item = Catalog(
        **{'title': item['title'], 'description': item['description']})
    for choice in item['choices']:
        choices = Choice(
            **{'title': choice['title'], 'price': choice['price']})
        new_item.choices.append(choices)
    session.add(new_item)
session.commit()
