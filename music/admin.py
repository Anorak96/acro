from django.contrib import admin
from .models import Artist, Album, Song, Genres, Album_song, Comment

class Album_SongAdmin(admin.ModelAdmin):
    list_display = ('name', 'album', 'artist_display', 'genre_display', )
    list_filter = ('album', 'genre', )
    search_fields = ('name', )
    list_per_page = 20

    def genre_display(self, obj):
        return ", ".join([genr.genre for genr in obj.genre.all()])
    genre_display.short_description = "Genre"

    def artist_display(self, obj):
        return ", ".join([art.artist_name for art in obj.artist.all()])
    artist_display.short_description = "Artist"

class Album_songInline(admin.TabularInline):
    model = Album_song
    extra = 1

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist', 'image_tag', 'genre_display', 'release_year', 'user')
    list_per_page = 20
    fieldsets = [
        (None, {'fields': ['name', 'artist', 'album_pic', 'full_album', 'genre', 'release_year', 'user', 'views']}),
    ]
    list_filter = ('artist', 'genre')
    search_fields = ('name', 'artist',)
    inlines = [Album_songInline]

    def genre_display(self, obj):
        return ", ".join([genr.genre for genr in obj.genre.all()])
    genre_display.short_description = "Genre"

class SongAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist_display', 'genre_display', )
    list_filter = ('artist', 'genre', )
    search_fields = ('name',)
    list_per_page = 20

    def genre_display(self, obj):
        return ", ".join([genr.genre for genr in obj.genre.all()])
    genre_display.short_description = "Genre"

    def artist_display(self, obj):
        return ", ".join([art.artist_name for art in obj.artist.all()])
    artist_display.short_description = "Artist"

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('artist_name', 'about', 'artist_pic')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('artist', 'user_id')
    list_per_page = 20

admin.site.register(Album, AlbumAdmin)
admin.site.register(Album_song, Album_SongAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Genres)
admin.site.register(Comment, CommentAdmin)
