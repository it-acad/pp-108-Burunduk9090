from django.db import models
from django.urls import reverse

class Book(models.Model):
    """
    This class represents a Book. \n
    Attributes:
    -----------
    param name: Describes name of the book
    type name: str max_length=128
    param description: Describes description of the book
    type description: str
    param count: Describes count of the book
    type count: int default=10
    param authors: list of Authors
    type authors: list->Author
    param year_of_publication: Year when the book was published
    type year_of_publication: int
    param date_of_issue: Date when the book was issued
    type date_of_issue: datetime
    """
    name = models.CharField(blank=True, max_length=128)
    description = models.CharField(blank=True, max_length=256)
    count = models.IntegerField(default=10)
    authors = models.ManyToManyField('author.Author', related_name='written_books')
    year_of_publication = models.IntegerField()
    date_of_issue = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f"'id': {self.id}, 'name': '{self.name}', 'description': '{self.description}', 'count': {self.count}, 'authors': {[author.id for author in self.authors.all()]}, 'year_of_publication': {self.year_of_publication}, 'date_of_issue': '{self.date_of_issue}'"

    def __repr__(self):
        return f"Book(id={self.id})"

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'pk': self.pk})

    @staticmethod
    def get_by_id(book_id):
        return Book.objects.get(id=book_id) if Book.objects.filter(id=book_id) else None

    @staticmethod
    def delete_by_id(book_id):
        if Book.get_by_id(book_id) is None:
            return False
        Book.objects.get(id=book_id).delete()
        return True

    @staticmethod
    def create(name, description, count=10, authors=None):
        if len(name) > 128:
            return None

        book = Book()
        book.name = name
        book.description = description
        book.count = count
        if authors is not None:
            for elem in authors:
                book.authors.add(elem)
        book.save()
        return book

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'count': self.count,
            'authors': [author.id for author in self.authors.all()],
            'year_of_publication': self.year_of_publication,
            'date_of_issue': self.date_of_issue
        }

    def update(self, name=None, description=None, count=None, year_of_publication=None):
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if count is not None:
            self.count = count
        if year_of_publication is not None:
            self.year_of_publication = year_of_publication
        self.save()

    def add_authors(self, authors):
        if authors is not None:
            for elem in authors:
                self.authors.add(elem)
                self.save()

    def remove_authors(self, authors):
        for elem in self.authors.values():
            self.authors.remove(elem['id'])

    @staticmethod
    def get_all():
        return Book.objects.all()
