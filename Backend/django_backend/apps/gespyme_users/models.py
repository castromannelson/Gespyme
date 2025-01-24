from django.db import models 
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser


class Gespyme_user(AbstractUser):
    """Gespime system custom user
    
    propertys:
    _all_ Base user django propertys;
    user_role = Charfuield max length 5 , Posible choices Admin and User, Role of the user in the systmen and its privileges
    cid = Charfield max and min length 11 , CID of the user
    
    """
    ROLES =(('Admin', 'Admin'), ('User','User'))
    user_role = models.CharField(max_length=5, null=False, blank=False, choices=ROLES, default='User')
    user_cid = models.CharField(max_length=11, null=False, blank=False, unique=True)
    
    def __str__(self) -> str:
        return f'< {self.user_role} - {self.username} >'