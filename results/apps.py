"""Application configuration."""
from __future__ import absolute_import, unicode_literals

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

__all__ = ['CeleryResultConfig']


class CeleryResultConfig(AppConfig):
    """Default configuration for the results app."""

    name = 'results'
    label = 'results'
    verbose_name = _('Results')
