from django.db import migrations
from django.contrib.auth.hashers import make_password


def set_kfc_password(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    u = User.objects.filter(username='kfc__tk_avenue').first()
    if u:
        u.password = make_password('qwerty')
        u.save(update_fields=['password'])


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_passwordresettoken'),
    ]

    operations = [
        migrations.RunPython(set_kfc_password, migrations.RunPython.noop),
    ]
