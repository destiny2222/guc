from os import name
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "index"

urlpatterns = [
    path('', views.HomeViews, name='home'),
    path('contact/', views.ContactViews, name='contact'),
    path('profile/', views.profileview, name='profile'),
    path('details/<slug:slug>/', views.detailView, name='details'),
    path('consulting/', views.ConsultingViews, name='consulting'),
    path('publication/', views.publicationViews, name='publication'),
    path('404/', views.error, name='404'),
    # path('cart/', views.cart, name="cart_page"),
    # path('payment/', views.publicationpage, name="payment")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)