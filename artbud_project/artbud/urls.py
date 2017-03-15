from django.conf.urls import url, include
from artbud import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'category/$', views.category, name='category'),
	url(r'^category/(?P<category_name_slug>[\w\-]+)/$',views.show_category,name='show_category'),
	url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$',views.add_page,name='add_page'),
	url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^register_profile/$', views.register_profile, name='register_profile'),
    url(r'^profile/(?P<username>[\w\-]+)/$', views.profile, name='profile'),
    url(r'^profiles/$', views.list_profiles, name='list_profiles'),
	url(r'^like/$', views.like_category, name='like_category'),
]

