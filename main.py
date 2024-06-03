import requests

BASE_URL = "http://jsonplaceholder.typicode.com"

def get_users():
    response = requests.get(f"{BASE_URL}/users")
    response.raise_for_status()
    return response.json()

def get_todos():
    response = requests.get(f"{BASE_URL}/todos")
    response.raise_for_status()
    return response.json()

def is_fancode_city(lat, lng):
    return -40 <= lat <= 5 and 5 <= lng <= 100

def get_fancode_users(users):
    return [
        user for user in users 
        if is_fancode_city(float(user['address']['geo']['lat']), float(user['address']['geo']['lng']))
    ]

def calculate_completed_tasks_percentage(todos, user_id):
    user_todos = [todo for todo in todos if todo['userId'] == user_id]
    if not user_todos:
        return 0
    completed_todos = [todo for todo in user_todos if todo['completed']]
    return (len(completed_todos) / len(user_todos)) * 100

def main():
    users = get_users()
    todos = get_todos()

    fancode_users = get_fancode_users(users)

    results = [
        {
            "user_id": user['id'],
            "name": user['name'],
            "completed_percentage": calculate_completed_tasks_percentage(todos, user['id'])
        }
        for user in fancode_users
    ]

    for result in results:
        if result["completed_percentage"] > 50:
            print(f"User {result['name']} has completed {result['completed_percentage']:.2f}% of their tasks.")

if __name__ == "__main__":
    main()
