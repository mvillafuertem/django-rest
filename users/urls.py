from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from users import views

urlpatterns = [
    url(r'^user/$', views.UserList.as_view())
    #url(r'^user/(?P\d+)/$', views.UserDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
