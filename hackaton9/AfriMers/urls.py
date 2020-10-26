from AfriMers.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='AfriMers-home'),
    path('about/', views.about, name='AfriMers-about'),
    path('account/', views.account, name='AfriMers-account'),
    path('LogIn/', views.LogIn, name='AfriMers-LogIn'),
    path('Groceries/', views.Groceries, name='AfriMers-Groceries'),
    path('Purchase/', views.Purchase, name='AfriMers-Purchase'),

]