from artists.models import Artist
from albums.models import Album, Song
from users.models import UserProfile
import factory
from faker import Faker
from django.contrib.auth import get_user_model
faker = Faker()

from collections.abc import Sequence
from typing import Any

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    username = factory.Faker("user_name")
    email = factory.Faker("email")
    
    @factory.post_generation
    def password(self, create: bool, extracted: Sequence[Any], **kwargs):
        password = (
            extracted
            if extracted
            else factory.Faker(
                "password",
                length=42,
                special_chars=True,
                digits=True,
                upper_case=True,
                lower_case=True,
            ).evaluate(None, None, extra={"locale": None})
        )
        self.set_password(password)


class UserProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserProfile
    user = factory.SubFactory(UserFactory)
    bio = factory.LazyAttribute(lambda _: faker.pystr())


class ArtistFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Artist
    stage_name = factory.LazyAttribute(lambda _: faker.pystr())
    social_link = factory.LazyAttribute(lambda _: faker.url())


class AlbumFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Album
    artist = factory.SubFactory(ArtistFactory)
    name = factory.LazyAttribute(lambda _: faker.pystr())
    release_datetime = factory.LazyAttribute(lambda _: faker.date_time())
    cost = factory.LazyAttribute(lambda _: faker.pyfloat(positive=True))
    is_approved = factory.LazyAttribute(
        lambda _: faker.boolean(chance_of_getting_true=50))


class SongFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Song
    album = factory.SubFactory(AlbumFactory)
    name = factory.LazyAttribute(lambda _: faker.pystr())

