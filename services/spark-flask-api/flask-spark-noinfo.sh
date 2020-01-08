# Deactivate INFO
# pwd
# ls -l
# cp handler/log4j.properties conf/log4j.properties

# Run version header and program from CLI flags
# pwd
# ./bin/spark-submit version.py
# python3 version.py
# ./bin/spark-submit $@

# Start API, port 5000
cd /api
FLASK_APP=api.py flask run
