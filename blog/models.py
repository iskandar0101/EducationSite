from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class CoursePost(models.Model):
    name = models.CharField(max_length=70, verbose_name='Kurs nomi')
    about = models.TextField(verbose_name='Kurs haqida')
    photo = models.ImageField(upload_to='media/', verbose_name='Kurs Rasmi')
    price = models.CharField(max_length=50, verbose_name='Kurs narxi')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqt")
    duration = models.TextField(verbose_name='Kurs davomiyligi')
    modules = models.CharField(max_length=50, verbose_name='Kurs modullari')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'CoursePost'
        managed = True
        verbose_name = 'Kurs'
        verbose_name_plural = 'Kurslar'


class TeachersPost(models.Model):
    name = models.CharField(max_length=70, verbose_name='Ustozning ismi')
    photo = models.ImageField(upload_to='media/', verbose_name='Ustozning rasmi')
    level = models.CharField(max_length=50, verbose_name='Ustozning darajasi')
    about = models.CharField(max_length=300, verbose_name='Ustoz haqida')

    def __str__(self):
        return self.name

    # class Meta:
    #     db_table = 'TeacherPost'
    #     managed = True
    #     verbose_name = 'Ustoz Haqida Post'
    #     verbose_name_plural = 'Ustoz Haqida Posts'


class ContactPage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Contact_Page'
        managed = True
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'


class Plan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=50, default="month")
    certificates = models.BooleanField(default=True)
    full_courses = models.BooleanField(default=True)
    full_modules = models.BooleanField(default=True)
    live_projects = models.BooleanField(default=True)
    support = models.CharField(max_length=100, default="24 x 7 supports")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Plan'
        managed = True
        verbose_name = 'Plan'
        verbose_name_plural = 'Plans'


class ReviewPost(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')
    about = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ReviewPost'
        managed = True
        verbose_name = 'Izoh'
        verbose_name_plural = 'Izohlar'


class Comment(models.Model):
    review = models.ForeignKey(ReviewPost, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

    class Meta:
        db_table = 'Komment'
        managed = True
        verbose_name = 'Komentariya'
        verbose_name_plural = 'Komentariyalar'
