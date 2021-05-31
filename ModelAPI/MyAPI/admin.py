from django.contrib import admin
from .models import predictions
# Register your models here.

@admin.register(predictions)
class predictionsModelsAdmin(admin.ModelAdmin):
    list_display = ['id','age','sex','cp','trestbps','restecg','chol','fbs','thalach','exang','oldpeak','slope','ca','thal']
