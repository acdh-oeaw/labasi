from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Count
from tablets.models import Tablet, Glyph, Sign
from vocabularies.models import Region, Scribe, Period

DATA = {
    "status": "ok",
    "query": "api:graph",
    "timestamp": "2016-07-21T09:56:36.803Z",
    "items": "7",
    "title": "TEST",
    "subtitle": "This is just a test to check if everythin works as expected.",
    "legendx": "Club",
    "legendy": "# of Victories",
    "measuredObject": "Victories",
    "payload": [
        ["Club", "# of Victories"],
        ["LASK", 10],
        ["Real Madrid", 4],
        ["Rapid Wien", 0],
        ["Blau Weiß Linz", -10],
    ],
}


def barcharts_view(request):
    context = {"test": "test"}
    return render(request, "charts/bar_charts.html", context)


def test_json(request):
    data = DATA
    return JsonResponse(data)


def tablets_per_region(request):
    tablets = (
        Tablet.objects.values("region")
        .annotate(total=Count("region_id"))
        .order_by("-total")
    )
    payload = []
    for x in tablets:
        if x["region"] is not None:
            temp_region = Region.objects.get(id=int(x["region"]))
            entry = [temp_region.name, x["total"]]
            payload.append(entry)
        else:
            if x["total"] > 0:
                entry = ["None", x["total"]]
                payload.append(entry)
    data = {
        "items": len(Tablet.objects.all()),
        "title": "Tablets per Region",
        "subtitle": "Distribution of Tablets over Regions",
        "legendx": "Region",
        "legendy": "# of Tablets",
        "measuredObject": "Tablets",
        "payload": payload,
    }
    return JsonResponse(data)


def tablets_per_scribe(request):
    tablets = (
        Tablet.objects.values("scribe")
        .annotate(total=Count("scribe_id"))
        .order_by("-total")
    )
    payload = []
    for x in tablets:
        if x["scribe"] is not None:
            temp_scribe = Scribe.objects.get(id=int(x["scribe"]))
            entry = [temp_scribe.name, x["total"]]
            payload.append(entry)
        else:
            if x["total"] > 0:
                entry = ["None", x["total"]]
                payload.append(entry)
    data = {
        "items": len(Tablet.objects.all()),
        "title": "Tablets per Scribe",
        "subtitle": "Distribution of Tablets over Scribes",
        "legendx": "Scribe",
        "legendy": "# of Tablets",
        "measuredObject": "Tablets",
        "payload": payload,
    }
    return JsonResponse(data)


def tablets_per_period(request):
    tablets = (
        Tablet.objects.values("period")
        .annotate(total=Count("period_id"))
        .order_by("-total")
    )
    payload = []
    for x in tablets:
        if x["period"] is not None:
            temp_period = Period.objects.get(id=int(x["period"]))
            entry = [temp_period.name, x["total"]]
            payload.append(entry)
        else:
            if x["total"] > 0:
                entry = ["None", x["total"]]
                payload.append(entry)
    data = {
        "items": len(Tablet.objects.all()),
        "title": "Tablets per Period",
        "subtitle": "Distribution of Tablets over Periods",
        "legendx": "Period",
        "legendy": "# of Tablets",
        "measuredObject": "Tablets",
        "payload": payload,
    }
    return JsonResponse(data)


def glyphs_per_sign(request):
    glyphs = (
        Glyph.objects.values("sign")
        .annotate(totalcount=Count("sign"))
        .order_by("-totalcount")
    )
    payload = []
    for x in glyphs:
        if x["totalcount"] is not None:
            temp_sign = Sign.objects.get(id=int(x["sign"]))
            entry = [
                "{} ({})".format(temp_sign.sign_name, temp_sign.abz_number),
                x["totalcount"],
            ]
            payload.append(entry)
        else:
            if x["totalcount"] > 0:
                entry = ["None", x["totalcount"]]
                payload.append(entry)
    data = {
        "items": len(Glyph.objects.all()),
        "title": "Glyphs per Sign",
        "subtitle": "Distribution of Glyphs over Signs",
        "legendx": "Sign",
        "legendy": "# of Glyphs",
        "measuredObject": "Glyphs",
        "payload": payload,
    }
    return JsonResponse(data)
