from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'questions',views.QuestionViewSet)





urlpatterns = [
    path('',include(router.urls)),
    path("questions/<slug:slug>/answer/",views.CreateAnswerAPI.as_view()),
    path("questions/<slug:slug>/answers/",views.AnswerListAPIView.as_view()),
    
]