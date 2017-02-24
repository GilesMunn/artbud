from django.conf.urls import url, include
from artbud import views
from registration.backends.simple.views import RegistrationView


class MyRegistrationView(RegistrationView):
	def get_success_url(self, user):
		return '/artbud/'


app = 'artbud'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'about/$', views.about, name='about'),
	url(r'^add_category/$', views.add_category, name='add_category'),

	url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
		views.show_category,
		name='show_category'),
		
	url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$',
		views.add_page,
		name='add_page'),
	
	url(r'^accounts/register/$',MyRegistrationView.as_view(),name='registration_register'),
	
	url(r'^accounts/', include('registration.backends.simple.urls')),

]

