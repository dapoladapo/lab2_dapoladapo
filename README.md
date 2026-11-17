# ALU Transcript generator
A Python application and Bash script that calculates a student's final academic standing based on a CSV file of course grades and archives that CSV file so the next batch of grades can be entered. 

## Features
- Accesses grades from a CSV file that the user gives
- Validates that every score is between 0 and 100 and each weight add up respectively (Formatives = 60, Summative = 40 and Total = 100)
- Calculates the final grade and GPA
- Decides whether student has passed or failed
- Finds the failed formative assignment with the highest weight for resubmission. 
- Clear error messages for user understanding and no crashes
- Shell script that archives the CSV file with timestamp and creates a fresh CSV file

## Technologies USed
- **Language:** Python, Bash. 
- **Database:** No database used (Data was stored in a CSV file)
- **Libraries:** Python libraries (csv, sys and os)

## Files
| File | Purpose |
|---|---|
| `grade-evaluator.py` | Loads the CSV grades, validates it, calculates the GPA, decides whether student passed or failed and displays formative(s) that are available for resubmission |
| `organizer.sh` | Archives CSV file with a timestamp and creates a fresh empty CSV file |
| `grades.csv` | Sample course data |
| `README.md` | A file that documents the project and needed information about it |

## Project Structure
```text
Current_working_directory/
├── grade-evaluator.py   
├── organizer.sh         
├── grades.csv           
└── README.md            
```

And after running the `organizer.sh`, the following will be added
```text
├── archive/             
└── organizer.log        
```

## Requirements
- Python 3 with standard libraries
- Bash

## Setup 
1. Firstly make sure you have the requirements 
2. Clone the repository

## How to run

In your terminal
```bash
python grade-evaluator.py
```

When you are prompted, type the CSV filename that holds the grades

### CSV Format
The CSV file must follow the exact header fieldname in this order

| Assignment | Group | Score | Weight |
| --- | --- | --- | --- |
| assignment | assignment group (Summative or Formative) | assignment score (must be a number) | assignment weight (must be a number)

For Example:

```csv
assignment,group,score,weight
Quiz,Formative,85,20
Group Exercise,Formative,40,20
Functions and Debugging Lab,Formative,45,20
Midterm Project - Simple Calculator,Summative,70,20
Final Project - Text-Based Game,Summative,60,20
```

### Sample Output
```text
Enter the name of the CSV file to process (e.g., grades.csv): grades.csv

--- Processing Grades ---

 ----- Assignment stats -----
Assignment: Quiz | Category: Formative | Score: 85.0 | Weight: 20.0
Assignment: Group Exercise | Category: Formative | Score: 40.0 | Weight: 20.0
Assignment: Functions and Debugging Lab | Category: Formative | Score: 45.0 | Weight: 20.0
Assignment: Midterm Project - Simple Calculator | Category: Summative | Score: 70.0 | Weight: 20.0
Assignment: Final Project - Text-Based Game | Category: Summative | Score: 60.0 | Weight: 20.0

 ----- Evaluation results -----
Formative: 34.0/60.0 --- (56.666666666666664%)
Summative: 26.0/40.0 --- (65.0%)
GPA: 3.0
Status: PASSED
These are the assignments available for resubmission
Group Exercise
Functions and Debugging Lab
```
### Shell script organizer

**How to run**
```bash
bash organizer.sh
```
**Example log entry:**
```text
20251105-170000 | Original file: grades.csv | Archived file: archive/grades_20251105-170000.csv
```

##Author 
David Oladapo
Github: dapoladapo