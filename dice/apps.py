from django.apps import AppConfig


class DiceConfig(AppConfig):
    """
    Configuration class for the dice application.

    This class defines application-specific settings and initialization
    behavior for the dice rolling functionality within the Django project.

    Attributes
    ----------
        default_auto_field: str
            The default primary key field type for models in this application.
        name: str
            The full Python path to the application.

    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "dice"
