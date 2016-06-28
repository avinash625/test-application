from django.conf.urls import url
from olx import views

urlpatterns = [
    url(r'^posts/$',view=views.postlistview , name = 'postslistview'),
    url(r'post/(?P<id>[0-9]*)/$',view=views.singlepostview,name ='singlepostview'),

]