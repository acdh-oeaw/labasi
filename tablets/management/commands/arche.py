import os
from django.conf import settings
from django.core.management.base import BaseCommand
from rdflib import Namespace, Graph, URIRef, Literal, RDF

from tablets.models import Tablet


class Command(BaseCommand):
    help = "generates ARCHE metadata"

    def handle(self, *args, **kwargs):
        SEED_FILE_DIR = settings.SEED_FILE_DIR
        ACDH = Namespace("https://vocabs.acdh.oeaw.ac.at/schema#")
        LABASI = Namespace("https://id.acdh.oeaw.ac.at/labasi/")
        ARCHE_ROOT = settings.ARCHE_ROOT
        ARCHE_MD_FILE = os.path.join(ARCHE_ROOT, "arche.ttl")

        g = Graph().parse(os.path.join(SEED_FILE_DIR, "arche_constants.ttl"))
        g_repo_objects = Graph().parse(
            os.path.join(SEED_FILE_DIR, "repo_objects_constants.ttl")
        )

        for x in Tablet.objects.exclude(title="")[:10]:
            uri = URIRef(LABASI[f"tablet_{x.id:03}.xml"])
            g.add((uri, RDF.type, ACDH["Resource"]))
            if x.title:
                g.add((uri, ACDH["hasTitle"], Literal(x.title, lang="und")))
            else:
                continue
            g.add(
                (
                    uri,
                    ACDH["hasCategory"],
                    URIRef("https://vocabs.acdh.oeaw.ac.at/archecategory/text/tei"),
                )
            )
            g.add(
                (
                    uri,
                    ACDH["hasLicense"],
                    URIRef("https://vocabs.acdh.oeaw.ac.at/archelicenses/cc-by-4-0"),
                )
            )
            if x.cdli_no:
                g.add(
                    (
                        uri,
                        ACDH["hasNonLinkedIdentifier"],
                        Literal(f"CDLI no. {x.cdli_no}", lang="en"),
                    )
                )
            if x.nabucco_no:
                g.add(
                    (
                        uri,
                        ACDH["hasNonLinkedIdentifier"],
                        Literal(f"NABUCCO no. {x.nabucco_no}", lang="en"),
                    )
                )
            g.add(
                (
                    uri,
                    ACDH["isPartOf"],
                    URIRef("https://id.acdh.oeaw.ac.at/labasi/tablets"),
                )
            )

        print("adding repo objects constants now")
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
