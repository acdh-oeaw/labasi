import requests
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView


from .forms import form_user_login
from .metadata import PROJECT_METADATA as PM
from copy import deepcopy


def template_view(request, template):
    if PM is not None:
        context = {"metadata": PM}
    else:
        context = {}
    if template == "":
        selected_template = "webpage/index.html"
    else:
        selected_template = "webpage/{}.html".format(template)
    return render(request, selected_template, context)


#################################################################
#               views for login/logout                          #
#################################################################


def user_login(request):
    if request.method == "POST":
        form = form_user_login(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd["username"], password=cd["password"])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(request.GET.get("next", "/"))
                else:
                    return HttpResponse("not active.")
            else:
                return HttpResponse("user does not exist")
    else:
        form = form_user_login()
        return render(request, "webpage/user_login.html", {"form": form})


def user_logout(request):
    logout(request)
    return render(request, "webpage/user_logout.html")


#################################################################
#                    project info view                          #
#################################################################


def project_info(request):
    """
    returns a dict providing metadata about the current project
    """

    info_dict = deepcopy(PM)

    if request.user.is_authenticated:
        pass
    else:
        del info_dict["matomo_id"]
        del info_dict["matomo_url"]
    info_dict["base_tech"] = "django"
    info_dict["framework"] = "djangobaseproject"
    return JsonResponse(info_dict)


class ImprintView(TemplateView):
    template_name = "webpage/imprint.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        redmine_id = settings.REDMINE_ID
        imprint_url = (
            imprint_url
        ) = f"https://imprint.acdh.oeaw.ac.at/{redmine_id}?locale=en"

        r = requests.get(imprint_url)

        if r.status_code == 200:
            context["imprint_body"] = "{}".format(r.text)
        else:
            context[
                "imprint_body"
            ] = """
            On of our services is currently not available.\
            Please try it later or write an email to\
            acdh@oeaw.ac.at; if you are service provide,\
            make sure that you provided ACDH_IMPRINT_URL and REDMINE_ID
            """
        return context
