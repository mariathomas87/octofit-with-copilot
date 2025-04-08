from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Verify test data in the database'

    def handle(self, *args, **kwargs):
        # Check if test data exists for each model
        user_count = User.objects.count()
        team_count = Team.objects.count()
        activity_count = Activity.objects.count()
        leaderboard_count = Leaderboard.objects.count()
        workout_count = Workout.objects.count()

        self.stdout.write(f"Users: {user_count}")
        self.stdout.write(f"Teams: {team_count}")
        self.stdout.write(f"Activities: {activity_count}")
        self.stdout.write(f"Leaderboards: {leaderboard_count}")
        self.stdout.write(f"Workouts: {workout_count}")