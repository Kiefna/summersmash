from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django_registration.views import RegistrationView

from user.forms import UserForm
from util import views

admin.autodiscover()

urlpatterns = [
    url(r'^$', views.homepage),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/register/$',
        RegistrationView.as_view(
            form_class=UserForm
        ),
        name='registration_register',
        ),
    url(r'^accounts/', include('django_registration.backends.activation.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    from django.views import static as static_views
    from django.conf.urls.static import static
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', static_views.serve, {'document_root': settings.MEDIA_ROOT})
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
