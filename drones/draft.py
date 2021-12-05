http POST :8000/drone-categories/ name="Quadcopter"



http POST :8000/drones/ name="WonderDrone" drone_category="Quadcopter" manufacturing_date="2017-11-03T01:58:49.135737Z" has_it_competed=False 

# create a new user
python manage.py shell
from django.contrib.auth.models import User
user = User.objects.create_user('au2', 'no@gmail.com', 'password')
user.save()


# connect to Postgresql database
psql - U username - h 127.0.0.1 drones

\x  to expand view (in Postgresql)



# how to get token
python manage.py shell
from rest_framework.authtoken.models  import Token
from django.contrib.auth.models import User

user = User.objects.get(username='au2')
token = Token.objects.create(user=user)
print(token)
#sample token for 'au2'
735b8f9fd1731fe5209304a5258de0a249c73e31
quit()



