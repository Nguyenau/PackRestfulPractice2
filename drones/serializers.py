# from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import DroneCategory, Drone, Pilot, Competition



class UserDroneSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Drone
    fields = (
        'url',
        'name')


class UserSerializer(serializers.HyperlinkedModelSerializer):
  drones = UserDroneSerializer(many=True, read_only=True)

  class Meta:
    model = User
    fields = (
        'url',
        'pk',
        'username',
        'drones')



class DroneCategorySerializer(serializers.HyperlinkedModelSerializer):
  drones = serializers.HyperlinkedRelatedField(
    many=True,
    read_only=True,
    view_name='drone-detail')

  class Meta:
    model = DroneCategory
    fields = (
      'url',
      'pk',
      'name',
      'drones')
# eg: http://127.0.0.1:8000/drone-categories/
#  {
#     "url": "http://127.0.0.1:8000/drone-categories/2/",
#     "pk": 2,
#     "name": "Octocopter",
#     "drones": [
#        "http://127.0.0.1:8000/drones/6/",
#        "http://127.0.0.1:8000/drones/4/",
#        "http://127.0.0.1:8000/drones/10/",
#        "http://127.0.0.1:8000/drones/8/"
#     ]
#  }


class DroneSerializer(serializers.HyperlinkedModelSerializer):
  owner = serializers.ReadOnlyField(source='owner.username')
  drone_category = serializers.SlugRelatedField(queryset=DroneCategory.objects.all(), slug_field='name')

	# Display the category name
	# drone_category = serializers.SlugRelatedField(queryset=DroneCategory.objects.all(), slug_field='name')
  # Display the owner's username (read-only)
  # owner = serializers.ReadOnlyField(source='owner.username')

  class Meta:
    model = Drone
    fields = ('url',
              'name',
              'drone_category',
              'owner',
              'manufacturing_date',
              'has_it_competed',
              'inserted_timestamp')
# eg: http://127.0.0.1:8000/drones/
# {
#   "url": "http://127.0.0.1:8000/drones/2/",
#   "name": "Atom",
#   "drone_category": "Quadcopter",
#   "owner": "au",
#   "manufacturing_date": "2017-11-03T01:58:49.135737Z",
#   "has_it_competed": false,
#   "inserted_timestamp": "2021-12-02T16:02:13.208689Z"
# }

class CompetitionSerializer(serializers.HyperlinkedModelSerializer):
  # display all the details for the related drone
  drone = DroneSerializer()

  class Meta:
    model = Competition
    fields = (
      'url',
      'pk',
      'distance_in_feet',
      'distance_achievement_date',
      'drone')


class PilotSerializer(serializers.HyperlinkedModelSerializer):
  competitions = CompetitionSerializer(many=True, read_only=True)
  gender = serializers.ChoiceField(choices=Pilot.GENDER_CHOICES)
  gender_description = serializers.CharField(
    source='get_gender_display',
    read_only=True)

  class Meta:
    model = Pilot
    fields = (
      'url',
      'name',
      'gender',
      'gender_description',
      'races_count',
      'inserted_timestamp',
      'competitions'
    )
# http://127.0.0.1:8000/pilots/
# {
#     "url": "http://127.0.0.1:8000/pilots/1/",
#     "name": "Penelope Pitstop",
#     "gender": "F",
#     "gender_description": "Female",
#     "races_count": 0,
#     "inserted_timestamp": "2021-12-02T18:23:37.236007Z",
#     "competitions": [
#               {
#                   "url": "http://127.0.0.1:8000/competitions/2/",
#                   "pk": 2,
#                   "distance_in_feet": 2800,
#                   "distance_achievement_date": "2017-10-21T06:03:23.776594Z",
#                   "drone": {
#                       "url": "http://127.0.0.1:8000/drones/1/",
#                       "name": "WonderDrone",
#                       "drone_category": "Quadcopter",
#                       "owner": "au",
#                       "manufacturing_date": "2017-11-03T01:58:49.135737Z",
#                       "has_it_competed": false,
#                       "inserted_timestamp": "2021-12-02T15:31:04.489152Z"
#                   }
#               },
#         {
#                   "url": "http://127.0.0.1:8000/competitions/1/",
#                   "pk": 1,
#                   "distance_in_feet": 800,
#                   "distance_achievement_date": "2017-10-20T05:03:20.776594Z",
#                   "drone": {
#                       "url": "http://127.0.0.1:8000/drones/2/",
#                       "name": "Atom",
#                       "drone_category": "Quadcopter",
#                       "owner": "au",
#                       "manufacturing_date": "2017-11-03T01:58:49.135737Z",
#                       "has_it_competed": false,
#                       "inserted_timestamp": "2021-12-02T16:02:13.208689Z"
#                   }
#               }
#     ]
# }

class PilotCompetitionSerializer(serializers.ModelSerializer):
	# Display the pilot's name
	pilot = serializers.SlugRelatedField(queryset=Pilot.objects.all(), slug_field='name')
	# Display the drone's name
	drone = serializers.SlugRelatedField(queryset=Drone.objects.all(), slug_field='name')
	
	class Meta:
		model = Competition
		fields = (
			'url',
			'pk',
			'distance_in_feet',
			'distance_achievement_date',
			'pilot',
			'drone')
# http://127.0.0.1:8000/competitions/
# {
#   "url": "http://127.0.0.1:8000/competitions/2/",
#   "pk": 2,
#   "distance_in_feet": 2800,
#   "distance_achievement_date": "2017-10-21T06:03:23.776594Z",
#   "pilot": "Penelope Pitstop",
#   "drone": "WonderDrone"
# }



