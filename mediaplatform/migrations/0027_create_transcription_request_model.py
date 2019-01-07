# Generated by Django 2.1.3 on 2019-01-07 12:10

from django.db import migrations, models
import django.db.models.deletion
import mediaplatform.models


class Migration(migrations.Migration):

    dependencies = [
        ('mediaplatform', '0026_add_initially_fetched_from_url_to_media_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='TranscriptionRequest',
            fields=[
                ('id', models.CharField(default=mediaplatform.models._make_token, editable=False, max_length=11, primary_key=True, serialize=False)),
                ('state', models.CharField(choices=[('pending', 'Pending'), ('running', 'Running'), ('resolved', 'Resolved'), ('rejected', 'Rejected'), ('cancelled', 'Cancelled')], default='pending', help_text='Request state', max_length=32)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('media_item', models.ForeignKey(help_text='Media item related to transcription request', on_delete=django.db.models.deletion.CASCADE, to='mediaplatform.MediaItem')),
            ],
        ),
        migrations.AddIndex(
            model_name='transcriptionrequest',
            index=models.Index(fields=['state'], name='mediaplatfo_state_0b0cc0_idx'),
        ),
        migrations.AddIndex(
            model_name='transcriptionrequest',
            index=models.Index(fields=['media_item'], name='mediaplatfo_media_i_2f0cd4_idx'),
        ),
    ]
