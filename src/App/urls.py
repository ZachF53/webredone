from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from post.views import index, portfolio, service, contact, thanks

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('portfolio/', portfolio),
    path('services/', service),
    path('contact/', contact),
    path('thanks/', thanks),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)