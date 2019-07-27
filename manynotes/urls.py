from django.conf.urls import url
from django.urls import path
from . import views
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# app_name = "manynotes"

urlpatterns = [
    path("", views.home, name='home'),
    path("base/", views.base, name="base"),
    path('upload/', views.upload, name="upload"),
    path('notes/', views.notes_list, name="notes_list"),
    path('note/<int:pk>/', views.delete_notes, name='delete_notes'),
    path('categories/', views.categories, name='categories'),
    path('notes/upload/', views.upload_notes, name="upload_notes"),
    path("logout/", views.logout_request, name="logout"),
    path("login/", views.login_request, name="login"),
    url(r'^results/$', views.search, name="search"),
    url(r'^dzieciecy/$', views.category_1, name="category1"),
    url(r'^mieszany/$', views.category_2, name="category2"),
    url(r'^zenski/$', views.category_3, name="category3"),
    url(r'^warsztaty/$', views.category_4, name="category4"),
    url(r'^meski/$', views.category_5, name="category5"),
    url(r'^favicon\.ico$',RedirectView.as_view(
        url='https://cdn.pixabay.com/photo/2017/01/09/20/11/music-1967480_960_720.png')),
]
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
