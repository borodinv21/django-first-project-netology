# Generated by Django 5.1.1 on 2024-09-12 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_rename_scope_articlescope_remove_tag_articles_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ArticleScope',
            new_name='Scope',
        ),
        migrations.RemoveField(
            model_name='article',
            name='tags',
        ),
        migrations.AddField(
            model_name='article',
            name='scopes',
            field=models.ManyToManyField(through='articles.Scope', to='articles.tag'),
        ),
    ]