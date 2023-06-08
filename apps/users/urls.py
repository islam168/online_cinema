from django.urls import path

from apps.users.views import (
    UserListCreateAPIView, UserAuthAPIVIew, UserDetailDestroyAPIView, PurchaseAPIView, SubscriptionAPIView
)

urlpatterns = [
    path('auth-token', UserAuthAPIVIew.as_view(), name='auth_token'),
    path('registration', UserListCreateAPIView.as_view(), name='users_list'),
    path('<int:id>', UserDetailDestroyAPIView.as_view(), name='user_detail'),
    path('purchase', PurchaseAPIView.as_view(), name='purchase'),
    path('subscription', SubscriptionAPIView.as_view(), name='subscription')
]
