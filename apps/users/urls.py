from django.urls import path

from apps.users.views import (
    UserListCreateAPIView, UserAuthAPIVIew, UserDetailDestroyAPIView, PurchaseAPIView, SubscriptionAPIView,
    UserChangePasswordAPIView
)

urlpatterns = [
    path('auth-token', UserAuthAPIVIew.as_view(), name='auth_token'),
    path('registration', UserListCreateAPIView.as_view(), name='users_list'),
    path('<int:id>', UserDetailDestroyAPIView.as_view(), name='user_detail'),
    path('<int:id>/change_password', UserChangePasswordAPIView.as_view(), name='user_change_password'),
    path('purchase', PurchaseAPIView.as_view(), name='purchase'),
    path('subscription', SubscriptionAPIView.as_view(), name='subscription')
]
