import datetime
from django.db import models
from django.shortcuts import reverse
from hitcount.models import HitCount
from django.contrib.contenttypes.fields import GenericRelation
from users.models import MyUser

YEAR_CHOICES = [(r, r) for r in range(1984, datetime.date.today().year+1)]

class Genres(models.Model):
    genre = models.CharField(max_length=10, primary_key=True)

    class Meta:
        verbose_name_plural = "Genres"
        ordering = ('genre',)

    def __str__(self):
        return self.genre

    def get_absolute_url(self):
        return reverse('music:genre', kwargs={'pk': self.pk})

def get_default_artist_image():
    return "img/artist.jpg"

def get_artist_image_path(instance, filename):
    return '{0}/{1}/{2}'.format('artist', instance.artist_name, filename)

class Artist(models.Model):
    artist_name = models.CharField(max_length=30, primary_key=True)
    artist_pic = models.ImageField(upload_to=get_artist_image_path, blank=True, default=get_default_artist_image)
    about = models.TextField(max_length=400, default='', blank=True)

    class Meta:
        ordering = ('artist_name',)
        verbose_name_plural = "Artist"

    def get_absolute_url(self):
        return reverse('music:artistdetail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.artist_name

def get_default_album_image():
    return "img/album.jpg"

def get_album_image_path(instance, filename):
    return '{0}/{1}/{2}'.format('album', instance.name, filename)

class Album(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, primary_key=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album_pic = models.ImageField(upload_to=get_album_image_path, blank=True, default=get_default_album_image)
    genre = models.ManyToManyField(Genres)
    release_year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    created_date = models.DateTimeField(verbose_name='date created', auto_now_add=True)
    about = models.TextField(max_length=400, default=name)
    full_album = models.FileField(upload_to='album zip', blank=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')

    class Meta:
        ordering = ('-created_date',)
        verbose_name_plural = "Album"

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

class Album_song(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True)
    num = models.IntegerField(blank=True)
    name = models.CharField(max_length=100, primary_key=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist = models.ManyToManyField(Artist, related_name='album_songs')
    song_file = models.FileField(upload_to='albumsong', blank=True)
    genre = models.ManyToManyField(Genres)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Album_song"

    def __str__(self):
        return self.name + '  -  '  + self.album.name

class Song(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, primary_key=True)
    artist = models.ManyToManyField(Artist)
    song_pic = models.ImageField(upload_to='song_pic', blank=True)
    song_file = models.FileField(upload_to='song', blank=True)
    created_date = models.DateTimeField(verbose_name='date created', auto_now_add=True)
    genre = models.ManyToManyField(Genres)

    class Meta:
        ordering = ('-created_date',)
        verbose_name_plural = "Song"

    # def get_absolute_url(self):
    #     return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True)
    text = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_on',)
        verbose_name_plural = "Comment"

    def __str__(self):
        return self.artist.artist_name + '  -  ' +  self.user.username

