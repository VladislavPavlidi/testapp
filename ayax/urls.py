from django.urls import path, include

from .views import index, realtor_check, RealtorCreateView, RealtorEditView, realtor_search, RealtorDeleteView

urlpatterns = [
    path('delete/<int:pk>/', RealtorDeleteView.as_view(), name='delete'),
    path('search/', realtor_search, name='search'),
    path('edit/<int:pk>/', RealtorEditView.as_view(), name='edit'),
    path('add/', RealtorCreateView.as_view(), name='add'),
    path('realtors/', realtor_check, name='realtor_check'),
    path('', index, name='index'),
]
