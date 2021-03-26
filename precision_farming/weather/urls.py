from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/',views.api,name='sac'),
    path('weather_report/',views.weather_report,name='wr'),
    path('predict_crop/',views.crop_report,name='pc'),
    path('',views.working,name='work')
]
