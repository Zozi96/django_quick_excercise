from django.core.files.storage import default_storage


def delete_profile_picture(sender, instance) -> None:
    if instance.pk:  # Delete the object if exists in the database
        old_instance = sender.objects.get(pk=instance.pk)
        if old_instance.profile_picture and instance.profile_picture != old_instance.profile_picture:
            # Delete the old picture only if the profile_picture field hasn't been updated
            default_storage.delete(old_instance.profile_picture.name)
