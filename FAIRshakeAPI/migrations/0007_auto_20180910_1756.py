# Generated by Django 2.0.7 on 2018-09-10 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FAIRshakeAPI', '0006_auto_20180910_1752'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Assessment',
        ),
        migrations.DeleteModel(
            name='AssessmentRequest',
        ),
        migrations.DeleteModel(
            name='DigitalObject',
        ),
        migrations.DeleteModel(
            name='Metric',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='Rubric',
        ),
    ]