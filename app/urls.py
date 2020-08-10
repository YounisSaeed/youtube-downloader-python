from django.urls import path
from app.views import index,index2,download_complete
app_name = 'app'

urlpatterns = [
    path('',index,name='down'),
    path('download/',index2,name=''),
    path('download_complete/<res>/',download_complete,name="download_complete"),
]