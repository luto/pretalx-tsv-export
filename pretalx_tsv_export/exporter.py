from pretalx.common.exporter import BaseExporter
import io
import csv

from pretalx.submission.models import SubmissionStates

class TSVExporter(BaseExporter):
    identifier = 'schedule.tsv'
    verbose_name = 'TSV Schedule'
    public = False
    icon = 'fa-file'

    def render(self, **kwargs):
        content = io.StringIO()

        for talk in self.event.current_schedule.talks.all():
            content.write(
f"""{talk.start}\t\u2012\t{talk.real_end}\t{talk.submission_type.name}
{talk.submission.title}
{talk.submission.display_speaker_names}
""")
        return (f'{self.event.slug}-schedule.tsv', 'text/plain', content.getvalue())
