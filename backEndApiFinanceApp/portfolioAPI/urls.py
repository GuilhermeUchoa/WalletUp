from django.urls import include, path
from . import views
from rest_framework import routers

app_name = 'portfolioAPI'

router = routers.DefaultRouter()
# precisa do basename para reescrever classe na view
router.register(r'ativos', views.AtivosViewSet, basename='ativos')
router.register(r'portfolio', views.PortfolioViewSet, basename='portfolio')

urlpatterns = [
    path('', include(router.urls)),
    path('fileUpload/', views.upload_file, name='FileUpload'),

]
