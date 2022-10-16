# imports
```python
from albums.models import Album
from artists.models import Artist
import datetime
```
# create some artists
```python

artist1 = Artist.objects.create(stage_name="ahmed",social_link = "www.example.com")

artist2 = Artist.objects.create(stage_name="mohamed",social_link = "www.example.com")

artist3 = Artist.objects.create(stage_name="adham",social_link = "www.example.com")

artist4 = Artist.objects.create(stage_name="eslam",social_link = "www.example.com")
```
# list down all artists
```python

Artist.objects.all().values()

<QuerySet [{`id`: 1, `stage_name`: 'ahmed', `social_link`: 'www.example.com'}, {`id`: 2, `stage_name`: 'mohamed', `social_link`: 'www.example.com'}, {`id`: 3, `stage_name`: 'adham', `social_link`: 'www.example.com'}, {`id`: 4, `stage_name`: 'eslam', `social_link`: 'www.example.com'}]>
```

# list down all artists sorted by name
```python

Artist.objects.all().order_by('stage_name').values()

<QuerySet [{`id`: 3, `stage_name`: 'adham', `social_link`: 'www.example.com'}, {`id`: 1, `stage_name`: 'ahmed', `social_link`: 'www.example.com'}, {`id`: 4, `stage_name`: 'eslam', `social_link`: 'www.example.com'}, {`id`: 2, `stage_name`: 'mohamed', `social_link`: 'www.example.com'}]>

```

# list down all artists whose name starts with `a`

```python

Artist.objects.all().filter(stage_name__startswith='a').values()

<QuerySet [{`id`: 1, `stage_name`: 'ahmed', `social_link`: 'www.example.com'}, 
             {`id`: 3, `stage_name`: 'adham', `social_link`: 'www.example.com'}]>

```
# in 2 different ways, create some albums and assign them to any artists

## first way
```python

Album.objects.create(artist = artist1,name='short life',release_datetime=datetime.date(2022, 5, 1),cost = 606.49)
Album.objects.create(artist = artist2,name='long life',release_datetime=datetime.date(2022, 10, 15),cost = 66.5)
Album.objects.create(artist = artist3,name='hello world',release_datetime=datetime.date(2022, 10, 25),cost = 166.5)
Album.objects.create(artist = artist3,name='half life',release_datetime=datetime.date(2022, 10, 12),cost = 155.99)
Album.objects.create(artist = artist1,name='no life',release_datetime=datetime.date(2021, 6, 12),cost = 132)

```
## second way

```python

artist1.albums.create(name = "short life",release_datetime=datetime.date(2022, 5, 1),cost = 606.49)
artist2.albums.create(name='long life',release_datetime=datetime.date(2022, 10, 15),cost = 66.5)
artist3.albums.create(name='hello world',release_datetime=datetime.date(2022, 10, 25),cost = 166.5)
artist3.albums.create(name='half life',release_datetime=datetime.date(2022, 10, 12),cost = 155.99)
artist1.albums.create(name='no life',release_datetime=datetime.date(2021, 6, 12),cost = 132)

```
# get the latest released album
```python

latestAlbum = Album.objects.all().order_by('-release_datetime').first()
print(latestAlbum.id,latestAlbum.name,latestAlbum.release_datetime)

3 hello world 2022-10-25 00:00:00+00:00

```
# get all albums released before today
```python

albumsBeforeToday = Album.objects.all().filter(release_datetime__lt=datetime.date.today())

for album in albumsBeforeToday:
   print(album.id,album.name,album.release_datetime)

1 short life 2022-05-01 00:00:00+00:00
2 long life 2022-10-15 00:00:00+00:00
4 half life 2022-10-12 00:00:00+00:00
5 no life 2021-06-12 00:00:00+00:00

```
# get all albums released today or before but not after today

```python

albumsBeforeOrToday = Album.objects.all().filter(release_datetime__lte=datetime.date.today())

for album in albumsBeforeOrToday:
   print(album.id,album.name,album.release_datetime)
   
1 short life 2022-05-01 00:00:00+00:00
2 long life 2022-10-15 00:00:00+00:00
4 half life 2022-10-12 00:00:00+00:00
5 no life 2021-06-12 00:00:00+00:00

```

# count the total number of albums

```python
Album.objects.count()
6
```
# in 2 different ways, for each artist, list down all of his/her albums

## first way 
```python
artists = Artist.objects.all()
for artist in artists:
artist.albums.all()

<QuerySet [<Album: Album object (1)>, <Album: Album object (5)>]>
<QuerySet [<Album: Album object (2)>]>
<QuerySet [<Album: Album object (3)>, <Album: Album object (4)>]>
<QuerySet []>

```
## second way

```python
artists = Artist.objects.all()
for artist in artists:
Album.objects.filter(artist=artist)

<QuerySet [<Album: Album object (1)>, <Album: Album object (5)>]>
<QuerySet [<Album: Album object (2)>]>
<QuerySet [<Album: Album object (3)>, <Album: Album object (4)>]>
<QuerySet []>

```
# list down all albums ordered by cost then by name (cost has the higher priority)

```python 
sortedAlbums = Album.objects.all().order_by('name').order_by('cost') 
for album in sortedAlbums:
    print(album.id,album.cost,album.name)

2 66.5 long life
5 132.0 no life
4 155.99 half life
3 166.5 hello world
1 606.49 short life

```