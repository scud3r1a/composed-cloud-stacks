import re, sys, os
from minio import Minio

def get_access_secret(filename):
    accessKey = ""
    secretKey = ""

    file = open(filename, "r")

    for line in file:
        if re.search('accessKey', line) or re.search('secretKey', line):
            line = line.strip().replace(" ", "").replace("\"","").replace(",", "").split(":")
            # print(line)

        for i in range(len(line)):
            if line[i] == 'accessKey':
                accessKey = line[i + 1]
            elif line[i] == 'secretKey':
                secretKey = line[i + 1]

    # print(accessKey)
    # os.environ["MINIO_ACCESSKEY"] = accessKey
    # os.environ["MINIO_SECRETKEY"] = secretKey

    # print(secretKey)
    # print(os.environ["MINIO_ACCESSKEY"])
    # print("Done. \'MINIO_ACCESSKEY\' and \'MINIO_SECRETKEY\' stored as \'os.environ\' variables.")

    return [accessKey, secretKey]

def create_client(port, filename):
    minio_client = Minio(
        endpoint="minio:" + str(port),
        access_key=get_access_secret(filename)[0],
        secret_key=get_access_secret(filename)[1],
        secure=False
    )
    return minio_client
