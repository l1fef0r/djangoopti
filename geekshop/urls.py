import mainapp.views as mainapp
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.urls import path, re_path

urlpatterns = [
    re_path(r'^$', mainapp.main, name='main'),
    path('', include('social_django.urls', namespace='social')),
    re_path(r'^products/', include('mainapp.urls', namespace='products')),
    re_path('contact/', mainapp.contact, name='contact'),
    path('auth/', include('authapp.urls', namespace='auth')),
    re_path(r'^basket/', include('basketapp.urls', namespace='basket')),
    re_path(r'^admin/', include('adminapp.urls', namespace='admin')),
    path('orders/', include('ordersapp.urls', namespace='ordersapp')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
