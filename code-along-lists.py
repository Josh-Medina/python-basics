# Create an empty list

todo_list = []
print("your todo list:", todo_list)

# Append items to the list

todo_list.append("Buy goceries")
todo_list.append("Finish homework")
todo_list.append("Call mom")

print("Updated list", todo_list)

# Intsert an item

todo_list.insert(1, "Pay bills")
print("After inserting an item:", todo_list)

# Using indexes & slicing

print("First task:", todo_list[0])
print("Last two tasks:", todo_list[-2:])

# Mark a task as done

done_task = todo_list.pop(2)
print("You completed:", done_task)
print("Todo list after removal:", todo_list)

# update an existing task
print(todo_list[1])
todo_list[1] = "Buy groceries and snacks"
print("Updated todo list:", todo_list)

# Print a task list

print("Here's what you still need to do:")
for task in todo_list:
    print("-", task)
