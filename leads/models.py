from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save


class User(AbstractUser):
    is_organiser = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.user.username


class Lead(models.Model):
    profile_picture = models.ImageField(blank=True, null=True, default=None)
    logo = models.ImageField(blank=True, null=True, default=None)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    company = models.CharField(max_length=100, default=None)
    post = models.CharField(max_length=100, default=None)
    email = models.EmailField(max_length=100, default=None)
    phone = models.CharField(max_length=100, default=None)
    communication_preference = models.CharField(choices=[
        ('email', 'Email'),
        ('sms', 'SMS'),
        ('whatsapp', 'Whatsapp'),
        ('polleen', 'Polleen')], max_length=100, default='Polleen')
    leisure = models.CharField(max_length=100, blank=True, null=True, default=None)
    linkedin = models.URLField(max_length=100, blank=True, null=True, default=None)
    facebook = models.URLField(max_length=100, blank=True, null=True, default=None)
    twitter = models.URLField(max_length=100, blank=True, null=True, default=None)
    instagram = models.URLField(max_length=100, blank=True, null=True, default=None)
    website = models.URLField(max_length=100, blank=True, null=True, default=None)
    other_social_media = models.URLField(max_length=100, blank=True, null=True, default=None)
    agent = models.ForeignKey(Agent, blank=True, on_delete=models.SET_NULL, null=True)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=None)
    category = models.ForeignKey('Category', related_name="leads", on_delete=models.SET_NULL, null=True, blank=True,
                                 default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class InvitedLead(models.Model):
    profile_picture = models.ImageField(blank=True, null=True, default=None)
    logo = models.ImageField(blank=True, null=True, default=None)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    company = models.CharField(max_length=100, default=None)
    post = models.CharField(max_length=100, default=None)
    email = models.EmailField(max_length=100, default=None)
    phone = models.CharField(max_length=100, default=None)
    linkedin = models.URLField(max_length=100, blank=True, null=True, default=None)
    facebook = models.URLField(max_length=100, blank=True, null=True, default=None)
    twitter = models.URLField(max_length=100, blank=True, null=True, default=None)
    instagram = models.URLField(max_length=100, blank=True, null=True, default=None)
    website = models.URLField(max_length=100, blank=True, null=True, default=None)
    other_social_media = models.URLField(max_length=100, blank=True, null=True, default=None)
    invited_by = models.CharField(max_length=100, default=None)
    agent = models.ForeignKey(Agent, blank=True, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Category(models.Model):
    name = models.CharField(max_length=30)  # New, Contacted, Converted, Unconverted
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name


def post_user_created_signal(sender, instance, created, *args, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(post_user_created_signal, sender=User)
