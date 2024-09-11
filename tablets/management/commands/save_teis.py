import glob
import os
import zipfile
from tqdm import tqdm
from django.conf import settings
from django.core.management.base import BaseCommand
from django.template.loader import render_to_string


from tablets.models import Tablet, Glyph


class Command(BaseCommand):
    help = "serializes tablet as TEIs into TEI folder"

    def handle(self, *args, **kwargs):
        ARCHE_ROOT = settings.ARCHE_ROOT
        TEI_ROOT = settings.TEI_ROOT
        file_to_remove = glob.glob(f"{TEI_ROOT}/*.xml")
        print(f"removing {len(file_to_remove)} from {TEI_ROOT}")
        [os.remove(x) for x in file_to_remove]

        items = Tablet.objects.all()
        print(f"starting to serialize {len(items)} Tablets")
        for instance in tqdm(items, total=len(items)):
            file_name = f"tablet_{instance.id:03}.xml"
            save_path = os.path.join(TEI_ROOT, file_name)
            context = {"object": instance}
            try:
                context["glyph_list"] = Glyph.objects.filter(tablet=instance.id)
            except:  # noqa:
                pass
            data = render_to_string("tablets/tablet_to_tei.html", context)
            with open(save_path, "w", encoding="utf-8") as fp:
                fp.write(data)
        print(f"done with serializing {len(items)} Tablets, now let's zip them")

        folder_path = os.path.join(ARCHE_ROOT, "teis.zip")
        items = glob.glob(f"{TEI_ROOT}/*.xml")
        with zipfile.ZipFile(f"{folder_path}", "w") as zipMe:
            for x in items:
                arcname = os.path.split(x)[-1]
                zipMe.write(x, arcname=arcname, compress_type=zipfile.ZIP_DEFLATED)
        return f"zipped {len(items)} tablets as TEIs into {folder_path}"
