# Math Diagnostic Scoring Logic (Grades 4–9)

# Input: Dictionary with strand scores (0–100)
# Output: Dictionary with mastery level for each strand

def assess_math_mastery_by_strand(scores_dict):
    """
    Assigns mastery levels based on percent scores per math strand.
    Levels:
    - Mastered: 90–100
    - In Progress: 70–89
    - Not Yet Mastered: < 70
    """
    mastery_results = {}
    for strand, score in scores_dict.items():
        if score >= 90:
            mastery_results[strand] = "Mastered"
        elif score >= 70:
            mastery_results[strand] = "In Progress"
        else:
            mastery_results[strand] = "Not Yet Mastered"
    return mastery_results

def export_results_to_json(results, filename="math_results.json"):
    import json
    with open(filename, "w") as f:
        json.dump(results, f, indent=4)

def export_results_to_csv(results, filename="math_results.csv"):
    import csv
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Strand", "Mastery Level"])
        for strand, level in results.items():
            writer.writerow([strand, level])

# Example input for a student across math strands
student_scores = {
    "Expressions & Equations": 85,
    "Ratios & Proportions": 73,
    "Geometry": 62,
    "Statistics": 91,
    "Number Sense & Operations": 94
}

# Run diagnostic scoring
results = assess_math_mastery_by_strand(student_scores)
print("Math Diagnostic Results:")
for strand, level in results.items():
    print(f"{strand}: {level}")

# Export to JSON and CSV
export_results_to_json(results)
export_results_to_csv(results)
