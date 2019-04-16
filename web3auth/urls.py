from django.conf.urls import url

from web3auth import views
app_name = 'web3auth'
urlpatterns = [
    url(r'login_api/$', views.login_api, name='login_api'),
    # url(r'signup_api/$', views.signup_api, name='signup_api'),
    # url(r'signup_view/$', views.signup_view, name='signup_view'),
]
