from django.db import models
import datetime
from datacenter.utils import chop_microseconds

class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= "leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
        )

    def get_duration(self):
        datetime_entered = self.entered_at
        datetime_current = datetime.datetime.now(datetime.timezone.utc)
        if self.leaved_at is None:
            visit_duration = datetime_current - datetime_entered
        else:
            datetime_got_out = self.leaved_at
            visit_duration = datetime_got_out - datetime_entered
        visit_duration = chop_microseconds(visit_duration)
        return visit_duration
    
    def is_long(self, minutes=60):
        visit_duration = self.get_duration()
        secs_in_min = 60
        duration_in_seconds = visit_duration.total_seconds()
        duration_in_minutes = int(duration_in_seconds // secs_in_min)
        return (duration_in_minutes >= minutes)
