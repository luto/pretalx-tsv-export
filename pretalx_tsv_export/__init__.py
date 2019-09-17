from django.apps import AppConfig
from django.utils.translation import ugettext_lazy


class PluginApp(AppConfig):
    name = "pretalx_tsv_export"
    verbose_name = "pretalx TSV export"

    class PretalxPluginMeta:
        name = ugettext_lazy("pretalx TSV export")
        author = "luto"
        description = ugettext_lazy("Export schedule and speaker data as tab separated file.")
        visible = True
        version = "0.0.0"

    def ready(self):
        from . import signals  # NOQA


default_app_config = "pretalx_tsv_export.PluginApp"
