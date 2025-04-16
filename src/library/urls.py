from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'author-profiles', AuthorProfileViewSet)
router.register(r'publishers', PublisherViewSet)
router.register(r'publications', PublicationViewSet)
router.register(r'books', BookViewSet)

urlpatterns = router.urls
