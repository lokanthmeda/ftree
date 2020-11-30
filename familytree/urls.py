from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('account.urls')),
    path('details/',include('details.urls')),
    path('',include('details.urls')),


    url(r'^invitations/', include('invitations.urls', namespace='invitations')),
    # url(r'', include('invitations.urls', namespace='invitations'))
]
urlpatterns += static(settings.MEDIA_URL,
                      document_root = settings.MEDIA_ROOT)