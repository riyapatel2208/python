import re
from collections import defaultdict

def parse_registration_data(data):
    lines = data.strip().splitlines()
    header = [field.strip() for field in lines[0].split(",")]
    
    records = []
    for line in lines[1:]:
        fields = [field.strip() for field in line.split(",")]
        if len(fields) == len(header):
            records.append(dict(zip(header, fields)))
    
    return records

def count_non_students(records):
    # Check for non-student entries by looking for occupations that are NOT 'student' (case insensitive)
    non_students = [r for r in records if not r.get('occupation', '').lower().startswith('student')]
    return len(non_students)

def find_iit_participants(records):
    iit_participants = [r for r in records if 'IIT' in r.get('affiliation', '').upper()]
    return iit_participants

def find_duplicate_records(records):
    seen = set()
    duplicates = []
    for r in records:
        identifier = (r.get('name', ''), r.get('email', ''))
        if identifier in seen:
            duplicates.append(r)
        else:
            seen.add(identifier)
    return duplicates

def group_by_affiliation(records):
    affiliation_groups = defaultdict(list)
    for r in records:
        affiliation_groups[r.get('affiliation', '')].append(r)
    return affiliation_groups

def main():
    data = """
    name,email,occupation,affiliation
    Alice,alice@example.com,student,IIT Bombay
    Bob,bob@example.com,non-student,XYZ Corp
    Charlie,charlie@example.com,student,IIT Delhi
    Alice,alice@example.com,student,IIT Bombay
    Eve,eve@example.com,non-student,ABC Ltd
    Frank,frank@example.com,non-student,IIT Kanpur
    """
    
    records = parse_registration_data(data)

    non_students_count = count_non_students(records)
    print(f"Number of non-student registrants: {non_students_count}")
    
    iit_participants = find_iit_participants(records)
    print("People registered from IITs:")
    for participant in iit_participants:
        print(participant.get('name'))
    
    duplicates = find_duplicate_records(records)
    print("Duplicate records:")
    for dup in duplicates:
        print(dup.get('name'), dup.get('email'))

    affiliation_groups = group_by_affiliation(records)
    print("Participants grouped by affiliation:")
    for affiliation, participants in affiliation_groups.items():
        print(f"{affiliation}:")
        for p in participants:
            print(f"  {p.get('name')}")

if __name__ == "__main__":
    main()
