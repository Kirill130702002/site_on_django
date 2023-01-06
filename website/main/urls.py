from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

#demand - востребованность
urlpatterns = [
    path('', views.index, name='home'),
    path('demand', views.demand, name='demand'),
    path('geography', views.geography, name='geography'),
    path('skills', views.skills, name='skills'),
    path('recent_vacancies', views.recent_vacancies, name='recent_vacancies'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
