from django.urls import path
from assets import views


app_name = 'assets'


urlpatterns = [
    path('test/', views.test, name='test'),
    path('report/', views.report, name='report'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('index/', views.index, name='index'),
    path('detail/<int:asset_id>/', views.detail, name='detail'),
    path('test1/', views.test1, name="test1"),
    path('txinfo/', views.txinfo, name="txinfo"),
    path('sintask/', views.sintask, name='sintask'),
    path('multtask/', views.multtask, name='multtask'),
    path('', views.dashboard),
]