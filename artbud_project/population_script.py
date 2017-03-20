import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','artbud_project.settings')

import django
django.setup()

from artbud.models import Category, Page

def populate():
	
	photography = [
		{title: 'Car in Damascus',user: 'Jack96', picture: '/images/photography/car.jpg', price: '£10', comment: 'A car'},
		{title: 'Theatre Performer',user: '-dsfs-', picture: '/images/photography/dancer.jpg', price: '£210', comment: 'A dancer'},
		{title: 'Green Tree Python',user: 'Giles123', picture: '/images/photography/python.jpg', price: '£33', comment: 'A snake'},
		{title: 'Tsunami',user: '87-Dom', picture: '/images/photography/tsunami.jpg', price: '£52', comment: 'A classroom after a tsunami'},
		{title: 'Giant Wave',user: 'JOHN_1', picture: '/images/photography/water.jpg', price: '£325', comment: 'A wave from a ship'}]
		
	drawings_images = [
		{title: 'Audi R8',user: '__Leah__', picture: '/images/drawings/audi.jpg', price: '£120', comment: 'An Audi R8'},
		{title: 'Clint Eastwood',user: 'xx-Harry-xx', picture: '/images/drawings/clint.jpg', price: '£345', comment: 'Clint Eastwood portrait'},
		{title: 'Rose',user: '12456789', picture: '/images/drawings/rose.jpg', price: '£36', comment: 'A white rose'},
		{title: 'Big Ben',user: 'TomSmith', picture: '/images/drawings/big_ben.jpg', price: '£6', comment: 'Big Ben tower'},
		{title: 'Tiger',user: 'Robotman', picture: '/images/drawings/tiger.jpg', price: '£35', comment: 'A friendly tiger'}]
		
	paintings_images = [
		{title: 'Adam',user: 'Aida66', picture: '/images/paintings/adam.jpg', price: '£12', comment: 'The creation of man'},
		{title: 'Persistence of Memory',user: 'LeoFitz', picture: '/images/paintings/memory.jpg', price: '£22', comment: 'Salvador Dali painting'},
		{title: 'Girl With Pearl Earrings',user: 'AgntSimmons', picture: '/images/paintings/pearl_earring.jpg', price: '£47', comment: 'A pretty girl'},
		{title: 'The Scream',user: 'Kyle-X', picture: '/images/paintings/scream.jpg', price: '£529', comment: 'A terrible figure screaming'},
		{title: 'A Starry Night',user: 'Y_Jessie', picture: '/images/paintings/starry_night.jpg', price: '£222', comment: 'Van Gogh painting'}]
	
	sculpture_images = [
		{title: 'Endless Column',user: 'TheDocW', picture: '/images/sculpture/column.jpg', price: '£5', comment: 'A large structure'},
		{title: 'Expansion',user: 'Gilbs96', picture: '/images/sculpture/expansion.jpg', price: '£53', comment: 'New York sculpture'},
		{title: "Michaelangelo's David",user: 'RoseT2005', picture: '/images/sculpture/david.jpg', price: '£324', comment: 'The most famous statue'},
		{title: 'Running Mustangs',user: 'Quantum', picture: '/images/sculpture/mustangs.jpg', price: '£99', comment: 'Horses running sculpture'},
		{title: "Michaelangelo's Pieta",user: 'PhilC', picture: '/images/sculpture/pieta.jpg', price: '£1', comment: 'Another famous statue'}]
		
	other_images = [
		{title: 'My Bed',user: 'Skye12', picture: '/images/other/bed.jpg', price: '£567', comment: 'Just a bed'},
		{title: 'Easter Island Heads',user: '64Android', picture: '/images/other/easter_island.jpg', price: '£3452', comment: 'Those famous heads'},
		{title: 'Fish Tank',user: 'Gauntlets', picture: '/images/other/fish_tank.jpg', price: '£54', comment: 'Abstract art of a fish tank'},
		{title: 'Video Game',user: 'Art_Lover', picture: '/images/other/game.jpg', price: '£14', comment: 'Digital art'},
		{title: 'Waterfall',user: 'HiEverybody', picture: '/images/other/waterfall.jpg', price: '£678', comment: 'Strange 3D drawing'}]
	
		
	artwork = {"Photography": {"info": photography_images},
			   "Drawing": {"info": drawings_images},
			   "Sculpture": {"info": sculpture_images},
			   "Other": {"info": other_images},
			   "Painting": {"info": painting_images} }
		
	for art, art_data in artwork.items():
		c = add_art(art)
		for p in art_data["pages"]:
			add_page(c, p["title"], p["url"])
    
	for c in Category.objects.all():
		for p in Page.objects.filter(category=c):
			print("- {0} - {1}".format(str(c), str(p)))

def add_page(art, title, url, views=0):
    p = Page.objects.get_or_create(category=art, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_art(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views=views
    c.likes=likes
    c.save()
    return c

if __name__ == '__main__':
    print("Starting Artbud population script...")
    populate()