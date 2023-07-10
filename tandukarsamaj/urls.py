from django.conf.urls import handler404, handler500
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

urlpatterns=[
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('dashboard/', include('dashboard.urls')),
 ]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

handler404 = 'app.views.error_404'


# urlpatterns=[
#     path('i182/', include("django.conf.urls.i18n")),
#  ]

# urlpatterns += i18n_patterns(
#     path( _('admin/'), admin.site.urls),
#     path('', include('app.urls')),
#     path('dashboard/', include('dashboard.urls')),
#     prefix_default_language=False,
# )+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# urlpatterns = [
#     *i18n_patterns(*urlpatterns, prefix_default_language=False),
#     ]
