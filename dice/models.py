from django.db import models
import uuid

class WeaponType(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="ID вида",
        help_text="Уникальный идентификатор вида оружия",
    )
    name = models.CharField(
        max_length=100,
        verbose_name="Имя вида",
        help_text="Название вида оружия",
    )

    class Meta:
        verbose_name = "Вид оружия"
        verbose_name_plural = "Виды оружия"
        ordering = ["name"]
        indexes = [
            models.Index(fields=["id"], name="weapon_type_id_idx"),
        ]

    def __str__(self) -> str:
        return self.name


class Weapon(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="ID оружия",
        help_text="Уникальный идентификатор оружия",
    )
    name = models.CharField(
        max_length=150,
        verbose_name="Имя оружия",
        help_text="Название оружия",
    )
    damage = models.CharField(
        max_length=50,
        verbose_name="Урон",
        help_text="Описание урона (например, '1d8 slashing' или '35')",
    )
    weapon_type = models.ForeignKey(
        WeaponType,
        on_delete=models.PROTECT,
        related_name="weapons",
        verbose_name="Вид оружия",
        help_text="Категория/вид оружия",
    )

    class Meta:
        verbose_name = "Оружие"
        verbose_name_plural = "Оружия"
        ordering = ["weapon_type__name", "name"]
        indexes = [
            models.Index(fields=["id"], name="weapon_id_idx"),
        ]

    def __str__(self) -> str:
        return f"{self.name}"


class ArmorType(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="ID вида",
        help_text="Уникальный идентификатор вида доспеха",
    )
    name = models.CharField(
        max_length=100,
        verbose_name="Имя вида",
        help_text="Название вида доспеха",
    )

    class Meta:
        verbose_name = "Вид доспеха"
        verbose_name_plural = "Виды доспеха"
        ordering = ["name"]
        indexes = [
            models.Index(fields=["id"], name="armor_type_id_idx"),
        ]

    def __str__(self) -> str:
        return self.name


class Armor(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="ID доспеха",
        help_text="Уникальный идентификатор доспеха",
    )
    name = models.CharField(
        max_length=150,
        verbose_name="Имя доспеха",
        help_text="Название доспеха",
    )
    armor_class = models.CharField(
        max_length=50,
        verbose_name="Класс доспеха",
        help_text="Класс/тип защиты (например, '11 + Модификатор Ловкости')",
    )
    armor_type = models.ForeignKey(
        ArmorType,
        on_delete=models.PROTECT,
        related_name="armors",
        verbose_name="Вид доспеха",
        help_text="Категория/вид доспеха",
    )

    class Meta:
        verbose_name = "Доспех"
        verbose_name_plural = "Доспехи"
        ordering = ["armor_type__name", "name"]
        indexes = [
            models.Index(fields=["id"], name="armor_id_idx"),
        ]

    def __str__(self) -> str:
        return f"{self.name}"
