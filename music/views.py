import django
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.db.models import Q
from django.urls import reverse_lazy
from .forms import CommentForm, ArtistEditForm, AlbumForm
from .models import Artist, Album, Song, Genres, Album_song

class IndexView(generic.ListView):
    model = Album
    template_name = 'music/index.html'
    context_object_name = 'albums'
    queryset = Album.objects.all()[1:4]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['taylor_swift'] = Album.objects.filter()[4:5].get()
        context['trending'] = Album.objects.get(name='Revival')
        context['songs'] = Song.objects.all().order_by('-created_date')[:4]
        context['genres'] = Genres.objects.all()[:5]
        context['artists'] = Artist.objects.all()[0:6]
        context['trents'] = Album.objects.all()[4:10]
        context['playing'] = Album_song.objects.get(name='Chandelier')
        return context

class AlbumView(generic.ListView):
    model = Album
    paginate_by = 12
    template_name = 'music/albums.html'
    context_object_name = 'albums'
    # queryset = Album.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk_ = self.kwargs.get("pk")
        context['album'] = Album.objects.filter(genre=pk_)
        context['genre'] = Genres.objects.all()
        return context

class ArtistView(generic.ListView):
    model = Artist
    paginate_by = 15
    template_name = 'music/artists.html'
    context_object_name = 'artists'
    # queryset = Artist.objects.all()

class AlbumDetailView(generic.DetailView):
    model = Album
    template_name = 'music/albumdetail.html'
    context_object_name = 'album'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk_ = self.kwargs.get("pk")
        album_view = get_object_or_404(Album, pk=pk_)
        album_view.views += 1  # Increase view count
        album_view.save()
        context['albums_song'] = Album_song.objects.filter(album_id=pk_).order_by('num')
        context['song'] = Album_song.objects.filter(name=pk_)
        return context

class ArtistDetailView(generic.DetailView):
    model = Artist
    template_name = 'music/artistdetail.html'
    context_object_name = 'artists'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk_ = self.kwargs.get("pk")
        context['albums'] = Album.objects.filter(artist_id=pk_).order_by('release_year')
        context['songs'] = Song.objects.filter(artist=pk_)
        context['artist'] = Artist.objects.filter(artist_name=pk_)
        return context

class GenreView(generic.DetailView):
    model = Genres
    template_name = 'music/genre.html'
    context_object_name = 'genre'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk_ = self.kwargs.get("pk")
        context['album'] = Album.objects.filter(genre=pk_)
        return context

class GenresView(generic.ListView):
    model = Genres
    paginate_by = 15
    template_name = 'music/genres.html'
    context_object_name = 'genres'

class AlbumCreate(generic.CreateView):
    model = Album
    fields = ['name', 'artist', 'album_pic', 'genre']
    template_name = 'music/add.html'
    success_url = reverse_lazy('music:index')

class AlbumDelete(generic.DeleteView):
    model = Album
    pk_url_kwarg = 'pk'
    template_name = 'music/delete.html'
    success_url = reverse_lazy('music:index')

class ArtistEdit(generic.UpdateView):
    model = Artist
    template_name = 'music/artistedit.html'
    form_class = ArtistEditForm
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('music:artists')

class AlbumEdit(generic.UpdateView):
    model = Album
    template_name = 'music/albumedit.html'
    form_class = AlbumForm
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('music:albums')

class PostDetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'
    context_object_name = 'album'
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context.update({
            'popular_albums': Album.objects.order_by('-hit_count_generic__hits')[:3],
        })
        return context

class SearchResultsView(generic.ListView):
    template_name = 'music/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Album.objects.filter(Q(name__icontains=query) | Q(artist__artist_name__icontains=query))
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        context['object_list2'] = Song.objects.filter(Q(name__icontains=query) | Q(artist__artist_name__icontains=query))
        context['object_list1'] = Album_song.objects.filter(Q(name__icontains=query) | Q(artist__artist_name__icontains=query))
        return context

def custom_page_not_found(request):
    return django.views.defaults.page_not_found(request, None, template_name='404.html')