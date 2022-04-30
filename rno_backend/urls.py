from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import index

admin.site.site_title = 'RnO Automation'
admin.site.site_header = 'RnO Automation Portal'
admin.site.index_title = 'Welcome to RnO Automation Portal'

urlpatterns = [
    path('rnoautomation/admin/', admin.site.urls),
    path('', view=index, name="index"),
    path('accounts/', include('allauth.urls')),
    # path('api-auth/', include('rest_framework.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
