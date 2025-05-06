from django.contrib import admin
from django.utils.html import format_html
from .models import Service, BlogPost, ContactMessage, TeamMember

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created', 'updated')
    list_filter = ('status', 'created')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created', 'updated')
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('title', 'slug', 'status')
        }),
        ('محتوا', {
            'fields': ('description', 'short_description')
        }),
        ('تصاویر', {
            'fields': ('icon', 'image')
        }),
        ('تاریخ‌ها', {
            'fields': ('created', 'updated'),
            'classes': ('collapse',)
        }),
    )

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'publish_date')
    list_filter = ('status', 'publish_date', 'author')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created', 'updated')
    date_hierarchy = 'publish_date'
    filter_horizontal = ()
    raw_id_fields = ('author',)
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # اگر در حال ایجاد پست جدید است
            obj.author = request.user
        super().save_model(request, obj, form, change)

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'status', 'created')
    list_filter = ('status', 'created')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('name', 'email', 'phone', 'subject', 'message', 'ip_address', 'created')
    
    def has_add_permission(self, request):
        return False  # امکان افزودن پیام جدید از طریق ادمین را غیرفعال می‌کند

class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'is_active', 'order')
    list_editable = ('order', 'is_active')
    search_fields = ('name', 'position')
    readonly_fields = ('image_preview',)
    
    def image_preview(self, obj):
        return format_html('<img src="{}" width="150" />'.format(obj.image.url) if obj.image else 'بدون تصویر')
    image_preview.short_description = 'پیش‌نمایش تصویر'

admin.site.register(Service, ServiceAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)

# admin.py
admin.site.site_header = 'پنل مدیریت زامیتک'
admin.site.site_title = 'سامانه مدیریت محتوای زامیتک'
admin.site.index_title = 'به پنل مدیریت زامیتک خوش آمدید'


# admin.py
from django.contrib import messages

def make_published(modeladmin, request, queryset):
    updated = queryset.update(status='published')
    modeladmin.message_user(request, f'{updated} مورد با موفقیت منتشر شد.', messages.SUCCESS)
make_published.short_description = 'انتشار موارد انتخاب شده'

def make_draft(modeladmin, request, queryset):
    updated = queryset.update(status='draft')
    modeladmin.message_user(request, f'{updated} مورد به پیش‌نویس تبدیل شد.', messages.WARNING)
make_draft.short_description = 'تبدیل به پیش‌نویس'

class BlogPostAdmin(admin.ModelAdmin):
    actions = [make_published, make_draft]
    # بقیه تنظیمات...