import sys

SPARK_VERSION = "2.3.0"
PYTHON_VERSION = str(sys.version).split(' ')[0]

print()
print("==== APACHE SPARK DOCKER CONTAINER ====")
print("Apache Spark version: " + str(SPARK_VERSION))
print("Python interpreter version: " + str(PYTHON_VERSION))
print()
