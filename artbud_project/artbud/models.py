from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth.models import User
from django import forms


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__self(self):
        return self.name

    def __unicode__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    bio = models.CharField(blank=True, max_length=240)
    artwork = models.ImageField(upload_to='artwork_images', blank=True)

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username


class Artwork(models.Model):
    user = models.OneToOneField(User)
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    contact = models.EmailField()
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class ArtworkForm(forms.ModelForm):
    category = forms.CharField()
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    contact = models.EmailField()


class UserProfileForm(forms.ModelForm):
    website = forms.URLField(required=False)
    picture = forms.ImageField(required=False)
    bio = forms.CharField(required=False)

    class Meta:
        model = UserProfile
        exclude = ('user',)


def user_directory_path(instance, filename):
    return 'artwork_images/{0}/{1}'.format(instance.user, filename)


class Upload(models.Model):
	user = models.ForeignKey(User)
	#category = models.ForeignKey(Category)
	name = models.CharField(max_length=128)
	picture = models.ImageField(upload_to=user_directory_path)
	rating = models.IntegerField(default=0)
	price = models.IntegerField(default=0)
	comment = models.CharField(max_length=256)


	def __str__(self):
		return self.name

	def __unicode__(self):
		return self.name
