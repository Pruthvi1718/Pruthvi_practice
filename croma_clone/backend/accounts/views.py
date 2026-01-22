from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Address, Wishlist, RewardWallet

@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')


@login_required
def profile(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        profile.title = request.POST.get('title')
        profile.middle_name = request.POST.get('middle_name')
        profile.gender = request.POST.get('gender')
        profile.phone = request.POST.get('phone')
        profile.save()
        return redirect('accounts:profile')
    return render(request, 'accounts/profile.html', {'profile': profile})


@login_required
def address_list(request):
    addresses = Address.objects.filter(user=request.user)
    return render(request, 'accounts/address_list.html', {'addresses': addresses})


@login_required
def wishlist(request):
    wishlist, _ = Wishlist.objects.get_or_create(user=request.user)
    return render(request, 'accounts/wishlist.html', {'wishlist': wishlist})


@login_required
def rewards(request):
    wallet, _ = RewardWallet.objects.get_or_create(user=request.user)
    return render(request, 'accounts/rewards.html', {'wallet': wallet})


#jwt log + reg
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.datas)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)

        return Response({
            'message': 'User registered successfully',
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
