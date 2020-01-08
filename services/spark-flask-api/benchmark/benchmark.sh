#!/usr/bin/env bash

# Test values
ONE=10000000
TWO=800

# Test functions
echo ""
echo "0) Spark start-up time"
time sudo docker run --rm -v `pwd`:/data scud3r1a/pyspark /data/version.py

echo""
echo "1) Native Python 3"
time sudo docker run --rm --entrypoint=python3 -v `pwd`:/data scud3r1a/pyspark /data/count2.py ${ONE} ${TWO}

echo ""
echo "2) Spark with Python 3 (PySpark)"
time sudo docker run --rm -v `pwd`:/data scud3r1a/pyspark /data/count.py ${ONE} ${TWO} 4
# /data/count.py 10000000 800 4
