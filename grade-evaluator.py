import csv
import sys
import os
print()
print()
print("=======================")
print("GRADE EVALUATOR")
print("=======================")
print()
print()
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
        # Convert numeric fields to floats for calculations
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if not all([
                    row["assignment"].strip(),
                    row["group"].strip(),
                    row["score"].strip(),
                    row["weight"].strip()
                    ]):
                    print("Error: CSV contains an empty or incomplete row.")
                    sys.exit(1)

                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        return assignments
    except Exception as e:
        print()
        print("----------------------------------------------")
        print(f"An error occurred while reading the file: {e}")
        print("please check the structure of the csv file.\n columns must be: \n assignment,group,score,weight")
        print("----------------------------------------------")
        sys.exit(1)

def evaluate_grades(data):
    """
    Implement your logic here.
    'data' is a list of dictionaries containing the assignment records.
    """
    print("\n--- Processing Grades ---")
    print()

    if not data:
        print("CSV file is empty.")
        print()
        return
    
    # Check if all scores are percentage based (0-100)
    for assignment in data:
        if assignment["score"] < 0 or assignment["score"] > 100:
            print(
                f"Invalid score ({assignment['score']}) "
                f"for '{assignment['assignment']}'. "
                "Scores must be between 0 and 100."
            )
            print()
            sys.exit(1)
    print()
       
    # Validate total weights (Total=100, Summative=40, Formative=60)
    total_weight = 0

    for assignment in data:
        total_weight += assignment['weight']

    if total_weight != 100: 
        print("Total weight must be 100 !") 
        print()
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
        print()
        sys.exit(1)
    if summative_total != 40:
        print(f"Error: Summative weight must be 40 ")
        print()
        sys.exit(1)

    # Calculate the Final Grade and GPA

    total_contribution = 0
    for assignment in data:
        contribution = (assignment['score'] * assignment['weight']) / 100
        total_contribution += contribution

    print(f"The final grade is {total_contribution}%")
    print()

    GPA = (total_contribution / 100) * 5
    print(f"The GPA is {GPA:.3f}")
    print()

    
    # Determine Pass/Fail status (>= 50% in BOTH categories)
    
    
    formative_grades = 0
    summative_grades = 0
    for assignment in data:
        if assignment['group'] == 'Formative':
            formative_contribution = (assignment['score'] * assignment['weight']) / 100
            formative_grades += formative_contribution

        elif assignment['group'] == 'Summative':
            summative_contribution = (assignment['score'] * assignment['weight']) / 100 # x/100 * 100 = x
            summative_grades += summative_contribution
            
    # Print the final decision (PASSED / FAILED) and resubmission options
        
    percentage_formative = (formative_grades / 60) * 100
    percentage_summative = (summative_grades / 40) * 100

    if percentage_formative >= 50 and percentage_summative >= 50:
        print("\nFinal Status: PASSED")
        print()
    else:
        print("\nFinal Status: FAILED")
        print()
    # Check for failed formative assignments (< 50%)
    # and determine which one(s) have the highest weight for resubmission.
  
    assignment_failed = {}
    for assignment in data:
        if assignment['group'] == 'Formative' and assignment['score'] < 50:
            assignment_failed[assignment['assignment']] = assignment['weight']
    assignment_with_max_weight = []
    max_weight = 0
    if not assignment_failed:
        print("No formative assignments require resubmission!")

    else:

        for key, value in assignment_failed.items():
            if not assignment_with_max_weight:
                assignment_with_max_weight.append(key)
                max_weight = value
            else:
                if value > max_weight:
                    assignment_with_max_weight = [key]
                    max_weight = value
                elif value == max_weight:
                    assignment_with_max_weight.append(key)
    if assignment_with_max_weight:
        print("\nEligible for resubmission:")
        print()
        for assignment in assignment_with_max_weight:
            print("-", assignment)
            print()


    
    
    

if __name__ == "__main__":
    # 1. Load the data
    course_data = load_csv_data()
    
    # 2. Process the features
    evaluate_grades(course_data)