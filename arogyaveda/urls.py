from django.urls import path
from . import views



urlpatterns = [
		path('', views.index, name="Arogyamveda"),
		path('blog/',views.blogHome, name="blogHome"),
		path('blog/<str:slug>',views.blogPost, name="blogPost"),
		path('download/', views.fileDownload, name="Download"),
		path("contact/",views.contactus, name="contact"),
		path("video/",views.video, name="video"),
		# path('event/',views.eventHome, name="eventHome"),
		# path('event/<str:slug>',views.eventPost, name="eventPost")

]