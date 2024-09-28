import json
from datetime import datetime, timedelta

# Step 1: Read the JSON data from the file
with open('trainings.txt', 'r') as file:
    data = json.load(file)

# Task 1: Count completions
training_counts = {}
for person in data:
    completions = person.get('completions', [])
    for completion in completions:
        training_name = completion['name']
        if training_name in training_counts:
            training_counts[training_name] += 1
        else:
            training_counts[training_name] = 1

print("\n--- Task 1 Output ---")
print(json.dumps(training_counts, indent=4))

# Task 2: List people who completed specific trainings
target_trainings = ["Electrical Safety for Labs", "X-Ray Safety", "Laboratory Safety Training"]
fiscal_year_start = datetime(2023, 7, 1)
fiscal_year_end = datetime(2024, 6, 30)
completed_trainings_in_fy = {}

for person in data:
    completions = person.get('completions', [])
    recent_completions = {}
    for completion in completions:
        training_name = completion['name']
        timestamp = datetime.strptime(completion['timestamp'], '%m/%d/%Y')
        
        # Add condition to check if the training is in target_trainings
        if training_name in target_trainings and fiscal_year_start <= timestamp <= fiscal_year_end:
            if training_name not in recent_completions or timestamp > recent_completions[training_name]['timestamp']:
                recent_completions[training_name] = {'name': person['name'], 'timestamp': timestamp}
    
    for training_name, info in recent_completions.items():
        if info['name'] not in completed_trainings_in_fy:
            completed_trainings_in_fy[info['name']] = []
        completed_trainings_in_fy[info['name']].append(training_name)

print("\n--- Task 2 Output ---")
print(json.dumps(completed_trainings_in_fy, indent=4))


# Task 3: Find expired or soon-to-expire trainings
check_date = datetime(2023, 10, 1)
one_month_later = check_date + timedelta(days=30)
expired_or_soon_expiring = {}

for person in data:
    completions = person.get('completions', [])
    for completion in completions:
        training_name = completion['name']
        expires = completion.get('expires')
        if expires:
            expiration_date = datetime.strptime(expires, '%m/%d/%Y')
            if expiration_date < check_date:
                status = "expired"
            elif check_date <= expiration_date <= one_month_later:
                status = "expires soon"
            else:
                continue
            
            if person['name'] not in expired_or_soon_expiring:
                expired_or_soon_expiring[person['name']] = []
            expired_or_soon_expiring[person['name']].append({
                'training': training_name,
                'status': status
            })

print("\n--- Task 3 Output ---")
print(json.dumps(expired_or_soon_expiring, indent=4))

# Write output to JSON files
with open('task_1_output.json', 'w') as f:
    json.dump(training_counts, f, indent=4)

with open('task_2_output.json', 'w') as f:
    json.dump(completed_trainings_in_fy, f, indent=4)

with open('task_3_output.json', 'w') as f:
    json.dump(expired_or_soon_expiring, f, indent=4)
