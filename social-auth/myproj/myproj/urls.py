from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

import app.views as app_views


urlpatterns = [
    # Examples:
    # url(r'^$', 'myproj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', app_views.HomeView.as_view(), name='home'),
    url(r'^welcome/', login_required(app_views.WelcomeView.as_view()), name='welcome'),
    url(r'^createuser/', app_views.CreateUser.as_view(), name='createuser'),
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
]
