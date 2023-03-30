from django.contrib import admin

# Register your models here.
from .models import TalkooPalaute, KokousPalaute, Hairioilmoitus

class TalkooPalauteAdmin(admin.ModelAdmin):
    list_display = ('kayttaja', 't_hyvaa', 't_huonoa','t_kehitettavaa', 'arvosana', 'date')
    list_filter = ['date']
    search_fields = ['t_hyvaa', 't_huonoa','t_kehitettavaa', 'arvosana']

admin.site.register(TalkooPalaute, TalkooPalauteAdmin)



class KokousPalauteAdmin(admin.ModelAdmin):
    list_display = ('kayttaja', 'k_hyvaa', 'k_huonoa','k_kehitettavaa', 'arvosana', 'date')
    list_filter = ['date']
    search_fields = ['k_hyvaa', 'k_huonoa','k_kehitettavaa', 'arvosana']

admin.site.register(KokousPalaute, KokousPalauteAdmin)



class HairioilmoitusAdmin(admin.ModelAdmin):
    list_display = ('kayttaja', 'h_huoneisto', 'h_hairionkuvaus','h_hairiontarkennus', 'arvosana', 'date')
    list_filter = ['date']
    search_fields = ['h_huoneisto', 'h_hairionkuvaus','h_hairiontarkennus', 'arvosana']

admin.site.register(Hairioilmoitus, HairioilmoitusAdmin)

