from django.urls import path
from . import views



urlpatterns = [
		path('', views.index, name="ShopHome"),
		path('advisor/', views.advisor, name="Advisor"),
		path('download/', views.fileDownload, name="Download"),
		path('blogComment', views.blogComment, name="blogComment"),
		path('blog/',views.blogHome, name="blogHome"),
		path('blog/<str:slug>',views.blogPost, name="blogPost"),
		path('search', views.search, name="search"),
		path("contact/",views.contactus, name="contact"),
		path("video/",views.video, name="video"),
		path("disease/",views.diseaseHome, name="disease"),
		path('disease/<str:slug>',views.diseasePost, name="diseasePost"),
		path('event/',views.eventHome, name="eventHome"),
		path('event/<str:slug>',views.eventPost, name="eventPost"),

]