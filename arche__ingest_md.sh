#/bin/bash

echo "ingest metadata for for ${TOPCOLID} into ${ARCHE}"
docker run --rm \
  -v ${PWD}/to-ingest:/data \
  --network="host" \
  --entrypoint arche-import-metadata \
  acdhch/arche-ingest \
  /data/arche.ttl ${ARCHE} ${ARCHE_USER} ${ARCHE_PASSWORD}