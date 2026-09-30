from controls import CONTROLS, ITEMS

for ci in ITEMS:
    problems = list(CONTROLS[ci["resourceType"]](ci))
    print("NON_COMPLIANT" if problems else "COMPLIANT", ci["resourceName"])
    for problem in problems:
        print("  " + problem)
