from django.contrib import admin
from django.db 		import models
from django.contrib.auth.models import User
from .models import Images, Colecoes,ElasUsam,Eventos,Email


class ImagesAdmin(admin.ModelAdmin):
    fields = ('title','slug', 'desc', 'created_date', 'published_date','image','image_thumbnail','created_by')

    def render_change_form(self, request, context, *args, **kwargs):
        context['adminform'].form.fields['created_by'].initial = request.user
        return super(ImagesAdmin, self).render_change_form(request, context, args, kwargs)

class ColecoesAdmin(admin.ModelAdmin):
    fields = ('title','desc','created_date','published_date','galery','created_by',)

    def render_change_form(self, request, context, *args, **kwargs):
        context['adminform'].form.fields['created_by'].initial = request.user
        return super(ColecoesAdmin, self).render_change_form(request, context, args, kwargs) 

class ElasUsamAdmin(admin.ModelAdmin):
    fields = ('title','desc','created_date','published_date','galery','created_by',)
    
    def render_change_form(self, request, context, *args, **kwargs):
        context['adminform'].form.fields['created_by'].initial = request.user
        return super(ElasUsamAdmin, self).render_change_form(request, context, args, kwargs) 

class EventosAdmin(admin.ModelAdmin):
    fields = ('title','desc','date','galery','created_by',)

    def render_change_form(self, request, context, *args, **kwargs):
        context['adminform'].form.fields['created_by'].initial = request.user
        return super(EventosAdmin, self).render_change_form(request, context, args, kwargs) 

class EmailAdmin(admin.ModelAdmin):
    fields = ('full_name','ddd','phone','message','send_date','email',)

admin.site.register(Images, ImagesAdmin)
admin.site.register(Colecoes, ColecoesAdmin)
admin.site.register(ElasUsam, ElasUsamAdmin)
admin.site.register(Eventos, EventosAdmin)
admin.site.register(Email, EmailAdmin)


