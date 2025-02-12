from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from wallet.models import Wallet, Transaction, UserProfile, SavingsPlan
import random
from django.utils import timezone

class Command(BaseCommand):
    help = 'Generate dummy data for e-wallet'

    def handle(self, *args, **kwargs):
        # Create or get a test user
        user, created = User.objects.get_or_create(
            username='testuser', 
            defaults={'email': 'test@example.com'}
        )
        
        # Set a password
        user.set_password('testpassword')
        user.save()

        # Create or get wallet
        wallet, _ = Wallet.objects.get_or_create(
            user=user, 
            defaults={'balance': 8899.75}
        )

        # Create user profile
        UserProfile.objects.get_or_create(
            user=user,
            defaults={
                'uid': '8194638720',
                'name': 'Call Me Teggar',
                'avatar_url': '/placeholder.svg'
            }
        )

        # Generate transactions
        transaction_types = ['income', 'expenses']
        for _ in range(10):
            Transaction.objects.create(
                wallet=wallet,
                amount=random.uniform(10, 1000),
                transaction_type=random.choice(transaction_types),
                timestamp=timezone.now()
            )

        # Create savings plans
        SavingsPlan.objects.create(
            user=user,
            name='Emergency Fund',
            target_amount=5000,
            current_amount=random.uniform(0, 5000)
        )

        self.stdout.write(self.style.SUCCESS('Successfully generated dummy data'))