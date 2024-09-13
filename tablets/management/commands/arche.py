import os
from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from rdflib import Namespace, Graph, URIRef, Literal, RDF
from tqdm import tqdm

from tablets.models import Tablet, Sign


class Command(BaseCommand):
    help = "generates ARCHE metadata"

    def handle(self, *args, **kwargs):
        SEED_FILE_DIR = settings.SEED_FILE_DIR
        ACDH = Namespace("https://vocabs.acdh.oeaw.ac.at/schema#")
        LABASI = Namespace("https://id.acdh.oeaw.ac.at/labasi/")
        ARCHE_ROOT = settings.ARCHE_ROOT
        ARCHE_MD_FILE = os.path.join(ARCHE_ROOT, "arche.ttl")

        print(f"loading constants into Graph from {ARCHE_ROOT}")
        g = Graph().parse(os.path.join(SEED_FILE_DIR, "arche_constants.ttl"))
        g_repo_objects = Graph().parse(
            os.path.join(SEED_FILE_DIR, "repo_objects_constants.ttl")
        )
        print("processing Tablets")
        for x in tqdm(Tablet.objects.exclude(title="")):
            uri = URIRef(LABASI[f"tablet_{x.id:03}.xml"])
            g.add((uri, RDF.type, ACDH["Resource"]))
            g.add((uri, ACDH["hasTitle"], Literal(x.title, lang="und")))
            g.add(
                (
                    uri,
                    ACDH["hasUrl"],
                    Literal(f"https://labasi.acdh.oeaw.ac.at/tablets/detail/{x.id}"),
                )
            )
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

        print("processing Signs")
        for x in tqdm(Sign.objects.exclude(sign_name="").exclude(image_1="")):
            # SIGN COLLECTION #
            col_uri = URIRef(LABASI[f"{slugify(x.sign_name)}-{x.id}"])
            g.add((col_uri, RDF.type, ACDH["Collection"]))
            g.add(
                (
                    col_uri,
                    ACDH["hasTitle"],
                    Literal(
                        f"Standard sign and glyph images for: {x.sign_name}", lang="und"
                    ),
                )
            )
            if x.abz_number:
                g.add(
                    (
                        col_uri,
                        ACDH["hasNonLinkedIdentifier"],
                        Literal(f"ABZ no. {x.abz_number}", lang="en"),
                    )
                )
            if x.meszl_number:
                g.add(
                    (
                        col_uri,
                        ACDH["hasNonLinkedIdentifier"],
                        Literal(f"MesZL no. {x.meszl_number}", lang="en"),
                    )
                )
            g.add(
                (
                    col_uri,
                    ACDH["isPartOf"],
                    URIRef("https://id.acdh.oeaw.ac.at/labasi/signs"),
                )
            )

            # SIGN IMAGE #
            uri_id = str(x.image_1).split("/")[-1]
            uri = URIRef(LABASI[uri_id])
            g.add((uri, RDF.type, ACDH["Resource"]))
            has_title = f"Image for Standardsign: {x.sign_name}"
            g.add((uri, ACDH["hasTitle"], Literal(has_title, lang="und")))
            g.add(
                (
                    uri,
                    ACDH["hasUrl"],
                    Literal(
                        f"https://labasi.acdh.oeaw.ac.at/tablets/sign/detail/{x.id}"
                    ),
                )
            )
            g.add(
                (
                    uri,
                    ACDH["hasCategory"],
                    URIRef("https://vocabs.acdh.oeaw.ac.at/archecategory/image"),
                )
            )
            g.add(
                (
                    uri,
                    ACDH["hasLicense"],
                    URIRef("https://vocabs.acdh.oeaw.ac.at/archelicenses/cc-by-4-0"),
                )
            )
            g.add(
                (
                    uri,
                    ACDH["isPartOf"],
                    col_uri,
                )
            )

            # GLYPH IMAGE #
            zip_uri = URIRef(LABASI[f"{slugify(x.sign_name)}-{x.id}.zip"])
            g.add((zip_uri, RDF.type, ACDH["Resource"]))
            g.add(
                (
                    zip_uri,
                    ACDH["hasCategory"],
                    URIRef("https://vocabs.acdh.oeaw.ac.at/archecategory/collection"),
                )
            )
            g.add(
                (
                    zip_uri,
                    ACDH["hasTitle"],
                    Literal(f"Zip file of glyph images for: {x.sign_name}", lang="und"),
                )
            )
            g.add(
                (
                    zip_uri,
                    ACDH["hasLicense"],
                    URIRef("https://vocabs.acdh.oeaw.ac.at/archelicenses/cc-by-4-0"),
                )
            )
            g.add(
                (
                    zip_uri,
                    ACDH["hasExtent"],
                    Literal(
                        f"This Zip files holds {x.glyph_set.all().count()} glyph images",
                        lang="en",
                    ),
                )
            )
            g.add(
                (
                    zip_uri,
                    ACDH["isPartOf"],
                    col_uri,
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

        print("fetching title image info")
        title_image_graph = Graph().parse(
            os.path.join(SEED_FILE_DIR, "title_image.ttl")
        )
        final_g = g + title_image_graph
        print(f"serializing graph into {ARCHE_MD_FILE}")
        final_g.serialize(ARCHE_MD_FILE)

        return ARCHE_MD_FILE
