from rest_framework import viewsets
from .models import Wallet, Transaction, UserProfile, SavingsPlan
from .serializers import (
    WalletSerializer, 
    TransactionSerializer, 
    UserProfileSerializer,
    SavingsPlanSerializer
)

class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer