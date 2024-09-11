import os
from django.conf import settings
from django.core.management.base import BaseCommand

from rdflib import Namespace, Graph


class Command(BaseCommand):
    help = "generates ARCHE metadata"

    def handle(self, *args, **kwargs):
        SEED_FILE_DIR = settings.SEED_FILE_DIR
        ARCHE_ROOT = settings.ARCHE_ROOT
        ARCHE_MD_FILE = os.path.join(ARCHE_ROOT, "arche.ttl")

        g = Graph().parse(os.path.join(SEED_FILE_DIR, "arche_constants.ttl"))
        g_repo_objects = Graph().parse(
            os.path.join(SEED_FILE_DIR, "repo_objects_constants.ttl")
        )

        ACDH = Namespace("https://vocabs.acdh.oeaw.ac.at/schema#")
        COLS = [ACDH["TopCollection"], ACDH["Collection"], ACDH["Resource"]]
        COL_URIS = set()

        for x in COLS:
            for s in g.subjects(None, x):
                COL_URIS.add(s)
        for x in COL_URIS:
            for p, o in g_repo_objects.predicate_objects():
                g.add((x, p, o))

        g.serialize(ARCHE_MD_FILE)

        return ARCHE_MD_FILE
