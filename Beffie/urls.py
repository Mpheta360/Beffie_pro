"""
URL configuration for Beffie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from .import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index.home, name='Home'),
    path("products/<int:id>", index.details, name="Pdetails"),
    path('why-choose-us/', index.choose, name='Choose'),
    path('services/', index.service, name='Service'),
    path('about-us/', index.about, name='About'),
    path('our-products/', index.product, name='Product'),
    path('our-gallery/', index.gallery, name='Gallery'),
    path('contact-us/', index.contact, name='Contact'),
    path('login/', index.login, name='Login'),
    path('blocks/', index.block, name='Block'),
    path('pavers/', index.paver, name='Paver'),
    path('slabs/', index.slab, name='Slab'),
    path('logout/', index.out, name='Logout'),
    path('sign-up/', index.lowani, name='Lowani'),
    path('loved-products/', index.lovedproducts, name='Loved-products'),
    path('dashboard/', index.dashboard, name='Dashboard'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
    document_root=settings.MEDIA_ROOT)

