from django.contrib import admin
from django.urls import path,include
from quran import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.Home,name='home'),
    path('surah',views.surah,name='surah'),
    path('<int:surah_number>/',views.surah_detail,name='surahdetail'),
    path('juz',views.juz,name='juz'),
    path('juz/<int:juz_number>/',views.juz_detail,name='juzdetail'),
    path('wadu/',views.wadu_view,name='wadu')
    
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
