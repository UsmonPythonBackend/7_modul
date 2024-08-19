from django.db import models
from .helpers import SaveMediaFiles



class StatusChoice(models.TextChoices):
    DRAFT = 'df', 'Draft',
    PUBLISH = 'pb', 'Publish'


class Services(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.URLField(null=True)
    status = models.CharField(max_length=4, choices=StatusChoice.choices, default=StatusChoice.PUBLISH)
    created_ad = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['id', ]

    def __str__(self):
        return self.title


    class Meta:
        ordering = ['id', ]
        indexes = [
            models.Index(fields=['id']),
        ]


    def df_to_pb(self):
        if self.status == 'df':
            self.status == 'pb'
            self.save()


    def pb_to_df(self):
        if self.status == 'pb':
            self.status == 'df'
            self.save()


class Business(models.Model):
    title = models.CharField(max_length=155)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.URLField(null=True)
    status = models.CharField(max_length=4, choices=StatusChoice.choices, default=StatusChoice.PUBLISH)
    created_ad = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


    class Meta:
        ordering = ['id', ]
        indexes = [
            models.Index(fields=['id']),
        ]


    def df_to_pb(self):
        if self.status == 'df':
            self.status == 'pb'
            self.save()


    def pb_to_df(self):
        if self.status == 'pb':
            self.status == 'df'
            self.save()



class Users(models.Model):
    slug = models.SlugField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.URLField(null=True)
    level = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    status = models.CharField(max_length=5, choices=StatusChoice.choices, default=StatusChoice.PUBLISH)
    created_ad = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id']),
        ]

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.get_full_name()

    def df_to_pb(self):
        if self.status == 'df':
            self.status == 'pb'
            self.save()


    def pb_to_df(self):
        if self.status == 'pb':
            self.status == 'df'
            self.save()


class Clients(models.Model):
    slug = models.SlugField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.URLField(null=True)
    comment = models.TextField()
    status = models.CharField(max_length=4, choices=StatusChoice.choices, default=StatusChoice.PUBLISH)
    created_ad = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id']),
        ]

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.get_full_name()

    def df_to_pb(self):
        if self.status == 'df':
            self.status == 'pb'
            self.save()

    def pb_to_df(self):
        if self.status == 'pb':
            self.status == 'df'
            self.save()


class Comments(models.Model):
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    comment = models.TextField()
    status = models.CharField(max_length=4, choices=StatusChoice.choices, default=StatusChoice.PUBLISH)
    created_ad = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.comment


    def df_to_pb(self):
        if self.status == 'df':
            self.status == 'pb'
            self.save()


    def pb_to_df(self):
        if self.status == 'pb':
            self.status == 'df'
            self.save()


class FAQs(models.Model):
    question = models.TextField()
    answer = models.TextField()
    status = models.CharField(max_length=4, choices=StatusChoice.choices, default=StatusChoice.PUBLISH)
    created_ad = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.question


    def df_to_pb(self):
        if self.status == 'df':
            self.status == 'pb'
            self.save()


    def pb_to_df(self):
        if self.status == 'pb':
            self.status == 'df'
            self.save()