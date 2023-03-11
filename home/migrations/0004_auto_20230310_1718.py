from django.db import migrations
from django.conf import settings


def add_default_user(apps, schema_editor):
    Journal = apps.get_model('home', 'Journal')
    User = apps.get_model(settings.AUTH_USER_MODEL)
    default_user = User.objects.first()
    Journal.objects.filter(created_by=None).update(created_by=default_user)


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20230310_1710'),
    ]

    operations = [
        migrations.RunPython(add_default_user),
    ]