from rest_framework import viewsets , permissions
from .models import Wallet, Transaction, UserProfile, SavingsPlan
from .serializers import (
    WalletSerializer, 
    TransactionSerializer, 
    UserProfileSerializer,
    SavingsPlanSerializer
)

class WalletViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer