import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','artbud_project.settings')

import django
django.setup()

from artbud.models import Category, Page

def populate():
	
	abstract_pages = [
		{'title': 'Ideas',
		'url':'http://inspirationseek.com/wp-content/uploads/2014/06/Abstract-Painting-Ideas.jpg', 'views': 12},
		{'title': 'Nature',
		'url':'http://inspirationseek.com/wp-content/uploads/2014/06/Abstract-Painting-Nature.jpg', 'views': 34},
		{'title': 'Flower Nature',
		'url':'http://inspirationseek.com/wp-content/uploads/2014/06/Abstract-Painting-Flower-Nature.jpg', 'views': 15} ]
		
	still_life_pages = [
		{'title': 'Bas Meeuws',
		'url':'http://cdn.mos.cms.futurecdn.net/rmnxHaXkhmZjncyzMahdJU-650-80.jpg', 'views': 24 },
		{'title': 'Elena K',
		'url':'http://cdn.mos.cms.futurecdn.net/fff6c24beaf409b2d24e479a414374a9-650-80.jpg', 'views': 86 },
		{'title': 'Joan Gamell',
		'url':'http://cdn.mos.cms.futurecdn.net/6133a6789a940f061a2a4eaf898ad67d-650-80.jpg', 'views': 201 } ]
		
	impressionist_pages = [
		{'title': 'Les raboteurs de parquet',
		'url':'https://learnodo-newtonic.com/wp-content/uploads/2013/07/The-Floor-Scrapers-by-Gustave-Caillebotte.jpeg'},
		{'title': 'Absinthe',
		'url':'https://learnodo-newtonic.com/wp-content/uploads/2013/07/The-Absinthe-Drinker-by-Edgar-Degas.jpg'},
		{'title': 'Pont Boieldieu in Rouen, Rainy Weather',
		'url':'https://learnodo-newtonic.com/wp-content/uploads/2013/07/Pont-Boieldieu-in-Rouen-Rainy-Weather-by-Camille-Pissarro.jpg'} ]
		
	photo_pages = [
		{'title': 'Modern dykes, windmills and highways in the Netherlands',
		'url':'https://files.brightside.me/files/news/part_4/46555/208855-3432610-1000-1446444849comment_pngkZ7y3otB9J0WJmTBEYYcmM3S6Tydz-1000-6d51e333c8-1484729696.jpg', 'views': 27 },
		{'title': 'A temple covered in ash from the Ontake volcanic eruption, Japan',
		'url':'https://files.brightside.me/files/news/part_4/46555/209105-3446910-1000-144645398520141015-ontake-1000-66810123c4-1484729696.jpg', 'views': 135},
		{'title': 'Two worlds divided, New York, USA',
		'url':'https://files.brightside.me/files/news/part_4/46555/209955-d-v-a-a-1000-1446452908-1000-6e726f73ab-1484729696.jpg', 'views': 400 } ]
		
	artwork = {'Abstract': {'pages': abstract_pages, 'views': 150, 'likes': 112 },
			   'Still Life': {'pages': still_life_pages, 'views': 10, 'likes': 3 },
			   'Impressionist': {'pages': impressionist_pages, 'views': 253, 'likes': 76 },
			   'Photos': {'pages': photo_pages, 'views': 423, 'likes': 290 }, 
			   
			   }
		
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