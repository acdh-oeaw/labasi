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
        ZIP_ROOT = settings.ZIP_ROOT
        TEI_ROOT = settings.TEI_ROOT
        file_to_remove = glob.glob(f"{ZIP_ROOT}/*.zip")
        print(f"removing {len(file_to_remove)} from {ZIP_ROOT}")
        [os.remove(x) for x in file_to_remove]

        file_to_remove = glob.glob(f"{TEI_ROOT}/*.xml")
        print(f"removing {len(file_to_remove)} from {TEI_ROOT}")
        [os.remove(x) for x in file_to_remove]

        props = ["id", "image", "sign__sign_name", "sign__id"]
        df = pd.DataFrame(
            Glyph.objects.values_list(*props)[:20],
            columns=props,
        ).astype("str")
        df["path"] = df.apply(lambda x: os.path.join(MEDIA_ROOT, x.image), axis=1)
        df["folder"] = df.apply(
            lambda x: slugify(f"{x.sign__sign_name}-{x.sign__id}"), axis=1
        )
        df.to_csv("hansi.csv", index=False)
        for g, ndf in df.groupby("folder"):
            folder_path = os.path.join(ZIP_ROOT, f"{g}.zip")
            with zipfile.ZipFile(f"{folder_path}", "w") as zipMe:
                for i, row in ndf.iterrows():
                    zipMe.write(row["path"], compress_type=zipfile.ZIP_DEFLATED)

        return "foo"
