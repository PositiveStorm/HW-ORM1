import csv
from slugify import slugify

from django.core.management.base import BaseCommand
from ormhw.models import Element


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))


        for phone in phones:
            Element.objects.create(
                id=phone['id'],
                name=phone['name'],
                image=phone['image'],
                price=phone['price'],
                release_date=phone['release_date'],
                lte_exists=phone['lte_exists'],
                slug=slugify(phone['name'])
            )


