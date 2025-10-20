import uuid
from typing import ClassVar

from django.db import models


class WeaponType(models.Model):
    """
    Represents a category or type of weapon in the system.

    This model stores different classifications of weapons such as swords, axes, bows, etc.
    Each weapon type groups similar weapons together for organizational purposes.

    Attributes
    ----------
        id: UUIDField
            Unique identifier for the weapon type, automatically generated.
        name: CharField
            Human-readable name of the weapon type (e.g., 'Sword', 'Axe').

    """

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
        """Metadata configuration for WeaponType model."""

        verbose_name = "Вид оружия"
        verbose_name_plural = "Виды оружия"
        ordering: ClassVar = ["name"]
        indexes: ClassVar = [
            models.Index(fields=["id"], name="weapon_type_id_idx"),
        ]

    def __str__(self) -> str:
        """Return string representation of weapon type."""
        return self.name


class Weapon(models.Model):
    """
    Represents a weapon item with its combat properties and characteristics.

    This model stores individual weapons that belong to specific weapon types,
    containing details about damage output and classification.

    Attributes
    ----------
        id: UUIDField
            Unique identifier for the weapon, automatically generated.
        name: CharField
            Display name of the weapon.
        damage: CharField
            Damage description including dice notation and damage type.
        weapon_type: ForeignKey to WeaponType
            Classification category this weapon belongs to.

    """

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
        """Metadata configuration for Weapon model."""

        verbose_name = "Оружие"
        verbose_name_plural = "Оружия"
        ordering: ClassVar = ["weapon_type__name", "name"]
        indexes: ClassVar = [
            models.Index(fields=["id"], name="weapon_id_idx"),
        ]

    def __str__(self) -> str:
        """Return string representation of weapon."""
        return f"{self.name}"


class ArmorType(models.Model):
    """
    Represents a category or type of armor in the system.

    This model stores different classifications of armor such as light, medium, heavy, etc.
    Each armor type groups similar protective gear together for organizational purposes.

    Attributes
    ----------
        id: UUIDField
            Unique identifier for the armor type, automatically generated.
        name: CharField
            Human-readable name of the armor type (e.g., 'Light', 'Heavy').

    """

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
        """Metadata configuration for ArmorType model."""

        verbose_name = "Вид доспеха"
        verbose_name_plural = "Виды доспеха"
        ordering: ClassVar = ["name"]
        indexes: ClassVar = [
            models.Index(fields=["id"], name="armor_type_id_idx"),
        ]

    def __str__(self) -> str:
        """Return string representation of armor type."""
        return self.name


class Armor(models.Model):
    """
    Represents an armor item with its defensive properties and characteristics.

    This model stores individual armor pieces that belong to specific armor types,
    containing details about protection level and classification.

    Attributes
    ----------
        id: UUIDField
            Unique identifier for the armor, automatically generated.
        name: CharField
            Display name of the armor.
        armor_class: CharField
            Armor class description including calculation method.
        armor_type: ForeignKey to ArmorType
            Classification category this armor belongs to.

    """

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
        """Metadata configuration for Armor model."""

        verbose_name = "Доспех"
        verbose_name_plural = "Доспехи"
        ordering: ClassVar = ["armor_type__name", "name"]
        indexes: ClassVar = [
            models.Index(fields=["id"], name="armor_id_idx"),
        ]

    def __str__(self) -> str:
        """Return string representation of armor."""
        return f"{self.name}"
