from django.contrib import admin
from .models import Article,Comment
# Register your models here.

# StackedInline
# each field has its own line :
# class CommentInline(admin.StackedInline):
#     model = Comment
    #  if you wanted no extra fields by default -> extra = 0

#  all model fields appear on one line
#  it shows more information in less space. (Preferred)
class CommentInline(admin.TabularInline):
    model = Comment

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
         CommentInline,
         ]
        
admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment)
