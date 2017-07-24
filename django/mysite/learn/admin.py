# coding:utf-8
# Register your models here.
from django.contrib import admin
from .models import Person, Blog


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'pub_date', 'update_time')
    search_fields = ('name',)

    def get_queryset(self, request):
        qs = super(PersonAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(author=request.user)

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super(PersonAdmin, self).get_search_results(request, queryset, search_term)
        try:
            search_term_as_int = int(search_term)
            queryset |= self.model.objects.filter(age=search_term_as_int)
        except:
            pass
        return queryset, use_distinct

    def save_model(self, request, obj, form, change):
        if change:# 更改的时候
            obj_original = self.model.objects.get(pk=obj.pk)
        else:# 新增的时候
            obj_original = None

        obj.user = request.user
        obj.save()

    def delete_model(self, request, obj):
        """
        Given a model instance delete it from the database.
        """
        # handle something here
        obj.delete()


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    search_fields = ('title',)


admin.site.register(Person, PersonAdmin)
admin.site.register(Blog, BlogAdmin)

