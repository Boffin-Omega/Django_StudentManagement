# Generated by Django 5.1 on 2024-10-18 16:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('courseid', models.CharField(db_column='CourseID', max_length=10, primary_key=True, serialize=False)),
                ('coursename', models.CharField(blank=True, db_column='CourseName', max_length=50, null=True)),
                ('semester', models.IntegerField(blank=True, db_column='Semester', null=True)),
                ('startdate', models.DateField(blank=True, db_column='StartDate', null=True)),
                ('enddate', models.DateField(blank=True, db_column='EndDate', null=True)),
            ],
            options={
                'db_table': 'courses',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('profid', models.IntegerField(db_column='ProfID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=25, null=True)),
                ('phoneno', models.BigIntegerField(blank=True, db_column='PhoneNo', null=True)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=30, null=True)),
                ('gender', models.CharField(blank=True, db_column='Gender', max_length=20, null=True)),
                ('dateofjoining', models.DateField(blank=True, db_column='DateOfJoining', null=True)),
            ],
            options={
                'db_table': 'professor',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('rollno', models.IntegerField(db_column='rollno', primary_key=True, serialize=False)),
                ('firstname', models.CharField(blank=True, db_column='firstname', max_length=20, null=True)),
                ('lastname', models.CharField(blank=True, db_column='lastname', max_length=20, null=True)),
                ('phoneno', models.CharField(blank=True, db_column='phoneno', max_length=10, null=True)),
                ('gender', models.CharField(blank=True, db_column='gender', max_length=10, null=True)),
                ('email', models.CharField(blank=True, db_column='email', max_length=40, null=True)),
                ('dob', models.DateField(blank=True, db_column='dob', null=True)),
                ('dateofadmission', models.DateField(blank=True, db_column='dateofadmission', null=True)),
            ],
            options={
                'db_table': 'student',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Scores',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('examtype', models.CharField(blank=True, db_column='ExamType', max_length=20, null=True)),
                ('grade', models.CharField(blank=True, db_column='Grade', max_length=5, null=True)),
                ('courseid', models.ForeignKey(blank=True, db_column='CourseID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='studentmanage.courses')),
                ('rollno', models.ForeignKey(blank=True, db_column='RollNo', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='studentmanage.student')),
            ],
            options={
                'db_table': 'scores',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Taken',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('courseid', models.ForeignKey(blank=True, db_column='CourseID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='studentmanage.courses')),
                ('rollno', models.ForeignKey(blank=True, db_column='RollNo', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='studentmanage.student')),
            ],
            options={
                'db_table': 'taken',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Taughtby',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('courseid', models.ForeignKey(blank=True, db_column='CourseID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='studentmanage.courses')),
                ('profid', models.ForeignKey(blank=True, db_column='ProfID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='studentmanage.professor')),
            ],
            options={
                'db_table': 'taughtby',
                'managed': True,
            },
        ),
    ]
