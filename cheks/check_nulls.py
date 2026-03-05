import subprocess


def check_nulls(table):

    query = f"""
    SELECT COUNT(*)
    FROM {table}
    WHERE id IS NULL
    """

    result = subprocess.check_output(["hive", "-e", query])

    nulls = result.decode().strip()

    return {"null_values": nulls}
