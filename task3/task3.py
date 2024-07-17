import json

def fill_value_graph(
        tests: list[dict],
        values: list[dict]
):
    for test in tests:
        _id = test.get("id")
        for value in values:
            if value["id"] == _id:
                test["value"] = value["value"]
        if _values := test.get("values"):
            fill_value_graph(_values, values)


values_path = input("Values file: ")
tests_path = input("Tests file: ")
report_path = input("Report file: ")

with open(values_path, 'r') as values_file:
    values = json.load(values_file).get("values")

with open(tests_path, 'r') as tests_file:
    tests = json.load(tests_file).get("tests")
    fill_value_graph(tests=tests, values=values)

with open(report_path, 'w') as report_file:
    json.dump(tests, report_file)

