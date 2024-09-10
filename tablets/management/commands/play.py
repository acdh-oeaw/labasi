import json
from django.core.management.base import BaseCommand
from tablets.models import Glyph


class Command(BaseCommand):
    help = "play around"

    def handle(self, *args, **kwargs):
        items = Glyph.objects.all()[:250]
        data = []
        for x in items:
            item = {
                "id": x.id,
                "label": x.image.path,
                "sign": x.sign.sign_name
            }
        data.append(item)
        with open("hansi.json", "w", encoding="utf-8") as fp:
            json.dump(data, fp, ensure_ascii=False, indent=2)

        return "foo"
