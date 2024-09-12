import glob
import os
from django.conf import settings
from django.core.management.base import BaseCommand


from tablets.models import Sign


class Command(BaseCommand):
    help = "fixes file names, https://github.com/acdh-oeaw/labasi/issues/50"

    def handle(self, *args, **kwargs):
        MEDIA_ROOT = settings.MEDIA_ROOT
        SIGN_FOLDER = os.path.join(MEDIA_ROOT, "sign_img")
        print("rename file name in database")
        for x in Sign.objects.filter(image_1__endswith=".bmp"):
            new_name = x.image_1.name.replace(".bmp", ".jpg")
            x.image_1.name = new_name
            x.save()
        for x in Sign.objects.filter(image_1__contains=".."):
            new_name = x.image_1.name.replace("..", ".")
            x.image_1.name = new_name
            x.save()

        print("rename files")
        items = glob.glob(f"{SIGN_FOLDER}/*.bmp")
        for x in items:
            new_name = x.replace(".bmp", ".jpg")
            os.rename(x, new_name)
        items = glob.glob(f"{SIGN_FOLDER}/*..*")
        for x in items:
            new_name = x.replace("..", ".")
            os.rename(x, new_name)
        print(items)
        return "done"
