from django.urls import include, path

from .views import GitHubLogin, GoogleLogin, MyPage, mypage_payments

from .views import IdLogin, Logout

from .views import login_api, logout_api

urlpatterns = [
    path("auth/", include("dj_rest_auth.urls")),
    path("accounts/login/", IdLogin.as_view(), name='accounts_login'),
    # path("accounts/email/", IdLogin.as_view(), name='account_email'),
    path("accounts/logout/", Logout.as_view(), name='accounts_logout'),
    # path("accounts/signup/", IdLogin.as_view(), name="account_signup"),
    # path("auth/github/login/", GitHubLogin.as_view(), name="github_login"),
    # path("auth/google/login/", GoogleLogin.as_view(), name="google_login"),
    #path("my-page/payments", MyPage.as_view())
    path("my-page/payments/", mypage_payments),

    # Endpoints for Seesion Based Login
    path("api/login/", login_api, name="login-api"),
    path("api/logout/", logout_api, name="logout-api"),
    # path("api/logout/", )

    path("api/mypage/", MyPage.as_view(), name="mypage-api"),
]
