import subprocess

def check_nulls(table):

    with open("sql/nulls_query.sql") as file:
        query = file.read().format(table=table)

    result = subprocess.check_output(["hive", "-e", query])

    nulls = result.decode().strip()

    return {"null_values": nulls}
