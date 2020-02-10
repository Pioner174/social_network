from django.urls import path, include
from django.contrib.auth import views as a_v
from . import views

urlpatterns = [
    # path('login/', views.user_login, name='login'),
    # path('login/', a_v.LoginView.as_view(), name='login'),
    # path('logout/', a_v.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),
    # path('password_change/', a_v.PasswordChangeView.as_view(),
    #      name='password_change'),
    # path('password_change/done/', a_v.PasswordChangeDoneView.as_view(),
    #      name='password_change_done'),
    # path('password_reset/', a_v.PasswordResetView.as_view(),
    #      name='password_reset'),
    # path('password_reset/done/', a_v.PasswordResetDoneView.as_view(),
    #      name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', a_v.PasswordResetConfirmView.as_view(),
    #      name='password_reset_confirm'),
    # path('reset/done/', a_v.PasswordResetCompleteView.as_view(),
    #      name='password_reset_complete')
    path('', include('django.contrib.auth.urls')),
]
