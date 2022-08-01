from fire_situation import views
from django.urls import path

app_name="fire_situation"

urlpatterns = [
      path('',views.detail_main_page,name='situation'),
]
