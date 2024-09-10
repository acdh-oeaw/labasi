#!/bin/bash

pg_dump -d labasi -h localhost -p 5433 -U  labasi -c -f labasi_dump.sql
psql -U postgres -d labasi < labasi_dump.sql
