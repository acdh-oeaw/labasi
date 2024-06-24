import uuid
from django.utils.text import slugify
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import DeleteView
from django.views.static import serve
from django.urls import reverse_lazy
from .models import Tablet, Glyph, TabletImage, Sign
from .forms import TabletForm, SignForm, GlyphForm, TabletImageForm, CutForm
from vocabularies.models import Region, Period


@login_required
def protected_serve(request, pic):
    show_indexes = "media/tablet_img/"
    pic = pic
    return serve(request, pic, show_indexes)


def tablet_to_tei(request, pk):
    instance = get_object_or_404(Tablet, id=pk)
    context = {"object": instance}
    try:
        context["glyph_list"] = Glyph.objects.filter(tablet=pk)
    except:  # noqa:
        pass
    return render(
        request,
        "tablets/tablet_to_tei.html",
        context,
        content_type="application/xhtml+xml",
    )


class TabletImageDetailView(DetailView):
    model = TabletImage

    def get_context_data(self, **kwargs):
        context = super(TabletImageDetailView, self).get_context_data(**kwargs)
        current_object = self.object
        context["glyph_list"] = Glyph.objects.filter(tablet=current_object.tablet.id)
        return context


@login_required
def cut_tabletImg(request, pk):
    context = {}
    context["object"] = get_object_or_404(TabletImage, id=pk)
    instance = TabletImage.objects.get(id=pk)
    context["glyph_list"] = Glyph.objects.filter(tablet=instance.tablet.id)
    identifier = "{}__{}".format(str(uuid.uuid4()), slugify(instance.tablet.title))
    if request.method == "GET":
        context["form"] = CutForm({"tablet": instance.tablet, "identifier": identifier})
        return render(request, "tablets/cut_tabletimg.html", context)
    elif request.method == "POST":
        context["form"] = CutForm(request.POST, request.FILES)
        if context["form"].is_valid():
            context["form"].save()
            return redirect("tablets:tabletimg_detail", pk=instance.id)
        else:
            return render(request, "tablets/cut_tabletimg.html", context)
    else:
        pass


@login_required
def create_tabletImg(request):
    if request.method == "POST":
        form = TabletImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("browsing:browse_tabletimages")
        else:
            return render(request, "tablets/create_tabletimg.html", {"form": form})
    else:
        form = TabletImageForm()
        return render(request, "tablets/create_tabletimg.html", {"form": form})


@login_required
def edit_tabletImg(request, pk):
    instance = get_object_or_404(TabletImage, id=pk)
    if request.method == "POST":
        form = TabletImageForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect("tablets:tabletimg_detail", pk=pk)
        else:
            return render(
                request,
                "tablets/create_tabletimg.html",
                {"form": form, "instance": instance},
            )
    else:
        form = TabletImageForm(instance=instance)
        return render(
            request,
            "tablets/create_tabletimg.html",
            {"form": form, "instance": instance},
        )


class TabletImageDelete(DeleteView):
    model = TabletImage
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("browsing:browse_tabletimages")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TabletImageDelete, self).dispatch(*args, **kwargs)


class GlyphDetailView(DetailView):
    model = Glyph

    def get_context_data(self, **kwargs):
        context = super(GlyphDetailView, self).get_context_data(**kwargs)
        return context


@login_required
def create_glyph(request):
    if request.method == "POST":
        form = GlyphForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("browsing:browse_glyphs")
        else:
            return render(request, "tablets:create_glyph", {"form": form})
    else:
        form = GlyphForm()
        return render(request, "tablets/create_glyph.html", {"form": form})


@login_required
def edit_glyph(request, pk):
    instance = get_object_or_404(Glyph, id=pk)
    if request.method == "POST":
        form = GlyphForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect("tablets:glyph_detail", pk=pk)
        else:
            return render(
                request,
                "tablets/create_glyph.html",
                {"form": form, "instance": instance},
            )
    else:
        form = GlyphForm(instance=instance)
        return render(
            request, "tablets/create_glyph.html", {"form": form, "instance": instance}
        )


class GlyphDelete(DeleteView):
    model = Glyph
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("browsing:browse_glyphs")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GlyphDelete, self).dispatch(*args, **kwargs)


class SignDetailView(DetailView):
    model = Sign
    template_name = "tablets/sign_detail.html"

    def get_context_data(self, **kwargs):
        current_object = self.object
        context = super(SignDetailView, self).get_context_data(**kwargs)
        context["glyph_list"] = Glyph.objects.filter(sign=current_object.id)
        context["glyphs"] = len(context["glyph_list"])
        context["region_list"] = set(
            Region.objects.filter(tablet__glyph__sign=current_object.id).exclude(
                name=""
            )
        )
        context["period_list"] = set(
            Period.objects.filter(tablet__glyph__sign=current_object.id).exclude(
                name=""
            )
        )
        return context


@login_required
def create_sign(request):
    if request.method == "POST":
        form = SignForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("browsing:browse_signs")
        else:
            return render(request, "tablets/create_sign.html", {"form": form})
    else:
        form = SignForm()
        return render(request, "tablets/create_sign.html", {"form": form})


@login_required
def edit_sign(request, pk):
    instance = get_object_or_404(Sign, id=pk)
    if request.method == "POST":
        form = SignForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect("tablets:sign_detail", pk=pk)
        else:
            return render(
                request,
                "tablets/create_sign.html",
                {"form": form, "instance": instance},
            )
    else:
        form = SignForm(instance=instance)
        return render(
            request, "tablets/create_sign.html", {"form": form, "instance": instance}
        )


class SignDelete(DeleteView):
    model = Sign
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("browsing:browse_signs")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SignDelete, self).dispatch(*args, **kwargs)


class TabletDetailView(DetailView):
    model = Tablet

    def get_context_data(self, **kwargs):
        context = super(TabletDetailView, self).get_context_data(**kwargs)
        current_object = self.object
        context["glyph_list"] = Glyph.objects.filter(tablet=current_object.id)
        context["glyphs"] = len(context["glyph_list"])
        context["img_list"] = TabletImage.objects.filter(tablet=current_object.id)
        context["images"] = len(context["img_list"])
        return context


@login_required
def create_tablet(request):
    if request.method == "POST":
        form = TabletForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("browsing:browse_tablets")
        else:
            return render(request, "tablets/create_tablet.html", {"form": form})
    else:
        form = TabletForm()
        return render(request, "tablets/create_tablet.html", {"form": form})


@login_required
def edit_tablet(request, pk):
    instance = get_object_or_404(Tablet, id=pk)
    if request.method == "POST":
        form = TabletForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect("tablets:tablet_detail", pk=pk)
        else:
            return render(
                request,
                "tablets/create_tablet.html",
                {"form": form, "instance": instance},
            )
    else:
        form = TabletForm(instance=instance)
        return render(
            request, "tablets/create_tablet.html", {"form": form, "instance": instance}
        )


class TabletDelete(DeleteView):
    model = Tablet
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("browsing:browse_tablets")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TabletDelete, self).dispatch(*args, **kwargs)
