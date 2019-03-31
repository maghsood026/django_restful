from rest_framework.generics import \
    (ListAPIView,
     RetrieveAPIView,
     CreateAPIView,
     DestroyAPIView,
     UpdateAPIView,
     )
from .serializer import ArticleSerializer
from .models import Article


class ArticleViewToGet(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleViewToPost(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleViewToUpdate(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleViewToDelete(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
