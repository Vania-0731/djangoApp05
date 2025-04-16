from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path, include
from library import views

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'author-profiles', AuthorProfileViewSet)
router.register(r'publishers', PublisherViewSet)
router.register(r'publications', PublicationViewSet)
router.register(r'books', BookViewSet)


urlpatterns = [
    # Templates
    path('categories/', views.categories_view, name='categories'),
    path('categories/<slug:slug>/', views.category_detail_view, name='category_detail'),

    # API
    path('api/', include(router.urls)),
]
