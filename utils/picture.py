from django.conf import settings
from django.core.files.storage import default_storage


def delete_profile_picture(sender, instance) -> None:
    if instance.pk:  # Delete the object if exists in the database
        old_instance = sender.objects.get(pk=instance.pk)
        if old_instance.profile_picture and instance.profile_picture != old_instance.profile_picture:
            # Delete the old picture only if the profile_picture field hasn't been updated
            default_storage.delete(old_instance.profile_picture.name)
    if instance.profile_picture:
        # Save the new picture on S3 Bucket
        file_path = f"{settings.MEDIA_ROOT}/{instance.profile_picture.name}"
        with default_storage.open(file_path, "wb") as f:
            f.write(instance.profile_picture.file.read())
