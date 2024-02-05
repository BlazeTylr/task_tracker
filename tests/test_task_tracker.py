from lib.task_tracker import *

def test_task_checker_add_new_tasks():
    my_tasks = Task_tracker()
    my_tasks.add('go running')
    my_tasks.add('go shopping')
    actual = my_tasks.tasks_list
    expected = ['go running', 'go shopping']
    assert actual == expected

def test_task_checker_task_completed():
    my_tasks = Task_tracker()
    my_tasks.add('go running')
    my_tasks.add('go shopping')
    my_tasks.complete('go running')
    actual = my_tasks.tasks_list
    expected = ['go shopping']
    assert actual == expected