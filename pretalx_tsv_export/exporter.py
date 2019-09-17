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
        writer = csv.DictWriter(content, fieldnames=['start', 'end', 'duration', 'room', 'title', 'speakers'], delimiter='\t')
        writer.writeheader()

        for talk in self.event.current_schedule.talks.all():
            writer.writerow(
                {
                    'start': talk.start,
                    'end': talk.real_end,
                    'duration': talk.duration,
                    'room': str(talk.room),
                    'title': talk.submission.title,
                    'speakers': talk.submission.display_speaker_names,
                }
            )

        return (f'{self.event.slug}-schedule.tsv', 'text/plain', content.getvalue())
