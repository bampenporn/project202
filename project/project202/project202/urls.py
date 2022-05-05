from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from store.views import HomeView, ProductDetail, checkout , add_to_cart,  remove_from_cart, OrderSummaryView, remove_single_from_cart

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomeView.as_view(),name='home'),
    path('add_to_cart/<slug>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove_from_cart'),
    path('remove-single-from-cart/<slug>/',remove_single_from_cart, name='remove_single_from_cart'),
    path('product/<slug>/', ProductDetail.as_view(), name='product'),
    path('order-summary/', OrderSummaryView.as_view(), name='order_summary'),
    path('checkout/', checkout, name='checkout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
