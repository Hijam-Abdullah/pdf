from . import views
from django.urls import path
urlpatterns = [
    path('',views.pdf, name='pdfmake'),
    path('pdf',views.pdf_create, name='pdfmake'),
    
]
