from django.contrib import admin
from home1.models import Book,Author,Genre, Customer

# Register your models here.
#admin.site.register(Book)
# admin.site.register(Author)
#admin.site.register(Genre)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields=('id','name')
    fields=[('name','purchase_date'),('genre','author')]
    list_filter=('name','purchase_date',('author',admin.RelatedOnlyFieldListFilter))
    list_filter=('name','purchase_date','author')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass
