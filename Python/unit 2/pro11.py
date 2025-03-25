import sys

if len(sys.argv) < 2:
    print("usage: python pro11.py a.txt")
    sys.exit(1)

with open(sys.argv[1], 'r') as f:
    total_credit_points = 0
    total_credits = 0
    for record in f:
        details = record.split()
        print(details)

        total_credits += float(details[1]) * float(details[2])

        total_credit_points += float(details[1])

    print("Total of (credits * points):", total_credits)
    print("Total Credits:", total_credit_points)

    cgpa = total_credits / total_credit_points
    print(f"CGPA: {cgpa:.2f}")
