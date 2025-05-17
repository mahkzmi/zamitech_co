from django.contrib import admin
from .models import TeamMember, BlogPost, ProductInfo

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')
    prepopulated_fields = {"slug": ("title",)}

@admin.register(ProductInfo)
class ProductInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'updated_date')
