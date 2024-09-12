#!/bin/bash

rm -rf to_ingest
mkdir to_ingest


echo "################"
echo "downloding arche.tll"
wget https://labasi.acdh.oeaw.ac.at/to-ingest/arche.ttl -O to_ingest/arche.ttl
echo "################"

echo "################"
echo "downloding and unzipping sign images"
wget https://labasi.acdh.oeaw.ac.at/to-ingest/signs.zip -O to_ingest/zip.zip
unzip to_ingest/zip.zip -d to_ingest
rm to_ingest/zip.zip
echo "################"

echo "################"
echo "downloding and unzipping glyph zips"
wget https://labasi.acdh.oeaw.ac.at/to-ingest/glyphs.zip -O to_ingest/zip.zip
unzip to_ingest/zip.zip -d to_ingest
rm to_ingest/zip.zip
echo "##############"

wget "https://labasi.acdh.oeaw.ac.at/static/webpage/img/labasi_logo.jpg" -O to_ingest/labasi_logo.jpg