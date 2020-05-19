
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('testpage', TemplateView.as_view(template_name='pages/page.html')),
    path('admin/', admin.site.urls),
    path('quote/', include('quotes.urls')),
    path('', include('pages.urls')),
]
