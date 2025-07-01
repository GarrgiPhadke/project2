from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from index import views as main_views
from account.views import (
    registration_view, login_view, logout_view, account_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.index, name='index'),

    path('register/', registration_view, name="register"),
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name="login"),
    path('account/', account_view, name="account"),

    path('contact/', include('contact.urls')),
    path('aboutus/', include('aboutus.urls')),
    path('myservice/', include('myservice.urls')),
    path('myservice/', include('booking.urls')),  # You may want to check this duplication
    path('gallery/', include('gallery.urls')),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
