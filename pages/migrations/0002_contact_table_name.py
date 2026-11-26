from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [("pages", "0001_initial")]
    operations = [migrations.AlterModelTable(name="contactmessage", table="contact")]
