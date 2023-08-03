
from django.urls import path
from . import views 


app_name = 'tweetapp'

urlpatterns = [
    path('', views.listtweet, name='listtweet'), #senelsomuncu.com/tweetapp/listtweet
    path('addtweet/', views.addtweet, name='addtweet'), #senelsomuncu.com/tweetapp/addtweet
    path('addtweetbyform', views.addtweetbyform, name='addtweetbyform'), #senelsomuncu.com/tweetapp/addtweetbyform
    path('addtweetbymodelform', views.addtweetbymodelform, name='addtweetbymodelform'), #senelsomuncu.com/tweetapp/addtweetbymodelform
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('deletetweet/<int:id>', views.deletetweet, name='deletetweet'),


]