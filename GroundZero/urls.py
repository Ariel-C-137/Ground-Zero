from django.urls import path
from . import views

urlpatterns = [
   path('', views.landing_page, name='landing_page'),
    path('our-jobs/', views.our_jobs, name='our_jobs'),
    path('paintings/', views.paintings, name='paintings'),
    path('sculptures/', views.sculptures, name='sculptures'),
    path('goldsmithing/', views.goldsmithing, name='goldsmithing'),
    path('fabrics/', views.fabrics, name='fabrics'),
    path('know-us/', views.know_us, name='know_us'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('error/', views.error_view, name='error'),
    path('artist/<int:pk>/', views.artist_detail, name='artist_detail'),
    path('search/', views.search_results, name='search_results'),
]