from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(FertilitySheet)
admin.site.register(MaleMedicalHistory)
admin.site.register(WifeExamination)
admin.site.register(Investigation)
admin.site.register(AncOpdFirstBlock)
admin.site.register(GynacOpdFirstBlock)
admin.site.register(AncOpdBlock)
admin.site.register(GynacOpdBlock)
admin.site.register(InfPlanOneFirstBlock)
admin.site.register(InfPlanTwoFirstBlock)
admin.site.register(InfPlanOneBlock)
admin.site.register(InfPlanTwoBlock)
admin.site.register(Usg)
admin.site.register(TtDose)