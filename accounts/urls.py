from django.urls import path
from . import views
# ログイン用のviewをインポート
from django.contrib.auth import views as auth_views
app_name = 'accounts'
urlpatterns = [
    path('signup/',views.SignUpView.as_view(), name='signup'),
    path('signup_success/',views.SignUpSuccessView.as_view(), name='signup_success'),
    path("signin/",auth_views.LoginView.as_view(template_name='signin.html'),name='signin'),
    path('signout/',auth_views.LogoutView.as_view(template_name='signout.html'),name='signout'),
    path('user-detail/<int:pk>/',views.UserDetailView.as_view(),name='userdetail'),
    path('user-update/<int:pk>/',views.UserUpdateView.as_view(),name='userupdate'),
    path('user-delete/<int:pk>',views.PhotoDetleteView.as_view(),name='delete')
]