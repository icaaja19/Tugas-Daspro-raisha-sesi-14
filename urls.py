from django.contrib import admin
from django.urls import path, include
from polls import views  # Tambahkan ini untuk akses langsung ke views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),  # tetap untuk semua route polls
    
    # Route langsung ke views tanpa prefix 'polls/'
    path('settings/', views.settings_view, name='settings_direct'),
    path('profile/', views.profile, name='profile_direct'),
    path('contact/', views.contact, name='contact_direct'),
    path('address/', views.address, name='address_direct'),
    path('phone/', views.phone, name='phone_direct'),
]
