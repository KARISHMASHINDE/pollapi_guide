from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Poll, Choice
from .serializers import PollSerializer
class PollList(APIView):
    def get(self, request):
        polls = Poll.objects.all()[:20]
        serializer = PollSerializer(polls, many=True).data
        return Response(serializer)
        
class PollDetail(APIView):
    def get(self, request, pk):
        poll = get_object_or_404(Poll, pk=pk)
        serializer = PollSerializer(poll).data
        return Response(serializer)
    
    # def get(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     serializer = CodeSerializer(snippet)
    #     return Response(serializer.data)

    def put(self, request, pk, format=None):
        poll = self.get_object(pk)
        serializer = PollSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        poll = self.get_object(pk)
        poll.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)