# lab1_jlouange
Python application that calculates a student's final academic standing based on a pre-existing CSV file of course grades

# Lab 1 - Grade Evaluator & Archiver

## Files

```
lab1_jlouange/
├── grade-evaluator.py
├── organizer.sh
└── README.md
```

## Requirements

- Python 3
- Bash

## Running the Python Application

1. Ensure `grades.csv` is in the same directory as `grade-evaluator.py`.
2. Run:

```bash
python3 grade-evaluator.py
```

3. When prompted, enter the CSV filename:

```text
grades.csv
```

The program will:

- Validate assignment scores (0–100)
- Validate assignment weights (100 total, 60 Formative, 40 Summative)
- Calculate the final grade and GPA
- Determine PASS or FAIL
- Display eligible formative assignment(s) for resubmission

## Running the Shell Script

Make the script executable:

```bash
chmod +x organizer.sh
```

Run the script:

```bash
./organizer.sh
```

The script will:

- Create an `archive` directory if it does not exist.
- Rename and archive `grades.csv` using a timestamp.
- Create a new empty `grades.csv`.
- Append the archival information to `organizer.log`.
