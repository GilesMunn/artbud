from django.conf.urls import url, include
from artbud import views
from registration.backends.simple.views import RegistrationView


class MyRegistrationView(RegistrationView):
	def get_success_url(self, user):
		return url('register_profile')



app = 'artbud'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'about/$', views.about, name='about'),
	url(r'^add_category/$', views.add_category, name='add_category'),

	url(r'category/$', views.category, name='category'),

	url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
		views.show_category,
		name='show_category'),
		
	url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$',
		views.add_page,
		name='add_page'),
	
	url(r'^accounts/register/$',MyRegistrationView.as_view(),name='registration_register'),
	url(r'^accounts/', include('registration.backends.simple.urls')),
	url(r'^goto/$', views.track_url, name='goto'),
    url(r'^register_profile/$', views.register_profile, name='register_profile'),
    url(r'^profile/(?P<username>[\w\-]+)/$', views.profile, name='profile'),
    url(r'^profiles/$', views.list_profiles, name='list_profiles'),

]

