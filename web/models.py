from django.db import models


class Product(models.Model):
    COSTUMES = 'Костюмы'
    BLAZERS = 'Пиджаки'
    TROUSERS = 'Брюки'
    SHOES = 'Обувь'

    CHOICE_GROUP = {
        (COSTUMES, 'Костюмы'),
        (BLAZERS, 'Пиджаки'),
        (TROUSERS, 'Брюки'),
        (SHOES, 'Обувь')
    }

    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    availability = models.BooleanField()
    group = models.CharField(max_length=20, choices=CHOICE_GROUP, default=COSTUMES)
    img = models.ImageField(default='notimg.jpg', upload_to='product_image')


    def __str__(self):
        return f'{self.name}'