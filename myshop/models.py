from django.db import models


class ProductKind(models.Model):
    name = models.CharField(max_length=128, db_index=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вид продукта'
        verbose_name_plural = 'Виды продуктов'
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(max_length=32, unique=True)
    # image = models.ImageField(upload_to='product', blank=True, null=True)
    kind = models.ForeignKey(ProductKind, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукты'
        ordering = ['pk']


# class Kind(models.Model):
#     name = models.CharField(max_length=32, unique=True)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='kind')
#
#     def __str__(self):
#         return self.name
#
#
# class Weight(models.Model):
#     name = models.IntegerField()
#     kind = models.ForeignKey(Kind, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.name
#
#
# class Price(models.Model):
#     name = models.IntegerField(unique=False)
#     weight = models.OneToOneField(Weight, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.name
#
#
# class Card(models.Model):
#     name = models.CharField(max_length=64, blank=True, unique=False)
#     kind = models.ForeignKey(Kind, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.name