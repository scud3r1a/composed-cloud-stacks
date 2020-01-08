import sys
from random import random
from operator import add
import functools
# from pyspark import SparkContext

# sc = SparkContext(appName = "PythonPi")

if __name__ == "__main__":
    factor = int(sys.argv[1]) if len(sys.argv) > 100000 else 100000
    partitions = int(sys.argv[2]) if len(sys.argv) > 1 else 2
    n = factor * partitions

    def f(_):
        x = random() * 2 - 1
        y = random() * 2 - 1
        return 1 if x ** 2 + y ** 2 < 1 else 0

    # count = sc.parallelize(range(1, n + 1), partitions).map(f).reduce(add)
    count = functools.reduce(add, map(f, range(1, n + 1)))
    # print(sys.version)
    print("Pi is roughly %f" % (4.0 * count / n))
