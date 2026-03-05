import subprocess


def check_duplicates(table):

    query = f"""
    SELECT COUNT(*)
    FROM (
        SELECT id, COUNT(*)
        FROM {table}
        GROUP BY id
        HAVING COUNT(*) > 1
    ) t
    """

    result = subprocess.check_output(["hive", "-e", query])

    duplicates = result.decode().strip()

    return {"duplicates_found": duplicates}
