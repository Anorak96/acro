from django.urls import path
from . import views

app_name = 'music'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('album/<pk>', views.AlbumDetailView.as_view(), name='detail'),
    path('albums', views.AlbumView.as_view(), name='albums'),
    path('album/add', views.AlbumCreate.as_view(), name='add'),
    path('album/delete/<pk>', views.AlbumDelete.as_view(), name='delete'),
    path('album/<pk>/edit', views.AlbumEdit.as_view(), name='album_edit'),

    path('artist/<pk>', views.ArtistDetailView.as_view(), name='artist'),
    path('artists', views.ArtistView.as_view(), name='artists'),
    path('artist/<pk>/edit', views.ArtistEdit.as_view(), name='artist_edit'),

    path('search', views.SearchResultsView.as_view(), name='search_results'),
    path('404', views.custom_page_not_found, name='error'),

    path('genre/<pk>', views.GenreView.as_view(), name='genre'),
    path('genres', views.GenresView.as_view(), name='genres'),

]
