from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from blog.views import homepage
from blog.views.contact import contact

urlpatterns = [
    path('contact', contact),
    path('', homepage),
]