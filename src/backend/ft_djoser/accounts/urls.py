from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from .views.signup_view import SignupView

urlpatterns = [
    path("signup/", SignupView.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)