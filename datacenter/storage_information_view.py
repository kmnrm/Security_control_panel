from datacenter.models import Passcard, Visit
from datacenter.utils import format_duration
from django.shortcuts import render


def storage_information_view(request):
    visits_not_leaved = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []
    for visit in visits_not_leaved:
        passcard_owner_name = visit.passcard.owner_name
        datetime_entered = visit.entered_at.strftime("%b %d %Y %I:%M %p")
        duration = visit.get_duration()
        duration = format_duration(duration)
        visit_is_suspicious = "YES" if visit.is_long() else "NO"
        non_closed_visit = {
            "who_entered": passcard_owner_name,
            "entered_at": datetime_entered,
            "duration": duration,
            "is_strange": visit_is_suspicious
        }
        non_closed_visits.append(non_closed_visit)

    context = {
        "non_closed_visits": non_closed_visits
    }
    return render(request, 'storage_information.html', context)

