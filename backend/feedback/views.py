from rest_framework.generics import CreateAPIView
from .models import Feedback
from .serializers import FeedbackSerializer


class FeedbackCreateView(CreateAPIView):

    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer