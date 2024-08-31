new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']


completed_tasks.append(new_tasks.pop())

new_tasks.remove('task_007')
new_tasks.remove('task_015')
new_tasks.insert(0,'task_015')
atten = count = len(new_tasks)

print(new_tasks)
print('Приоритет задачи: ' + new_tasks[atten - 3] + ' - поднят!')
print(completed_tasks)
