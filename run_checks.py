import yaml
from checks.check_duplicates import check_duplicates
from checks.check_nulls import check_nulls
from checks.check_rowcount import check_rowcount
from reports.report_generator import generate_report


def main():

    with open("config.yaml") as file:
        config = yaml.safe_load(file)

    database = config["hive"]["database"]
    table = config["hive"]["table"]

    full_table = f"{database}.{table}"

    results = []

    if "duplicates" in config["checks"]:
        results.append(check_duplicates(full_table))

    if "nulls" in config["checks"]:
        results.append(check_nulls(full_table))

    if "rowcount" in config["checks"]:
        results.append(check_rowcount(full_table))

    generate_report(results)


if __name__ == "__main__":
    main()
