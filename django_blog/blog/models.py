from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.conf import settings


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, default="man")
    image = models.ImageField(
        default=(
            "profile_pics/default_woman.jpg"
            if gender == "man"
            else "profile_pics/default_man.jpg"
        ),
        upload_to="profile_pics",
    )
    bio = models.TextField(default="")

    def __str__(self) -> str:
        return str(self.username)

    def save(self, *args, **kwargs):
        # Set default image if none provided
        if not self.image:
            default_image = (
                "profile_pics/default_man.jpg"
                if self.gender == "man"
                else "profile_pics/default_woman.jpg"
            )
            self.image.name = default_image  # Assign default image path

        super().save(*args, **kwargs)  # Save the instance first to generate image path

        # Resize image only if it's not a default one (skip resizing default images)
        if self.image and "default_" not in self.image.name:
            img = Image.open(self.image.path)

            # Resize while maintaining aspect ratio
            max_size = (300, 300)
            img.thumbnail(max_size)

            img.save(self.image.path)  # Save optimized image


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
