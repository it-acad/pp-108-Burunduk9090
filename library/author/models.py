from django.db import models
from django.urls import reverse

class Author(models.Model):
    """
    This class represents an Author. \n
    Attributes:
    -----------
    param name: Describes name of the author
    type name: str max_length=20
    param surname: Describes last name of the author
    type surname: str max_length=20
    param patronymic: Describes middle name of the author
    type patronymic: str max_length=20
    """
    name = models.CharField(blank=True, max_length=20)
    surname = models.CharField(blank=True, max_length=20)
    patronymic = models.CharField(blank=True, max_length=20)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f"\'id\': {self.pk}, \'name\': \'{self.name}\'," \
               f" \'surname\': \'{self.surname}\', \'patronymic\': \'{self.patronymic}\'"

    def __repr__(self):
        return f"Author(id={self.pk})"

    def get_absolute_url(self):
        return reverse('author_detail', kwargs={'pk': self.pk})

    @staticmethod
    def get_by_id(author_id):
        try:
            return Author.objects.get(pk=author_id)
        except:
            return None

    @staticmethod
    def delete_by_id(author_id):
        try:
            author = Author.objects.get(pk=author_id)
            author.delete()
            return True
        except:
            return False

    @staticmethod
    def create(name, surname, patronymic):
        if name and len(name) <= 20 and surname and len(surname) <= 20 and patronymic and len(patronymic) <= 20:
            author = Author(name=name, surname=surname, patronymic=patronymic)
            author.save()
            return author

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'patronymic': self.patronymic
        }

    def update(self, name=None, surname=None, patronymic=None):
        if name and len(name) <= 20:
            self.name = name
        if surname and len(surname) <= 20:
            self.surname = surname
        if patronymic and len(patronymic) <= 20:
            self.patronymic = patronymic
        self.save()

    @staticmethod
    def get_all():
        return Author.objects.all()
