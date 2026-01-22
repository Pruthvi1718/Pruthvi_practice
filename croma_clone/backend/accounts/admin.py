from django.contrib import admin
from .models import UserProfile, Address, Wishlist, RewardWallet

admin.site.register(UserProfile)
admin.site.register(Address)
admin.site.register(Wishlist)
admin.site.register(RewardWallet)
