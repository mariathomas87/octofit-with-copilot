from djongo import models
from bson import ObjectId

class ObjectIdField(models.Field):
    def get_prep_value(self, value):
        if not value:
            return str(ObjectId())  # Generate a new ObjectId if value is empty or None
        if isinstance(value, ObjectId):
            return str(value)
        return value

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return ObjectId(value)

class User(models.Model):
    _id = ObjectIdField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class Team(models.Model):
    _id = ObjectIdField(primary_key=True)
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User)

class Activity(models.Model):
    _id = ObjectIdField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=255)
    duration = models.IntegerField()
    date = models.DateField()

class Leaderboard(models.Model):
    _id = ObjectIdField(primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()

class Workout(models.Model):
    _id = ObjectIdField(primary_key=True)  # Add _id field
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()