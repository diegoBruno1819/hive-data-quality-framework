import subprocess

def check_duplicates(table):

    with open("sql/duplicates_query.sql") as file:
        query = file.read().format(table=table)

    result = subprocess.check_output(["hive", "-e", query])

    duplicates = result.decode().strip()

    return {"duplicates_found": duplicates}
