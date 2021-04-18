from django.core.management.base import BaseCommand

from prof_education.graduates.factories import GraduateFactory


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("dummy_num", type=int)

    def handle(self, *args, **options):
        for _ in range(0, options["dummy_num"]):
            graduate = GraduateFactory()
            self.stdout.write(self.style.SUCCESS(f'Created "{graduate}"'))
