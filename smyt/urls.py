from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from app.views import DataView, StructureDataView,  IndexView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'smyt.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view(), name='author_add'),
    url(r'^api/structure/', StructureDataView.as_view(),
        name='structure-date-view'),
    url(r'^api/data/', DataView.as_view(), name='date-view'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
