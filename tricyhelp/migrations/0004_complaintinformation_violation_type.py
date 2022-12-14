# Generated by Django 4.1.2 on 2022-11-30 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tricyhelp', '0003_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaintinformation',
            name='violation_type',
            field=models.CharField(choices=[('Contracting Passenger', 'Contracting Passenger'), ('Overcharging Fare', 'Overcharging Fare'), ('Arrogant Discourteous Driver', 'Arrogant Discourteous Driver'), ('Refusal To Convey Passenger', 'Refusal To Convey Passenger'), ('Hit And Run', 'Hit And Run'), ('Threatening Passenger', 'Threatening Passenger'), ('Reckless Driving', 'Reckless Driving'), ('Discriminating Againts Passenger', 'Discriminating Againts Passenger'), ('Refusal To Grant Discount', 'Refusal To Grant Discount')], default=1, max_length=150, verbose_name='Violation Type'),
            preserve_default=False,
        ),
    ]
