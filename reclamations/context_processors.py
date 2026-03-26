from .models import Reclamation
from .notifications import NotificationService

def reclamations_ouvertes(request):
    if request.user.is_authenticated:
        count = Reclamation.objects.filter(cloture=False).count()
        return {'reclamations_ouvertes_count': count}
    return {'reclamations_ouvertes_count': 0}

def reclamations_retard_count(request):
    """Ajoute le nombre de réclamations en retard au contexte"""
    if request.user.is_authenticated:
        reclamations_retard = NotificationService.get_reclamations_a_notifier()
        return {'reclamations_retard_count': len(reclamations_retard)}
    return {'reclamations_retard_count': 0}