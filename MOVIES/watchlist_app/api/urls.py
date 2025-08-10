from django.urls import path, include
from watchlist_app.api.views import WatchListAPIView, WatchListDetailAPIView, StreamPlatformListAV, StreamPlatformDetailAV, ReviewList, ReviewDetail

urlpatterns = [
    path('list/', WatchListAPIView.as_view(), name='movie-list'),
    path('<int:pk>/', WatchListDetailAPIView.as_view(), name='movie-detail'),
    path('stream/', StreamPlatformListAV.as_view(), name = "stream-platform"),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name="stram-platform-detail"),
    path('stream/<int:pk>/review-create', ReviewList.as_view(), name='review-list'),

    path('stream/<int:pk>/review', ReviewList.as_view(), name='review-list'),
    path('stream/review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
]
