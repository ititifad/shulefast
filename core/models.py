from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from embed_video.fields import EmbedVideoField

class SchoolManager(models.Manager):
    def get_queryset(self, user):
        return super().get_queryset().filter(user=user)


# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='regioncategory')

    def __str__(self):
        return f'{self.name} - {self.region.name}'
    
class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategory')

    def __str__(self):
        return f'{self.name} - {self.category.name} - {self.category.region.name}'
    

class JoiningForm(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/')

    def __str__(self):
        return f'{self.title} - {self.file}'

class School(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='logos/')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='schoolsubcat')
    phone_number1 = models.CharField(max_length=255, help_text="nambari ya simu")
    phone_number2 = models.CharField(max_length=255, help_text="nambari ya simu")
    email = models.EmailField(null=True, blank=True)
    whatsapp_number = models.CharField(max_length=255, null=True, help_text="namba ya whatsapp")
    location = models.CharField(max_length=255, help_text="mahali shule ilipo")
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_verified = models.BooleanField(default=True)
    # objects = SchoolManager()


    def __str__(self):
        return self.name
    

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('school_detail', kwargs={'slug': self.slug})

class SchoolImage(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True,
                              related_name='schoolimages')
    images = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.school.name


class SchoolGallery(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True,
                              related_name='schoolgallery')
    images = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.school.name
    
class SchoolJoining(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True,
                              related_name='schooljoining')
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/')
    show_file = models.BooleanField(default=True)

    def __str__(self):
        return self.school.name


class OpeningHours(models.Model):
    WEEKDAYS = [
    ('monday', "Monday"),
    ('tuesday', "Tuesday"),
    ('wednesday', "Wednesday"),
    ('thursday', "Thursday"),
    ('friday', "Friday"),
    ('saturday', "Saturday"),
    ('sunday', "Sunday"),
]


    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='openinghours')
    weekday = models.CharField(max_length=20,choices=WEEKDAYS)
    from_hour = models.TimeField(blank=True)
    to_hour = models.TimeField(blank=True)

    

    def __str__(self):
        return "%s %s (%s - %s)" % (self.school, self.weekday, self.from_hour, self.to_hour)


class SchoolAds(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='schoolads')
    title = models.CharField(max_length=255, null=True)
    description = models.TextField()
    file_upload = models.FileField(upload_to='ads/')
    updated = models.DateTimeField(auto_now=True)
    date_added = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.school.name
    

class SchoolAcademic(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True,
                              related_name='schoolacademics')
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/')

    def __str__(self):
        return self.school.name
    


class UserFeedback(models.Model):
    name = models.CharField(max_length=255)
    feedback_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.created_at}"
    

class SchoolCalendar(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True,
                              related_name='schoolacalendar')
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.school.name
    


class SchoolVideo(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True,
                              related_name='schoolvideos')
    # title = models.CharField(max_length=255)
    video = EmbedVideoField()

    def __str__(self):
        return self.school.name