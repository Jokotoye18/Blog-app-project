from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.views.i18n import JavaScriptCatalog
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from articles.sitemap import ArticleSitemap, StaticViewSitemap

schema_view = get_schema_view(
    openapi.Info(
        title="Jokotoye18 Blog API",
        default_version="v1",
        description="Blog description",
        contact=openapi.Contact(email="jokotoyeademola95@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


sitemaps = {
    'article': ArticleSitemap,
    'staic': StaticViewSitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "sitemap.xml/",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path("accounts/", include("django.contrib.auth.urls")),
    path("comments/", include("django_comments_xtd.urls")),
    path("", include("pages.urls")),
    path("api/", include("articles.api.urls")),
    path("rest-auth/", include("rest_auth.urls")),
    path("rest-auth/registration/", include("rest_auth.registration.urls")),
    path(
        "api/read-docs/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
    path("martor/", include("martor.urls")),
    path("accounts/", include("accounts.urls")),
    path("", include("articles.urls")),
    path("jsi18n/", JavaScriptCatalog.as_view(), name="javascript-catalog"),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = [path("__debug__/", include(debug_toolbar.urls)),] + urlpatterns
