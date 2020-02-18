# Generated by Django 3.0.3 on 2020-02-18 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StreetCardServices', '0005_auto_20200214_0231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('EnrollmentID', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('PersonalId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Enrollment_PersonalId', to='StreetCardServices.Homeless')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('ProjectId', models.CharField(max_length=32, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='IncomeAndSources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('InformationDate', models.DateField()),
                ('IncomeFromAnySources', models.IntegerField(choices=[(0, 'No'), (1, 'Yes'), (8, "Client Doesn't Know"), (9, 'Client Refused'), (99, 'Data Not Collected')])),
                ('Earned', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], default=0)),
                ('EarnedIncome', models.IntegerField(default=0)),
                ('Unemployment', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], default=0)),
                ('UnemploymentAmount', models.IntegerField(null=True)),
                ('SSI', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')])),
                ('SSIAmount', models.IntegerField(null=True)),
                ('SSDI', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')])),
                ('SSDIAmount', models.IntegerField(null=True)),
                ('VADisabilityService', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')])),
                ('VADisabilityServiceAmount', models.IntegerField(null=True)),
                ('VADisabilityNonService', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')])),
                ('VADisabilityNonServiceNonAmount', models.IntegerField(null=True)),
                ('PrivateDisability', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')])),
                ('PrivateDisabilityAmount', models.IntegerField(null=True)),
                ('WorkersComp', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')])),
                ('WorkersCompAmount', models.IntegerField(null=True)),
                ('TANF', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')])),
                ('TANFAmount', models.IntegerField(null=True)),
                ('GA', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')])),
                ('GAAmount', models.IntegerField(null=True)),
                ('SocSecRetirement', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')])),
                ('SocSecRetirementAmount', models.IntegerField(null=True)),
                ('Pension', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')])),
                ('PensionAmount', models.IntegerField(null=True)),
                ('ChildSupport', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')])),
                ('ChildSupportAmount', models.IntegerField(null=True)),
                ('Alimony', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')])),
                ('AlimonyAmount', models.IntegerField(null=True)),
                ('OtherIncomeSources', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')])),
                ('OtherIncomeSourcesAmount', models.IntegerField(null=True)),
                ('OtherIncomeSourcesIdentify', models.TextField(blank=True, max_length=50, null=True)),
                ('TotalMonthlyIncome', models.IntegerField(default=0)),
                ('EnrollmentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='IncomeAndSources_EnrollmentID', to='StreetCardServices.Enrollment')),
                ('PersonalId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='IncomeAndSources_PersonalId', to='StreetCardServices.Homeless')),
            ],
        ),
        migrations.AddField(
            model_name='enrollment',
            name='ProjectID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ProjectID', to='StreetCardServices.Project'),
        ),
    ]
