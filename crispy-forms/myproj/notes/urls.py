from django.conf.urls import include, url
from notes import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'myproj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', views.HomeView.as_view()),
]
