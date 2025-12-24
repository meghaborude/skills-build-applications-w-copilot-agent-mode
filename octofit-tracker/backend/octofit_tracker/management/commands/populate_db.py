from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team='Marvel')
        captain = User.objects.create(name='Captain America', email='cap@marvel.com', team='Marvel')
        batman = User.objects.create(name='Batman', email='batman@dc.com', team='DC')
        superman = User.objects.create(name='Superman', email='superman@dc.com', team='DC')

        # Create Activities
        Activity.objects.create(user='Iron Man', activity='Run', duration=30)
        Activity.objects.create(user='Captain America', activity='Swim', duration=45)
        Activity.objects.create(user='Batman', activity='Bike', duration=60)
        Activity.objects.create(user='Superman', activity='Yoga', duration=20)

        # Create Workouts
        Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes')
        Workout.objects.create(name='Strength Training', description='Strength for all heroes')

        # Create Leaderboard
        Leaderboard.objects.create(user='Iron Man', points=100)
        Leaderboard.objects.create(user='Captain America', points=90)
        Leaderboard.objects.create(user='Batman', points=95)
        Leaderboard.objects.create(user='Superman', points=85)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
