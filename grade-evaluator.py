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



def evaluate_grades(data):
    """
    Implement your logic here.
    'data' is a list of dictionaries containing the assignment records.
    """
    print("\n--- Processing Grades ---")
    
    # TODO: a) Check if all scores are percentage based (0-100)
    for assignment in data: 
        if assignment['score'] < 0 or assignment['score'] > 100:
            print (f"Error: {assignment['assignment']} has a false score not within the range 0-100.")
            sys.exit(1)
        else:
            continue

    # TODO: b) Validate total weights (Total=100, Summative=40, Formative=60)
    validate_formative_score = 0
    validate_summative_score = 0
    for assignment in data:
        #Sums up all the weights depending on their category
        if assignment['group'] == 'Formative':
            validate_formative_score += assignment['weight']
        elif assignment['group'] == 'Summative':
            validate_summative_score += assignment['weight']
        else:
            print (f"Error: {assignment['assignment']} has a false group. It must be a 'Formative' or 'Summative'.")
            sys.exit(1)

    #Validating the weights
    if validate_formative_score != 60.0:
        print (f"The sum of weights for each formative does not equal to 60. Please adjust values")
        sys.exit(1)
    elif validate_summative_score != 40.0:
        print (f"The sum of weights for each formative does not equal to 40. Please adjust values")
        sys.exit(1)
    else:
        Total_weight = validate_formative_score + validate_summative_score
        if Total_weight != 100.0:
            print (f"The total weight between formatives and summatives does not equal to 100")

    # TODO: c) Calculate the Final Grade and GPA
    #Getting the total weighted scores
    total_weighted_formative_score = 0
    total_weighted_summative_score = 0
    
    for assignment in data: 
        if assignment['group'] == 'Formative':
            total_weighted_formative_score += ((assignment['score'] * assignment['weight'])/100)
        elif assignment['group'] == 'Summative':
            total_weighted_summative_score += ((assignment['score'] * assignment['weight'])/100)
        else: 
            print (f"Error: {assignment['assignment']} has a false group. It must be Formative or Summative")
            sys.exit(1)

    #calculation the number for each formative 
    GPA = (((total_weighted_formative_score + total_weighted_summative_score) / 100) * 5.0)
    #print (f"Students GPA: {GPA}")

    # TODO: d) Determine Pass/Fail status (>= 50% in BOTH categories)

    #Calculating if passed 50%
    if ((total_weighted_formative_score/60) * 100) >= 50 and ((total_weighted_summative_score/40) * 100) >= 50:
        passed = True
    else:
        passed = False

    # TODO: e) Check for failed formative assignments (< 50%) and determine which one(s) have the highest weight for resubmission.

    failed_formative = []

    for assignment in data:
        if assignment['group'] == 'Formative' and assignment['score'] < 50:
            failed_formative.append(assignment)
    
    resubmit_formative = []
    if failed_formative: #Checking if there is data in failed_formative list
        highest_weight = failed_formative[0]['weight'] #assigns first weight in the list as highest weight so we compare

        #Compares the assignment weight and the highest_weight assigned at first and updates it if it is higher
        for assignment in failed_formative:
            if assignment['weight'] > highest_weight:
                highest_weight = assignment['weight']

        #Calculates the difference between the highest weight and each assignement's weight and will add to list if its within range
        for assignment in failed_formative:
            difference = highest_weight - assignment['weight']
            if difference <= 0.0001:
                resubmit_formative.append(assignment)


    # TODO: f) Print the final decision (PASSED / FAILED) and resubmission options
    print("\n ----- Assignment stats -----")

    for assignment in data:
        print (f"Assignment: {assignment['assignment']} | Category: {assignment['group']} | Score: {assignment['score']} | Weight: {assignment['weight']}")

    print("\n ----- Evaluation results -----")
    print(f"Formative: {total_weighted_formative_score}/{validate_formative_score} --- ({(total_weighted_formative_score / validate_formative_score) * 100}%)")
    print(f"Summative: {total_weighted_summative_score}/{validate_summative_score} --- ({(total_weighted_summative_score / validate_summative_score)*100}%)")
    print(f"GPA: {GPA}")
    print(f"Status: {'Passed' if passed else 'Failed'}")

    if resubmit_formative:
        print("These are the assignments available for resubmission")
        for assignment in resubmit_formative:
            print(assignment['assignment'])
    else:
        print("There are no formatives that need resubmission")        



if __name__ == "__main__":
    # 1. Load the data
    course_data = load_csv_data()
    
    # 2. Process the features
    evaluate_grades(course_data)