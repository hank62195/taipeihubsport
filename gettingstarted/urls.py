from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^index', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^login', hello.views.login, name='login'),#登入
    url(r'^game', hello.views.game, name='game'),
    url(r'^team', hello.views.teamlist, name='team'),
    url(r'^manager', hello.views.manager, name='manager'),
    url(r'^register', hello.views.register, name='register'),
    url(r'^logout', hello.views.logout, name='logout'),
    path('admin/', admin.site.urls),
]