
from django.contrib import admin
from django.urls import path, include


#btre/
urlpatterns = [
    
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),

]
 