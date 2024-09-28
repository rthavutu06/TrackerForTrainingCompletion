# Training Completion Tracker

## Description

The **Training Completion Tracker** is a Python console application designed to process training completion data from a JSON file. This application analyzes training records to provide insights into training counts, fiscal year completions, and expiration statuses.

## Features

- **Count Completions**: Lists each completed training along with the count of how many individuals have completed it.
- **Fiscal Year Analysis**: Identifies individuals who completed specific trainings during the fiscal year 2024.
- **Expiration Tracking**: Detects trainings that have expired or will expire within one month from a specified date, providing a status for each training.

## Requirements

- Python 3.x
- JSON data file (`trainings.txt`) in the same directory as the script.

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/rthavutu06/TrackerForTrainingCompletion.git
   ```
2. Navigate to the project directory:
   ```bash
   cd TrainingCompletionTracker
   ```
3. Ensure you have Python installed.
4. Run the application:
   ```bash
   python training_app.py
   ```

## Output Files

The application generates three JSON files:

- `task_1_output.json`: Count of completed trainings.
- `task_2_output.json`: List of people who completed specific trainings in FY 2024.
- `task_3_output.json`: People with expired or soon-to-expire trainings.

## License

This project is licensed under the MIT License.
