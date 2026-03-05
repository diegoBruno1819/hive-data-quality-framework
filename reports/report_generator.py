def generate_report(results):

    print("\nDATA QUALITY REPORT")
    print("----------------------")

    for result in results:
        for key, value in result.items():
            print(f"{key}: {value}")

    print("----------------------\n")
