
from django.views.generic.base import TemplateView
from quotes.views import Register


from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('rgister/success/',TemplateView.as_view(template_name="registration/success.html"), name='register-success'),
    path('register/', Register.as_view(), name='register'),
    path('testpage', TemplateView.as_view(template_name='pages/page.html')),
    path('admin/', admin.site.urls),
    path('quote/', include('quotes.urls')),
    path('', include('django.contrib.auth.urls')),
    path('', include('pages.urls')),
]
