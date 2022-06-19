"""Quick_Tab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from Invoice import views
urlpatterns = [
    path('',views.home,name='home'),
    path('admin/', admin.site.urls),
    path('signup/',views.signupuser,name='signup'),
    path('clients/',views.clients,name='clients'),
    path('logout/',views.logoutuser,name='logoutuser'),
    path('login/',views.loginuser,name='login'),
    path('add-client/',views.add_client,name="add-client"),
    path('inventory/',views.inventory,name="inventory"),
    path('add_invoice/', views.add_invoice, name='add_invoice'),
    path('to-pdf', views.render_pdf_view, name='to_pdf'),
    
]
