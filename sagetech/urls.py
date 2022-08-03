from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('blog/', include('blog.urls')),
    path('account/', include('account.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('propos/', include('proposition.urls')),
    path('token/', views.CustomAuthToken.as_view())

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
