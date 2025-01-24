"""mysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # http://127.0.0.1:8000/page/2003/
    path('page/2003/', views.page_2003_view),

    path('', views.page_index_view),
    path('page/1/', views.page1_view),
    path('page/2/', views.page2_view),
    path('page/<int:page>/', views.pagen_view),

    re_path(r'^(?P<m>\d{1,2})/(?P<op>\w+)/(?P<n>\d{1,2})$', views.cal2_view),
    path('<int:m>/<str:op>/<int:n>', views.cal_view),

    re_path(r'^birthday/(?P<y>\d{4})/(?P<m>\d{1,2})/(?P<d>\d{1,2})$', views.cal_bitrhday_view),
    re_path(r'^birthday/(?P<m>\d{1,2})/(?P<d>\d{1,2})/(?P<y>\d{4})$', views.cal_bitrhday_view),

    path('test_request/', views.test_request),
    path('test_get_post/', views.test_get_post),
    path('test_html_request/', views.test_html_request),
    path('test_html_param/', views.test_html_param),
    path('test_if_for/', views.test_if_for),
    path('test_mycal/', views.test_mycal),

    path('base/', views.base_view, name="base"),
    path('music/', views.music_view),
    path('sport/', views.sport_view),

    path('test/url/', views.test_url),
    path('test_url_result/<int:page>', views.test_url_result, name='tr'),
]
