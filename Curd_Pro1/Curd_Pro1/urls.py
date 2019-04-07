from django.contrib import admin
from django.conf.urls import url
from Curd_App1 import views

urlpatterns = {
    url('admin/', admin.site.urls),
    url(r'^$', views.homeview),
    url(r'^insert/', views.insertview),
    url(r'^update/', views.Updateview),
    url(r'^retrieve/',views.retrieveview),
    url(r'^delete/',views.deleteview)
}
