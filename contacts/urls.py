from django.urls import path
from . import views

# Url patterns to navigate through the application
urlpatterns = [
    path('', views.contacts_home, name = 'contacts_home'),
    path('signup', views.signup, name = 'signup'),
    path('signin', views.signin, name = 'signin'),
    path('signout', views.signout, name = 'signout'),
    path('contacts', views.contacts, name = 'contacts'),
]
