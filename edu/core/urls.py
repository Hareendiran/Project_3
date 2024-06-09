from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('',views.home,name=""),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('about-us',views.about_us,name="about-us"),
    path('contact',views.contact,name="contact"),
    path('logout/',views.logout,name="logout"),
    path('chemistry/',include('chemistry.urls')),
    path('biology/',include('biology.urls')),
    path('physics/',include('physics.urls')),
    path('custom/',include('custom.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)