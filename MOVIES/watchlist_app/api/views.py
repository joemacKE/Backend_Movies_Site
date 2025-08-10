from watchlist_app.models import WatchList, StreamPlatform, Review
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from watchlist_app.api.serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
from rest_framework import status
from rest_framework import generics
# from rest_framework import mixins


#######----------------GENERIC API VIEW CLASS-----------#####
class ReviewList(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(Watchlist=pk)

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = WatchList.objects.get(pk=pk)
        serializer.save(watchlist=watchlist)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer






###-------------------GENERIC VIEWS WITH MIXINS-------------####
# class ReviewwList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#         queryset = Review.objects.all()
#         serializer_class = ReviewSerializer

#         def get(self, request, *args, **kwargs):
#             return self.list(request, *args, **kwargs)
        
#         def post(self, request, *args, **kwargs):
#             return self.create(request, *args, **kwargs)

# class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
# ###-------------------------------------------------------------------###


###---------CLASS BASED VIEWS------------------------------####
class StreamPlatformListAV(APIView):
    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

class StreamPlatformDetailAV(APIView):
    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error': "the streaming platform not found"}, status= status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(platform)
        return Response(serializer.data)
    
    def post(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error': 'Stream platform not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error': 'Stream platform not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    def delete(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({"error": "Stream platform not found"})
        StreamPlatform.delete()
        return Response(statu=status.HTTP_204_NO_CONTENT)

class WatchListAPIView(APIView):
    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class WatchListDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            movies = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error': "Movie does not exist"})
        serializer = WatchListSerializer(movies)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            movies = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error': "movie does not exist"})
        serializer = WatchListSerializer(movies, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({"error": "Movie not found"})
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#####-----------------------------------------------------------########






###------------------FUNCTION BASED VIEWS--------------------##########
# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == "GET":
#         try:
#             movie = Movie.objects.all()
#         except Movie.DoesNotExist:
#             return Response({'error': 'Movie Not Found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = WatchListSerializer(movie, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     if request.method == "POST":
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail(request, pk):

#     if request.method == "GET":
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
    
#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == 'DELETE':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'error': 'Movie you are looking for does not exist'})
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#  ####-----------------------------------------------------------########



# Create your views here.
