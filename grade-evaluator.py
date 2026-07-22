import csv
import sys
import os

def load_csv_data():
    """
    Prompts the user for a filename, checks if it exists, 
    and extracts all fields into a list of dictionaries.
    """
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")
    
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
        
    assignments = []
    
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert numeric fields to floats for calculations
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        return assignments
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

def evaluate_grades(data=[]):
    """
    Implement your logic here.
    'data' is a list of dictionaries containing the assignment records.
    """
    print("\n--- Processing Grades ---")

    if not data:
        print("CSV file is empty.")
        return
    
    # TODO: a) Check if all scores are percentage based (0-100)
    for assignment in data:
        if assignment["score"] < 0 or assignment["score"] > 100:
            print("Score must be between 0 and 100")
            sys.exit(1)
    print()
       
    # TODO: b) Validate total weights (Total=100, Summative=40, Formative=60)
    Total_weight = 0

    for assignment in data:
        Total_weight += assignment['weight']

    if Total_weight != 100: 
        print("Total weight must be 100 !") 
        sys.exit(1)

    formative_total = 0
    summative_total = 0

    for assignment  in data:
        if assignment['group'] == 'Formative':
            formative_total += assignment['weight']
        if assignment['group'] == 'Summative':
            summative_total += assignment['weight']

    if formative_total != 60:
        print(f"Error: Formative weight must be 60 ")
        sys.exit(1)
    elif summative_total != 40:
        print(f"Error: Summative weight must be 40 ")
        sys.exit(1)

    # TODO: c) Calculate the Final Grade and GPA
    # TODO: d) Determine Pass/Fail status (>= 50% in BOTH categories)
    # TODO: e) Check for failed formative assignments (< 50%)
    #          and determine which one(s) have the highest weight for resubmission.
    # TODO: f) Print the final decision (PASSED / FAILED) and resubmission options
    
    pass

if __name__ == "__main__":
    # 1. Load the data
    course_data = load_csv_data()
    
    # 2. Process the features
    evaluate_grades(course_data)