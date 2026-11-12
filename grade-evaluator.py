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
        if not assignment['score'] <= 0 or assignment['score'] >= 100:
            continue
        else:
            print (f"Error: {assignment['assignment']} has a false score not within the range 0-100.")
            exit

    # TODO: b) Validate total weights (Total=100, Summative=40, Formative=60)
    for assignment in data:
        #Sums up all the weights depending on their category
        if assignment['group'] == 'Formative':
            validate_formative_score = 0
            assignment['weight'] += validate_formative_score
        elif assignment['group'] == 'Summative':
            validate_summative_score = 0
            assignment['weight'] += validate_summative_score
        else:
            print (f"Error: {assignment['assignment']} has a false group. It must be a 'Formative' or 'Summative'.")
            exit

    #Validating the weights
    if validate_formative_score != 60.0:
        print (f"The sum of weights for each formative does not equal to 60. Please adjust values")
        exit
    elif validate_summative_score != 40.0:
        print (f"The sum of weights for each formative does not equal to 40. Please adjust values")
        exit
    else:
        Total_weight = validate_formative_score + validate_summative_score
        if Total_weight != 100.0:
            print (f"The total weight between formatives and summatives does not equal to 100")
        else:
            print ("Total weight = 100 \n Formative total weight = 60 \n Summative total weight = 40")

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
            exit

    #calculation the number for each formative 
    GPA = (((total_weighted_formative_score + total_weighted_summative_score) / 100) * 5.0)
    print (f"Students GPA: {GPA}")

    # TODO: d) Determine Pass/Fail status (>= 50% in BOTH categories)

    #Calculating if passed 50%
    if ((total_weighted_formative_score/60) * 100) >= 50 and ((total_weighted_summative_score/40) * 100):
        passed: True
    else:
        passed: False

    # TODO: e) Check for failed formative assignments (< 50%) and determine which one(s) have the highest weight for resubmission.

    failed_formative = []

    for assignment in data:
        if assignment['group'] == 'Formative' and assignment['score'] < 50:
            


    # TODO: f) Print the final decision (PASSED / FAILED) and resubmission options
    pass

if __name__ == "__main__":
    # 1. Load the data
    course_data = load_csv_data()
    
    # 2. Process the features
    evaluate_grades(course_data)