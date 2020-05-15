from django.urls import path, include

from rest_framework.routers import DefaultRouter

from gate import views


router = DefaultRouter()
'''# name of the 1st URL you want to register
# while creating a viewset URL we need not have to specify a forward slash '/' in 'hello-viewset' URL name
# 2nd argument is the viewset that we want to register to this viewset created in the views.py'''
''' And 3rd argument is the base_name for our URL,
used to retirve the URL in our router by using the URL retrieveing
function provided by our router'''
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls))
    #'' (blank space above is bcz is we do not want to include the prefix to the base URL of the router)
]
