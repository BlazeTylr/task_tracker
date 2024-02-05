## 1. Describe the Problem

I can keep track of my tasks

- I want a program that I can add todo tasks to and see a list of them.
- I can focus on tasks to complete
- I want to mark tasks as complete and have them disappear
  from the list.

## 2. Design the Function Signature

```python
# EXAMPLE

class Task_tracker():
    """
    tracking user tasks
    - add a todo
    - see a list of todos
    - be able to mark tasks complete and delete them from the list if they are complete
    """
    pass
```

## 3. Create Examples as Tests

```python

"""
Given a task it will adds it to the tasks list
"""
my_tasks.add("go running") => ["do homework", "go running"]

"""
When a task is complete it can be removed from the list
"""
my_tasks.remove("do homework") => ["go running"]

```

## 4. Implement the Behaviour

```python

from lib.task_checker import *

"""
Given several new tasks, it will create a list of tasks.
"""
def test_task_checker_add_new_tasks():
    my_tasks = Task_tracker()
    my_task.add('go running')
    my_task.add('go shopping')
    actual = my_task.tasks_list
    expected = ['go running', 'go shopping']
    assert actual == expected

"""
Given several new tasks, it will create a list of tasks.
"""
def test_task_checker_task_completed():
    my_tasks = Task_tracker()
    my_task.add('go running')
    my_task.add('go shopping')
    my_task.complete('go running')
    actual = mytask.tasks_list
    expected = ['go shopping']
    assert actual == expected

```
