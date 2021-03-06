
# -*- coding: utf-8 -*-
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','artbud_project.settings')

import django
django.setup()

from artbud.models import Upload
from django.contrib.auth.models import User

def populate():
	
	photography = [
		{'name': 'CarInDamascus','user': 'Jack96', 'picture': 'images/photography/car.jpg', 'price': '£10', 'comment': 'A car', 'category': 'Photography'},
		{'name': 'TheatrePerformer','user': '-dsfs-', 'picture': 'images/photography/dancer.jpg', 'price': '£210', 'comment': 'A dancer', 'category': 'Photography'},
		{'name': 'GreenTreePython','user': 'Giles123', 'picture': 'images/photography/python.jpg', 'price': '£33', 'comment': 'A snake', 'category': 'Photography'},
		{'name': 'Tsunami','user': '87-Dom', 'picture': 'images/photography/tsunami.jpg', 'price': '£52', 'comment': 'A classroom after a tsunami', 'category': 'Photography'},
		{'name': 'GiantWave','user': 'JOHN_1', 'picture': 'images/photography/water.jpg', 'price': '£325', 'comment': 'A wave from a ship', 'category': 'Photography'} ]
		
	drawings_images = [
		{'name': 'AudiR8','user': '__Leah__', 'picture': 'images/drawings/audi.jpg', 'price': '£120', 'comment': 'An Audi R8', 'category': 'Drawing'},
		{'name': 'ClintEastwood','user': 'x-Harry-x', 'picture': 'images/drawings/clint.jpg', 'price': '£345', 'comment': 'Clint Eastwood portrait', 'category': 'Drawing'},
		{'name': 'Rose','user': '12456789', 'picture': 'images/drawings/rose.jpg', 'price': '£36', 'comment': 'A white rose', 'category': 'Drawing'},
		{'name': 'BigBen','user': 'TomSmith', 'picture': 'images/drawings/big_ben.jpg', 'price': '£6', 'comment': 'Big Ben tower', 'category': 'Drawing'},
		{'name': 'Tiger','user': 'Robotman', 'picture': 'images/drawings/tiger.jpg', 'price': '£35', 'comment': 'A friendly tiger', 'category': 'Drawing'} ]
		
	paintings_images = [
		{'name': 'Adam','user': 'Aida66', 'picture': 'images/paintings/adam.jpg', 'price': '£12', 'comment': 'The creation of man', 'category': 'Painting'},
		{'name': 'PersistenceofMemory','user': 'LeoFitz', 'picture': 'images/paintings/memory.jpg', 'price': '£22', 'comment': 'Salvador Dali painting', 'category': 'Painting'},
		{'name': 'GirlWithPearlEarrings','user': 'AgntSimm', 'picture': 'images/paintings/pearl_earring.jpg', 'price': '£47', 'comment': 'A pretty girl', 'category': 'Painting'},
		{'name': 'TheScream','user': 'Kyle-X', 'picture': 'images/paintings/scream.jpg', 'price': '£529', 'comment': 'A terrible figure screaming', 'category': 'Painting'},
		{'name': 'AStarryNight','user': 'Y_Jessie', 'picture': 'images/paintings/starry_night.jpg', 'price': '£222', 'comment': 'Van Gogh painting', 'category': 'Painting'} ]
	
	sculpture_images = [
		{'name': 'EndlessColumn','user': 'TheDocW', 'picture': 'images/sculpture/column.jpg', 'price': '£5', 'comment': 'A large structure', 'category': 'Sculpture'},
		{'name': 'Expansion','user': 'Gilbs96', 'picture': 'images/sculpture/expansion.jpg', 'price': '£53', 'comment': 'New York sculpture', 'category': 'Sculpture'},
		{'name': "MichaelangeloDavid",'user': 'RoseT2005', 'picture': 'images/sculpture/david.jpg', 'price': '£324', 'comment': 'The most famous statue', 'category': 'Sculpture'},
		{'name': 'RunningMustangs','user': 'Quantum', 'picture': 'images/sculpture/mustangs.jpg', 'price': '£99', 'comment': 'Horses running sculpture', 'category': 'Sculpture'},
		{'name': "Michaelangelo'sPieta",'user': 'PhilC', 'picture': 'images/sculpture/pieta.jpg', 'price': '£1', 'comment': 'Another famous statue', 'category': 'Sculpture'} ]
		
	other_images = [
		{'name': 'MyBed','user': 'Skye12', 'picture': 'images/other/bed.jpg', 'price': '£567', 'comment': 'Just a bed', 'category': 'Other'},
		{'name': 'EasterIslandHeads','user': '64Android', 'picture': 'images/other/easter_island.jpg', 'price': '£3452', 'comment': 'Those famous heads', 'category': 'Other'},
		{'name': 'FishTank','user': 'Gauntlets', 'picture': 'images/other/fish_tank.jpg', 'price': '£54', 'comment': 'Abstract art of a fish tank', 'category': 'Other'},
		{'name': 'VideoGame','user': 'Art_Lover', 'picture': 'images/other/game.jpg', 'price': '£14', 'comment': 'Digital art', 'category': 'Other'},
		{'name': 'Waterfall','user': 'NameTooLo', 'picture': 'images/other/waterfall.jpg', 'price': '£678','comment': 'Strange 3D drawing', 'category': 'Other' } ]
		

	artwork = [
	photography,
	drawings_images,
	sculpture_images,
	other_images,
	paintings_images]
		
	for art_data in artwork:
		for p in art_data:
			add_art(p['user'],p['category'],p['name'],p['picture'],p['price'],p['comment'])

def get_or_create_user(username):
    email='populationscript@artbud.com'
    password='placeholder987'
    try:
        user = User.objects.create_user(username, email, password)
        user.save()
        userprofile = UserProfile(user=user)
        userprofile.save()
    except:
        user = User.objects.get(username=username)
    return user
			
def add_art(user, category, name, picture, price, comment): 
    p = Upload.objects.get_or_create(user=get_or_create_user(user), category=category, 
    name=name,picture=picture, price=price, comment=comment)[0]
    p.save()
    return p

if __name__ == '__main__':
    print("Starting Artbud population script...")
    populate()