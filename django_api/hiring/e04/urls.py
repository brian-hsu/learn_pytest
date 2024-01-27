from rest_framework.routers import DefaultRouter
from rest_framework import routers
from .views import CompanyViewSet

companies_router = routers.DefaultRouter()
companies_router.register(r'companies', viewset=CompanyViewSet, basename='companies')

