from django.urls import path
from feed import views

urlpatterns=[
    path('',views.func1,name='homePage'),
    path('about',views.func2,name='aboutPage'),
    path('contact',views.func3,name='contactPage'),
    path('posts',views.func4,name='postsPage'),
    path('login',views.func5,name='loginPage'),
    path('form',views.func6,name='formsPage'),
]