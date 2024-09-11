import glob
import os
import zipfile
from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils.text import slugify
import pandas as pd

from tablets.models import Glyph


class Command(BaseCommand):
    help = "group and zip glyph images by signs"

    def handle(self, *args, **kwargs):

        MEDIA_ROOT = settings.MEDIA_ROOT
        ARCHE_ROOT = settings.ARCHE_ROOT
        ZIP_ROOT = settings.ZIP_ROOT
        items = glob.glob(f"{ZIP_ROOT}/*.zip")
        print(f"removing {len(items)} from {ZIP_ROOT}")
        [os.remove(x) for x in items]

        props = ["id", "image", "sign__sign_name", "sign__id"]
        df = pd.DataFrame(
            Glyph.objects.values_list(*props)[:20],
            columns=props,
        ).astype("str")
        df["path"] = df.apply(lambda x: os.path.join(MEDIA_ROOT, x.image), axis=1)
        df["folder"] = df.apply(
            lambda x: slugify(f"{x.sign__sign_name}-{x.sign__id}"), axis=1
        )
        for g, ndf in df.groupby("folder"):
            folder_path = os.path.join(ZIP_ROOT, f"{g}.zip")
            with zipfile.ZipFile(f"{folder_path}", "w") as zipMe:
                for i, row in ndf.iterrows():
                    arcname = os.path.split(row["path"])[-1]
                    zipMe.write(
                        row["path"], arcname=arcname, compress_type=zipfile.ZIP_DEFLATED
                    )
        folder_path = os.path.join(ARCHE_ROOT, "glyphs.zip")
        items = glob.glob(f"{ZIP_ROOT}/*.zip")
        with zipfile.ZipFile(f"{folder_path}", "w") as zipMe:
            for x in items:
                arcname = os.path.split(x)[-1]
                zipMe.write(x, arcname=arcname, compress_type=zipfile.ZIP_DEFLATED)
        items = glob.glob(f"{ZIP_ROOT}/*.zip")
        [os.remove(x) for x in items]
        return folder_path
