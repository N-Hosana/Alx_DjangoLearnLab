from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
class Book(models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 100)
    publication_year = models.IntegerField()
    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"
# Create your models here.

class CustomUserManager(BaseUserManager):
	def create_user(self,date_of_birth,profile_photo,**extra_fields):
		if not date_of_birth:
			raise ValueError("Fill the date of birth field")
		if not profile_photo:
			raise ValueError("Upload the profile photo in the field")
		user = self.model(date_of_birth = date_of_birth, profile_photo = profile_photo,**extra_fields)
		user.save(using = self._db)
		return user

	def create_superuser(self,date_of_birth,profile_photo,**extra_fields):
		extra_fields.setdefault('is_staff',True)
		extra_fields.setdefault('is_superuser',True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError("The super user must have is_staff = True")

		if extra_fields.get('is_superuser') is not True:
			raise ValueError("The super user must have is_superuser = True")

		return sel.create_user(self,date_of_birth,profile_photo,**extra_fields)

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    # Specify unique related names to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name="customuser_groups",
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name="customuser_permissions",
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    objects = CustomUserManager()

    #Creating custom permissions
    class Meta:
        permissions = [
                    ("can_view","Can view the books"),
                    ("can_create", "Can Create the new user"),
                    ("can_edit","Can edit the details of the book"),
                    ("can_delete","Can delete any details of the book")
                ]


from django.conf import settings

# Updating the app to use the custom user model
class UpdateModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
