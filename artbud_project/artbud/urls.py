from django.conf.urls import url, include
from artbud import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'category/$', views.category, name='category'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^register_profile/$', views.register_profile, name='register_profile'),
    url(r'^profile/(?P<username>[\w\-]+)/$', views.profile, name='profile'),
    url(r'^profiles/$', views.list_profiles, name='list_profiles'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^category/painting/$', views.user_upload_painting, name='painting'),
    url(r'^category/drawing/$', views.user_upload_drawing, name='drawing'),
    url(r'^category/photography/$', views.user_upload_photography, name='photography'),
    url(r'^category/sculpture/$', views.user_upload_sculpture, name='sculpture'),
    url(r'^category/other/$', views.user_upload_other, name='other'),
    url(r'^add_artwork/$', views.add_artwork, name='add_artwork'),
    url(r'^upload/$', views.user_upload, name='upload'),
    url(r'^profile/(?P<username>[\w\-]+)/(?P<uploaded_picture>[\w\-]+)/$', views.art_display, name='art_display'),
    url(r'^profile/(?P<username>[\w\-]+)/(?P<uploaded_picture>[\w\-]+)/delete/$', views.art_delete, name='art_delete'),
]
