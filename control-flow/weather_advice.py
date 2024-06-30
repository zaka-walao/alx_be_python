task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        reminder = "Reminder:",task," is a high priority task"
    case "medium":
        reminder = "Reminder: ",task," is a medium priority task"
    case "low":
        reminder = "Note: ",task," is a low priority task"
    case _:
        reminder = "Invalid priority level. Please enter high, medium, or low."

if time_bound == "yes":
    reminder += " that requires immediate attention today!"
elif time_bound == "no":
    reminder += ". Consider completing it when you have free time."
else:
    reminder = "Invalid input for time-bound. Please enter yes or no."

print(reminder)