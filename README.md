
## Instructions

### Main Logic (`main.py`)

1. **Fetching Data:**
   - `get_users()`: Fetches the list of users.
   - `get_todos()`: Fetches the list of to-dos.

2. **Identifying FanCode City Users:**
   - `is_fancode_city(lat, lng)`: Checks if a user is from FanCode City based on latitude and longitude.
   - `get_fancode_users(users)`: Filters users who are from FanCode City.

3. **Calculating Completed Tasks Percentage:**
   - `calculate_completed_tasks_percentage(todos, user_id)`: Calculates the percentage of tasks completed by a user.

4. **Main Execution:**
   - The `main()` function fetches the users and tasks data, filters FanCode City users, calculates their task completion percentage, and prints those with more than 50% tasks completed.

### Unit Tests (`test_user_todos.py`)

1. **Setup:**
   - `setUpClass()`: Fetches users and tasks data once for all tests.

2. **Tests:**
   - `test_get_fancode_users()`: Verifies that the latitude and longitude of FanCode City users fall within the specified ranges.
   - `test_calculate_completed_tasks_percentage()`: Ensures that the task completion percentage is a float between 0 and 100.
   - `test_users_with_more_than_50_percent_tasks_completed()`: Checks that the calculated percentages are valid.

## Running the Project

### Execute the Main Logic

Run the `main.py` file:

