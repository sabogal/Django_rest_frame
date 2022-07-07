from django.urls import path
from apps.products.api.views.general_views import MeasureUnitListAPIView,IndicatorUnitListAPIView,CategoryProductUnitListAPIView
from apps.products.api.views.products_views import ProductListAPIView

urlpatterns = [
    path('measure_unit/',MeasureUnitListAPIView.as_view(), name='measure_unit'),
    path('indicator/',IndicatorUnitListAPIView.as_view(), name='indicator'),
    path('category_product/',CategoryProductUnitListAPIView.as_view(), name='category_product'),
    path('product/',ProductListAPIView.as_view(), name='category_product'),]
