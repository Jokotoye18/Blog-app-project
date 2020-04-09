from django.contrib import admin
from django.urls import path,include
from django.views.i18n import JavaScriptCatalog


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('comments/', include('django_comments_xtd.urls')),
    path('', include('pages.urls')),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('accounts/', include('accounts.urls')),
    path('article/', include('articles.urls')), 
]
