
from django.conf.urls import url
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('programe/', include('prog_app.urls'))
    url(r''   , views.programe1 , name='programe1'),
    url(r''   , views.programe2 , name='programe2'),
    url(r''   , views.programe3 , name='programe3'),
    url(r''   , views.programe4 , name='programe4'),
    url(r''   , views.programe5 , name='programe5'),
]
