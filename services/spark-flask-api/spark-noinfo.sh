# Deactivate INFO
cp handler/log4j.properties conf/log4j.properties

# Run version header and program from CLI flags
# ./bin/spark-submit version.py
python3 version.py
./bin/spark-submit $@
