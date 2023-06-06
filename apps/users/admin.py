from django.contrib import admin

from apps.users.models import User, Subscription, Purchase, MovieReview, TVShowReview


admin.site.register(User)
admin.site.register(Subscription)
admin.site.register(Purchase)
admin.site.register(MovieReview)
admin.site.register(TVShowReview)

