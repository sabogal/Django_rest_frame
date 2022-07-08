from django.urls import path
from apps.products.api.views.general_views import MeasureUnitListAPIView,IndicatorUnitListAPIView,CategoryProductUnitListAPIView
from apps.products.api.views.products_views import (
    ProductListCreateAPIView, ProductRetriveUpdateDestroyAPIView, )

urlpatterns = [
    path('measure_unit/',MeasureUnitListAPIView.as_view(), name='measure_unit'),
    path('indicator/',IndicatorUnitListAPIView.as_view(), name='indicator'),
    path('category_product/',CategoryProductUnitListAPIView.as_view(), name='category_product'),
    path('product/',ProductListCreateAPIView.as_view(), name='product_create'),
    path('product/retrive-update-destroy/<int:pk>/',ProductRetriveUpdateDestroyAPIView.as_view(), name='retrive-update-destroy'),
]
