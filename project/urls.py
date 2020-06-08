
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('programs/', include('programs.urls')),
    path('', include('dss_box.urls')),



]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


admin.site.site_header = "Motadamn Admin Panel"
