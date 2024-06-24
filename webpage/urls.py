from django.urls import re_path, path
from django.contrib import admin
from . import views

app_name = "webpage"

urlpatterns = [
    path("imprint", views.ImprintView.as_view(), name="imprint"),
    re_path(r"^admin/", admin.site.urls),
    re_path(r"^(?!admin)(?P<template>\w*)$", views.template_view, name="template"),
    re_path(r"^login/$", views.user_login, name="user_login"),
    re_path(r"^accounts/login/$", views.user_login, name="user_login"),
    re_path(r"^logout/$", views.user_logout, name="user_logout"),
    re_path(r"^project-info/$", views.project_info, name="project_info"),
]
