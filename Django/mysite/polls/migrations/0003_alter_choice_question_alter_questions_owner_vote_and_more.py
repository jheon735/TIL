# Generated by Django 5.0.4 on 2024-04-12 04:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_questions_owner_alter_questions_pub_date_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='polls.questions'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.choice')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.questions')),
                ('voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='vote',
            constraint=models.UniqueConstraint(fields=('question', 'voter'), name='unique_voter_for_questions'),
        ),
    ]
