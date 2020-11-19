from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('registerPage', views.registerPage, name='register'),
    path('volunteer', views.volunteer, name='volunteer'),
    path('dummy', views.DummyregisterPage, name='dummy'),
    path('login', views.loginPage, name='login'),
    path('feedback', views.feedbackview, name='feedback'),
    path('gallery', views.gallery, name='gallery'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)