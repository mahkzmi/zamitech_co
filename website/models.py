from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Service(models.Model):
    STATUS_CHOICES = [
        ('draft', 'پیش‌نویس'),
        ('published', 'منتشر شده'),
    ]
    
    title = models.CharField(max_length=200, verbose_name='عنوان خدمت')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='آدرس URL')
    description = models.TextField(verbose_name='توضیحات کامل')
    short_description = models.CharField(max_length=300, verbose_name='توضیح کوتاه')
    icon = models.CharField(max_length=50, help_text='نام آیکون از فونت Awesome', verbose_name='آیکون')
    image = models.ImageField(upload_to='services/', verbose_name='تصویر شاخص')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name='وضعیت')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')

    class Meta:
        verbose_name = 'خدمت'
        verbose_name_plural = 'خدمات'
        ordering = ['-created']

    def __str__(self):
        return self.title

# models.py
from ckeditor.fields import RichTextField

class BlogPost(models.Model):
    content = RichTextField(verbose_name='محتوا')  
    STATUS_CHOICES = [
        ('draft', 'پیش‌نویس'),
        ('published', 'منتشر شده'),
    ]
    
    title = models.CharField(max_length=200, verbose_name='عنوان مقاله')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='آدرس URL')
    content = models.TextField(verbose_name='محتوا')
    excerpt = models.CharField(max_length=300, verbose_name='چکیده')
    cover_image = models.ImageField(upload_to='blog/', verbose_name='تصویر شاخص')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name='وضعیت')
    publish_date = models.DateTimeField(default=timezone.now, verbose_name='تاریخ انتشار')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        ordering = ['-publish_date']

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    STATUS_CHOICES = [
        ('unread', 'خوانده نشده'),
        ('read', 'خوانده شده'),
        ('replied', 'پاسخ داده شده'),
    ]
    
    name = models.CharField(max_length=100, verbose_name='نام')
    email = models.EmailField(verbose_name='ایمیل')
    phone = models.CharField(max_length=15, blank=True, verbose_name='تلفن')
    subject = models.CharField(max_length=200, verbose_name='موضوع')
    message = models.TextField(verbose_name='پیام')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='unread', verbose_name='وضعیت')
    ip_address = models.GenericIPAddressField(blank=True, null=True, verbose_name='آی‌پی')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ارسال')

    class Meta:
        verbose_name = 'پیام تماس'
        verbose_name_plural = 'پیام‌های تماس'
        ordering = ['-created']

    def __str__(self):
        return f"{self.name} - {self.subject}"

class TeamMember(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام کامل')
    position = models.CharField(max_length=100, verbose_name='سمت')
    bio = models.TextField(verbose_name='بیوگرافی')
    image = models.ImageField(upload_to='team/', verbose_name='تصویر')
    email = models.EmailField(blank=True, verbose_name='ایمیل')
    phone = models.CharField(max_length=15, blank=True, verbose_name='تلفن')
    linkedin = models.URLField(blank=True, verbose_name='لینکدین')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    order = models.PositiveIntegerField(default=0, verbose_name='ترتیب نمایش')

    class Meta:
        verbose_name = 'عضو تیم'
        verbose_name_plural = 'اعضای تیم'
        ordering = ['order']

    def __str__(self):
        return self.name