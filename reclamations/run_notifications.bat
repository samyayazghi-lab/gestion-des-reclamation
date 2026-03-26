# Éditer le crontab
crontab -e

# Ajouter la ligne pour exécuter tous les jours à 8h00
0 8 * * * cd /chemin/vers/projet && /chemin/vers/venv/bin/python manage.py send_notifications >> /var/log/notifications.log 2>&1