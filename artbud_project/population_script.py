# -*- coding: utf-8 -*-
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','artbud_project.settings')

import django
django.setup()

from artbud.models import Category, Page

def populate():
	
	photography = [
		{name: 'Car in Damascus',user: 'Jack96', picture: '/static/images/photography/car.jpg', price: '£10', comment: 'A car', category: 'photography'},
		{name: 'Theatre Performer',user: '-dsfs-', picture: '/static/images/photography/dancer.jpg', price: '£210', comment: 'A dancer', category: 'photography'},
		{name: 'Green Tree Python',user: 'Giles123', picture: '/static/images/photography/python.jpg', price: '£33', comment: 'A snake', category: 'photography'},
		{name: 'Tsunami',user: '87-Dom', picture: '/static/images/photography/tsunami.jpg', price: '£52', comment: 'A classroom after a tsunami', category: 'photography'},
		{name: 'Giant Wave',user: 'JOHN_1', picture: '/static/images/photography/water.jpg', price: '£325', comment: 'A wave from a ship', category: 'photography'} ]
		
	drawings_images = [
		{name: 'Audi R8',user: '__Leah__', picture: '/static/images/drawings/audi.jpg', price: '£120', comment: 'An Audi R8', category: 'drawing'},
		{name: 'Clint Eastwood',user: 'xx-Harry-xx', picture: '/static/images/drawings/clint.jpg', price: '£345', comment: 'Clint Eastwood portrait', category: 'drawing'},
		{name: 'Rose',user: '12456789', picture: '/static/images/drawings/rose.jpg', price: '£36', comment: 'A white rose', category: 'drawing'},
		{name: 'Big Ben',user: 'TomSmith', picture: '/static/images/drawings/big_ben.jpg', price: '£6', comment: 'Big Ben tower', category: 'drawing'},
		{name: 'Tiger',user: 'Robotman', picture: '/static/images/drawings/tiger.jpg', price: '£35', comment: 'A friendly tiger', category: 'drawing'} ]
		
	paintings_images = [
		{name: 'Adam',user: 'Aida66', picture: '/static/images/paintings/adam.jpg', price: '£12', comment: 'The creation of man', category: 'painting'},
		{name: 'Persistence of Memory',user: 'LeoFitz', picture: '/static/images/paintings/memory.jpg', price: '£22', comment: 'Salvador Dali painting', category: 'painting'},
		{name: 'Girl With Pearl Earrings',user: 'AgntSimmons', picture: '/static/images/paintings/pearl_earring.jpg', price: '£47', comment: 'A pretty girl', category: 'painting'},
		{name: 'The Scream',user: 'Kyle-X', picture: '/static/images/paintings/scream.jpg', price: '£529', comment: 'A terrible figure screaming', category: 'painting'},
		{name: 'A Starry Night',user: 'Y_Jessie', picture: '/static/images/paintings/starry_night.jpg', price: '£222', comment: 'Van Gogh painting', category: 'painting'} ]
	
	sculpture_images = [
		{name: 'Endless Column',user: 'TheDocW', picture: '/static/images/sculpture/column.jpg', price: '£5', comment: 'A large structure', category: 'sculpture'},
		{name: 'Expansion',user: 'Gilbs96', picture: '/static/images/sculpture/expansion.jpg', price: '£53', comment: 'New York sculpture', category: 'sculpture'},
		{name: "Michaelangelo's David",user: 'RoseT2005', picture: '/static/images/sculpture/david.jpg', price: '£324', comment: 'The most famous statue', category: 'sculpture'},
		{name: 'Running Mustangs',user: 'Quantum', picture: '/static/images/sculpture/mustangs.jpg', price: '£99', comment: 'Horses running sculpture', category: 'sculpture'},
		{name: "Michaelangelo's Pieta",user: 'PhilC', picture: '/static/images/sculpture/pieta.jpg', price: '£1', comment: 'Another famous statue', category: 'sculpture'} ]
		
	other_images = [
		{name: 'My Bed',user: 'Skye12', picture: '/static/images/other/bed.jpg', price: '£567', comment: 'Just a bed', category: 'other'},
		{name: 'Easter Island Heads',user: '64Android', picture: '/static/images/other/easter_island.jpg', price: '£3452', comment: 'Those famous heads', category: 'other'},
		{name: 'Fish Tank',user: 'Gauntlets', picture: '/static/images/other/fish_tank.jpg', price: '£54', comment: 'Abstract art of a fish tank', category: 'other'},
		{name: 'Video Game',user: 'Art_Lover', picture: '/static/images/other/game.jpg', price: '£14', comment: 'Digital art', category: 'other'},
		{name: 'Waterfall',user: 'HiEverybody', picture: '/static/images/other/waterfall.jpg', price: '£678',comment: 'Strange 3D drawing', category: 'other' } ]
		
	artwork = {'Photography': {'pages': photography_images},
			   'Drawing': {'pages': drawings_images},
			   'Sculpture': {'pages': sculpture_images},
			   'Other': {'pages': other_images},
			   'Painting': {'pages': painting_images} }
		
	for art, art_data in artwork.items():
		c = add_art(art)
		for p in art_data['pages']:
			add_page(c, p['name'], p['user'], p['picture'], p['comment'], p['category'])
    
	for c in Category.objects.all():
		for p in Page.objects.filter(category=c):
			print("- {0} - {1}".format(str(c), str(p)))

def add_page(art, name, user, picture, comment, category):
    p = Page.objects.get_or_create(category=art, name=name)[0]
    p.name=name
	p.user=user
	p.picture=picture
	p.comment=comment
	p.category=category
    p.save()
    return p

def add_art(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

if __name__ == '__main__':
    print("Starting Artbud population script...")
    populate()