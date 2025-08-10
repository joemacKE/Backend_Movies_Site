# from django.shortcuts import render
# from django.http import request, JsonResponse
# from .models import Movie

# def movie_list(request):
#     movies = Movie.objects.all()
#     data = {"movies": list(movies.values())}
#     return JsonResponse(data)

# def movie_detail(request, pk):
#     movie = Movie.objects.get(pk=pk)
#     print(movie)
#     data = {
#         'name':movie.name,
#         'description': movie.description,
#             'is_active': movie.is_active,    }
#     return JsonResponse(data)


# # Create your views here.
