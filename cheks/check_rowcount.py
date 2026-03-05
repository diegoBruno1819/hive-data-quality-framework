import subprocess


def check_rowcount(table):

    query = f"""
    SELECT COUNT(*)
    FROM {table}
    """

    result = subprocess.check_output(["hive", "-e", query])

    rows = result.decode().strip()

    return {"row_count": rows}
