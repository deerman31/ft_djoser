from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from .views.signup_view import SignupView
from .views.login_view import LoginView
from .views.verify_token_view import VerifyTokenView
from .views.refresh_token_view import RefreshTokenView
from .views.delete_user_view import DeleteUserView
from .views.get_user_name_view import GetUserNameView
from .views.get_user_email_view import GetUserEmailView

from .views.set_avatar_view import SetAvatarView

from .views.update_email_view import UpdateEmailView
from .views.update_name_view import UpdateNameView

from .views.get_avatar_view import GetAvatarView

from .views.delete_avatar_view import DeleteAvatarView

urlpatterns = [
    path("signup/", SignupView.as_view()),
    path("login/", LoginView.as_view()),
    path("jwt/refresh/", RefreshTokenView.as_view()),
    path("jwt/verify/", VerifyTokenView.as_view()),
    path("get/name/", GetUserNameView.as_view()),
    path("get/email/", GetUserEmailView.as_view()),

    path("get/avatar/", GetAvatarView.as_view()),

    path("update/name/", UpdateNameView.as_view()),
    path("update/email/", UpdateEmailView.as_view()),
    path("set/avatar/", SetAvatarView.as_view()),

    path("delete/avatar/", DeleteAvatarView.as_view()),
    path("delete/user/", DeleteUserView.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)