"""Django Application configuration."""
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

__all__ = ['BeatConfig']


class BeatConfig(AppConfig):
    """Default configuration for beat app."""

    name = 'beat'
    label = 'beat'
    verbose_name = _('Periodic Tasks')
    default_auto_field = 'django.db.models.AutoField'
