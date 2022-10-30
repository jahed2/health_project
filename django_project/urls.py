"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from Patients import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", include("posts.urls")),
    path("contact/", include("Contact.urls")),
    path("noc/", include("NOC.urls")),
    path("publications/", include("Publications.urls")),
    path("research/", include("Research.urls")),
    path("investigation/", include("Investigations.urls")),
    path("gallary/", include("gallary.urls")),
    path("ict/", include("ICT.urls")),
    path("link/", include("links.urls")),
    path("site/", include("Sitemap.urls")),
    path("departments/", include("Departments.urls")),
    path('patient/', views.add_show, name="addandshow"),
    path('delete/<int:id>/', views.delete_data, name="deletedata"),
    path('<int:id>/', views.update_data, name="updatedata"),
    path('order/', include("orders.urls")),
    path('circular/', include("circulars.urls")),
    path('notice/', include("notice.urls")),
    path('resource/', include("resource.urls")),
    path("", include("Home.urls")),

]

if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
