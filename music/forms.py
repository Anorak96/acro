from django import forms
from .models import Album, Song, Artist, Comment

class AlbumForm(forms.ModelForm):
    class Meta():
        model = Album
        fields = ['name', 'artist', 'album_pic', 'genre']

class SongForm(forms.Form):
    class Meta():
        model = Song
        song_file = forms.FileField()

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['artist_name']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['artist', 'text']

class ArtistEditForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['artist_name', 'artist_pic', 'about']
