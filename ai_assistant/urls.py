from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),  # Include the chat app URLs
    path('', RedirectView.as_view(url='/chat/')),  # Redirect homepage to /chat/
]
