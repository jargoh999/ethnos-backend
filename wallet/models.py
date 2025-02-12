from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Wallet(models.Model):
    """Wallet model representing user's financial account"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wallet')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=8899.75)
    
    def __str__(self):
        return f"{self.user.username}'s Wallet"

class Transaction(models.Model):
    """Transaction model for income and expenses"""
    TRANSACTION_TYPES = [
        ('income', 'Income'),
        ('expenses', 'Expenses')
    ]

    wallet = models.ForeignKey(Wallet, related_name='transactions', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    timestamp = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.transaction_type.capitalize()} - ${self.amount}"

class UserProfile(models.Model):
    """User profile for QR code and additional details"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    uid = models.CharField(max_length=50, unique=True, default='8194638720')
    name = models.CharField(max_length=100, default='Call Me Teggar')
    avatar_url = models.URLField(default='/placeholder.svg')
    
    def __str__(self):
        return self.name

class SavingsPlan(models.Model):
    """Savings plan model"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='savings_plans')
    name = models.CharField(max_length=100)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return f"{self.name} - ${self.current_amount}/{self.target_amount}"