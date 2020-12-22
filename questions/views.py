from rest_framework import generics,viewsets
from .models import Question,Answer
from rest_framework.generics import get_object_or_404
from .serializers import QuestionSerializer,AnswerSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadOnly
from rest_framework.exceptions import ValidationError


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated,IsAuthorOrReadOnly]


    def perform_create(self,serializer):
        serializer.save(author = self.request.user)

class CreateAnswerAPI(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self,serializer):
        kwarg_slug = self.kwargs.get("slug")
        question = get_object_or_404(Question,slug = kwarg_slug)

        if question.answers.filter(author=self.request.user).exists():
            raise ValidationError("You have already answered this Question!")

        serializer.save(question=question,author=self.request.user)

class AnswerListAPIView(generics.ListAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        kwarg_slug = self.kwargs.get("slug")
        return Answer.objects.filter(
            question__slug = kwarg_slug
        )