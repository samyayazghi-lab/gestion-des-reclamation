from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from reclamations import views  # <-- ADD THIS IMPORT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reclamations.urls')),
    path('accounts/', include('accounts.urls')),
    
    # CHAT - ADD DIRECTLY HERE
    path('chat/', views.chat_view, name='chat'),
    path('chat/api/', views.chat_api, name='chat_api'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)