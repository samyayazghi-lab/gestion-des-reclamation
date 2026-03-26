# reclamations/templatetags/reclamations_extras.py
from django import template
from django import template

register = template.Library()

@register.filter
def sum_reclamations(queryset):
    """
    Compte le nombre total de réclamations pour différents types d'objets:
    - Liste de clients
    - Liste de sites
    - Liste d'UAP
    """
    if not queryset:
        return 0
    
    total = 0
    
    try:
        # Vérifier le premier élément pour déterminer le type
        first_item = queryset.first() if hasattr(queryset, 'first') else None
        
        if first_item:
            # Si c'est une liste de clients (a un attribut reclamations)
            if hasattr(first_item, 'reclamations'):
                for client in queryset:
                    total += client.reclamations.count()
            
            # Si c'est une liste de sites (a un attribut clients)
            elif hasattr(first_item, 'clients'):
                for site in queryset:
                    for client in site.clients.all():
                        total += client.reclamations.count()
            
            # Si c'est une liste d'UAP (a un attribut sites)
            elif hasattr(first_item, 'sites'):
                for uap in queryset:
                    for site in uap.sites.all():
                        for client in site.clients.all():
                            total += client.reclamations.count()
        
        # Si le queryset est vide
        else:
            total = 0
            
    except Exception as e:
        print(f"Erreur dans sum_reclamations: {e}")
        total = 0
    
    return total

@register.filter
def zip_lists(a, b):
    """Zippe deux listes ensemble"""
    return zip(a, b)


