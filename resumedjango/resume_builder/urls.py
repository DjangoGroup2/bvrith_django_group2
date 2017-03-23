from django.conf.urls import url
from resume_builder import views
urlpatterns = [
	url(r'^$', views.index, name = "index"),
	url(r'^resume/$', views.resume, name = "resume"),
	url(r'^success/$', views.success, name = "success"),
]
