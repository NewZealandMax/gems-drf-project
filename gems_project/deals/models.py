from django.db import models


class Gem(models.Model):
    """Describes gem model."""
    name = models.SlugField(
        max_length=64,
        unique=True,
        verbose_name='Название'
    )
    customers = models.ManyToManyField(
        'Customer',
        related_name='gems',
        verbose_name='Клиенты'
    )

    def __str__(self):
        return self.name


class Customer(models.Model):
    """Describes customer model."""
    username = models.SlugField(
        max_length=64,
        unique=True,
        verbose_name='Логин клиента'
    )
    spent_money = models.PositiveIntegerField(
        default=0,
        verbose_name='Потраченная сумма'
    )


class Deal(models.Model):
    """Describes deal model."""
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='deals',
        verbose_name='Клиент'
    )
    item = models.ForeignKey(
        Gem,
        on_delete=models.CASCADE,
        related_name='deals',
        verbose_name='Товар'
    )
    total = models.PositiveIntegerField(
        verbose_name='Сумма сделки'
    )
    quantity = models.PositiveIntegerField(
        verbose_name='Количество товара'
    )
    date = models.DateTimeField(
        verbose_name='Дата сделки'
    )
