# Generated by Django 3.1 on 2022-05-13 20:25

from django.db import migrations, models
import music.models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20200727_2311'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genres',
            options={'ordering': ('genre',), 'verbose_name_plural': 'Genres'},
        ),
        migrations.AlterField(
            model_name='album',
            name='release_year',
            field=models.IntegerField(choices=[(1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], default=2022),
        ),
        migrations.AlterField(
            model_name='artist',
            name='artist_pic',
            field=models.ImageField(blank=True, default=music.models.get_default_artist_image, upload_to=music.models.get_artist_image_path),
        ),
    ]
