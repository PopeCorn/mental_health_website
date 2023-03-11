from django.conf import settings
from django.db import migrations

def set_created_by(apps, schema_editor):
    Journal = apps.get_model('home', 'Journal')
    default_user = settings.AUTH_USER_MODEL.objects.first()
    Journal.objects.filter(created_by=None).update(created_by=default_user)

class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20230310_1710'),
    ]

    operations = [
        migrations.RunPython(set_created_by),
    ]

