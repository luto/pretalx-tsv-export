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
        tz = self.event.tz

        for talk in self.event.current_schedule.talks.all().order_by('start'):
            if not talk.start or not talk.real_end:
                continue

            content.write(
                '\t'.join(map(str, [
                    talk.room.name,
                    f'{talk.start.astimezone(tz):%H.%M}\u2013{talk.real_end.astimezone(tz):%H.%M}',
                    talk.submission.title,
                    talk.submission.display_speaker_names,
                    talk.submission.submission_type.name,
                ])) + '\n'
            )

        return (f'{self.event.slug}-schedule.tsv', 'text/plain', content.getvalue())
