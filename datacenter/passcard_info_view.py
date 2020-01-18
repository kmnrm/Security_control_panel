from datacenter.models import Passcard, Visit
from datacenter.utils import format_duration
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    passcard_visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []

    for passcard_visit in passcard_visits:
        datetime_entered = passcard_visit.entered_at.strftime("%b %d %Y %I:%M %p")
        duration = format_duration(passcard_visit.get_duration())
        visit_is_suspicious = "UNDER SUSPICION" if passcard_visit.is_long() else "-"

        visit = {
                "entered_at": datetime_entered,
                "duration": duration,
                "is_strange": visit_is_suspicious
            }
        this_passcard_visits.append(visit)
    
    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)

