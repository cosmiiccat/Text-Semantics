from django.urls import path
from . import views 


urlpatterns = [
    path("ensure", views.ensure, name="ensure"),

    path("similarity-score/overall", views.similarity_score, name="overall"),
    path("similarity-score/token", views.token_score, name="token"),
    path("similarity-score/paragraph", views.paragraph_score, name="paragraph"),
    path("similarity-score/embedding", views.embedding_score, name="embedding"),
]