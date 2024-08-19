import uuid
from django.db import models


# class StatusChoice(models.TextChoices):
#     DRAFT = 'df', 'Draft'
#     PUBLISH = 'pb', 'Publish'




class SaveMediaFiles(object):

    def save_services_image(instance, filename):
        image_path = filename.split('.')[-1]
        return f"services/{uuid.uuid4()}.{image_path}"

    def save_business_image(instance, filename):
        image_path = filename.split('.')[-1]
        return f"business/{uuid.uuid4()}.{image_path}"

    def save_users_image(instance, filename):
        image_path = filename.split('.')[-1]
        return f"users/{uuid.uuid4()}.{image_path}"

    def save_clients_image(instance, filename):
        image_path = filename.split('.')[-1]
        return f"clients/{uuid.uuid4()}.{image_path}"


