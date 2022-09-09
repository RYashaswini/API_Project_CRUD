from django.urls import path
from apicode import views
from .views import ArticleAPIView, ArticleDetails,ArticleSearch
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('class_article/',ArticleAPIView.as_view()),
    path('class_detail/<int:pk>/', ArticleDetails.as_view()),
   

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)