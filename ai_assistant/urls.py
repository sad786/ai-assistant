from django.contrib import admin
from django.urls import path, include

from chat.views import redirect_to_chat

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),
    path('', redirect_to_chat),  # Use the custom view for redirection
]
