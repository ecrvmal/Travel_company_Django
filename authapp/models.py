from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class TravelUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name='Age', default=18)


class TravelUserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'F'

    Gender_Choices = (
        (MALE, 'M'),
        (FEMALE, 'F'),
    )

    user = models.OneToOneField(TravelUser, unique=True, null=False,
                                db_index=True, on_delete=models.CASCADE)
    tagline = models.CharField(verbose_name='tags', max_length=128, blank=True)
    aboutMe = models.TextField(verbose_name='about me', max_length=512, blank=True)
    gender = models.CharField(verbose_name='gender', max_length=1, choices=Gender_Choices, blank=True)

    @receiver(post_save, sender=TravelUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            TravelUserProfile.objects.create(user=instance)

    @receiver(post_save, sender=TravelUser)
    def save_user_profile(sender, instance, **kwargs):
        instance.traveluserprofile.save()




