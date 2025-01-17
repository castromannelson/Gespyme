from django.db import models


# Product DB ORM model


class  Product(models.Model):
    """Product DB Model
    
    propertys:
    product_name: Charfield max_length=255 ; product Name
    product_code: Charfield max_lengt=11 ; product unique code
    product_cuantity: Integer ; product cuantity in the DB
    product_prize: Float ; product sell prize
    
    """
    product_name = models.CharField(max_length=255, blank=False, null=False)
    product_code = models.CharField(max_length=11, blank=False, null=False, unique=True)
    product_cuantity = models.IntegerField(blank=False, null=False, default=0)
    product_prize = models.FloatField(blank=False, null=False)
    
    # Meta Class    
    class Meta:
        verbose_name = ("product")
        verbose_name_plural = ("products")
    
    # Str 
    def __str__(self):
        return f'< {self.product_code} - {self.product_name} >'

