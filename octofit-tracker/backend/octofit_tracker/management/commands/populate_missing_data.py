from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate missing test data for Leaderboards and Workouts'

    def handle(self, *args, **kwargs):
        # Populate Leaderboards
        if Leaderboard.objects.count() == 0:
            team1, created1 = Team.objects.get_or_create(name='Blue Team', defaults={'_id': ObjectId()})
            team2, created2 = Team.objects.get_or_create(name='Gold Team', defaults={'_id': ObjectId()})

            Leaderboard.objects.bulk_create([
                Leaderboard(_id=ObjectId(), team=team1, points=100),
                Leaderboard(_id=ObjectId(), team=team2, points=90),
            ])
            self.stdout.write('Leaderboards populated successfully.')

        # Populate Workouts
        if Workout.objects.count() == 0:
            workouts = [
                Workout(_id=ObjectId(), name='Cycling Training', description='Training for a road cycling event', duration=60),
                Workout(_id=ObjectId(), name='Crossfit', description='Training for a crossfit competition', duration=120),
                Workout(_id=ObjectId(), name='Running Training', description='Training for a marathon', duration=90),
                Workout(_id=ObjectId(), name='Strength Training', description='Training for strength', duration=30),
                Workout(_id=ObjectId(), name='Swimming Training', description='Training for a swimming competition', duration=75),
            ]
            Workout.objects.bulk_create(workouts)
            self.stdout.write('Workouts populated successfully.')