from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from util import views

admin.autodiscover()

urlpatterns = [
    url(r'^$', views.homepage),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.views import static as static_views
    from django.conf.urls.static import static
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', static_views.serve, {'document_root': settings.MEDIA_ROOT})
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
