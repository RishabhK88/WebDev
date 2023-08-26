from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('form',views.formm, name='form'),
    # path('result',views.qviews, name='res'),
    path('noon',views.qimage, name='qimage')
]