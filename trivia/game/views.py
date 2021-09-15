from .models import Game, Question, Result
from .serializers import GamesSerializer, QuestionsSerializer, ResultsSerializer
from rest_framework import viewsets

class GamesViewSet(viewsets.ModelViewSet):
    serializer_class = GamesSerializer
    queryset = Game.objects.all()
        
class QuestionsViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionsSerializer
    def get_queryset(self):
        return Question.objects.filter(game=self.kwargs['game_pk'])
    
class ResultsViewSet(viewsets.ModelViewSet):
    serializer_class = ResultsSerializer
    def get_queryset(self):
        return Result.objects.filter(game=self.kwargs['game_pk'])