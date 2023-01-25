# from rest_framework.views import APIView
from rest_framework import generics
# from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from habittracker.models import Habit, Record
from . import serializers


# # Create your views here.
# class HabitListView(APIView):
#     def get(self, request, format=None):
#         """
#         Return a list of all users.
#         """
#         habits = Habit.objects.all()
#         serializer = serializers.HabitSerializer(habits, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         """
#         Create a new habit for the logged in user
#         """
#         # get the user
#         serializer = serializers.HabitSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(owner=request.user)
#         # create a new habit for that user using the serializer
#         # return the newly created habit
#         return Response(serializer.data)


class HabitListAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.HabitListSerializer

    def get_queryset(self):
        return Habit.objects.all().filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class HabitDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = serializers.HabitSerializer


class RecordAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.RecordSerializer

    def get_queryset(self):
        habit = get_object_or_404(Habit, pk=self.kwargs['habit_pk'])
        return habit.records.all()


class RecordCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.RecordSerializer

    def perform_create(self, serializer):
        habit = get_object_or_404(Habit, pk=self.kwargs['habit_pk'])
        serializer.save(habit=habit)