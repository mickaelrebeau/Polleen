# Generated by Django 4.0.2 on 2022-06-08 11:32

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_organiser', models.BooleanField(default=True)),
                ('is_agent', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(blank=True, default=None, null=True, upload_to='')),
                ('logo', models.ImageField(blank=True, default=None, null=True, upload_to='')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=0)),
                ('company', models.CharField(default=None, max_length=100)),
                ('post', models.CharField(default=None, max_length=100)),
                ('email', models.EmailField(default=None, max_length=100)),
                ('phone', models.CharField(default=None, max_length=100)),
                ('communication_preference', models.CharField(choices=[('email', 'Email'), ('sms', 'SMS'), ('whatsapp', 'Whatsapp'), ('polleen', 'Polleen')], default='Polleen', max_length=100)),
                ('leisure', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('linkedin', models.URLField(blank=True, default=None, max_length=100, null=True)),
                ('facebook', models.URLField(blank=True, default=None, max_length=100, null=True)),
                ('twitter', models.URLField(blank=True, default=None, max_length=100, null=True)),
                ('instagram', models.URLField(blank=True, default=None, max_length=100, null=True)),
                ('website', models.URLField(blank=True, default=None, max_length=100, null=True)),
                ('other_social_media', models.URLField(blank=True, default=None, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='leads.agent')),
                ('category', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='leads', to='leads.category')),
                ('organisation', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='leads.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='InvitedLead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(blank=True, default=None, null=True, upload_to='')),
                ('logo', models.ImageField(blank=True, default=None, null=True, upload_to='')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=0)),
                ('company', models.CharField(default=None, max_length=100)),
                ('post', models.CharField(default=None, max_length=100)),
                ('email', models.EmailField(default=None, max_length=100)),
                ('phone', models.CharField(default=None, max_length=100)),
                ('linkedin', models.URLField(blank=True, default=None, max_length=100, null=True)),
                ('facebook', models.URLField(blank=True, default=None, max_length=100, null=True)),
                ('twitter', models.URLField(blank=True, default=None, max_length=100, null=True)),
                ('instagram', models.URLField(blank=True, default=None, max_length=100, null=True)),
                ('website', models.URLField(blank=True, default=None, max_length=100, null=True)),
                ('other_social_media', models.URLField(blank=True, default=None, max_length=100, null=True)),
                ('invited_by', models.CharField(default=None, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='leads.agent')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='organisation',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='leads.userprofile'),
        ),
        migrations.AddField(
            model_name='agent',
            name='organisation',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='leads.userprofile'),
        ),
        migrations.AddField(
            model_name='agent',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
