from celery.schedules import crontab


CELERY_IMPORTS = ('app.tasks.test')
CELERY_TASK_RESULT_EXPIRES = 30
CELERY_TIMEZONE = 'UTC'

CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

'''
This is for scheduling the task periodically
'''
'''
CELERYBEAT_SCHEDULE = {
    'for_task_A': {
        'task': 'app.tasks.test.print_numbers',
		'args': (10,),
        # Every minute
        #'schedule': crontab(minute='*'),
    },
	'for_task_B': {
		'task': 'app.tasks.test.print_hello',
		#'schedule': crontab(minute='*'),
	}
}
'''
'''
This is for routing the tasks into Queue
I have defined the Queue, otherwise it takes the
default queue
Worker will be listening to these queues
I have used redis PUB/SUB for messaging queues
'''
CELERY_ROUTES = {
    'app.tasks.test.print_numbers': {'queue': 'for_task_A', 'routing_key': 'for_task_A'},
    'app.tasks.test.print_hello': {'queue': 'for_task_A', 'routing_key': 'for_task_A'},
	'app.tasks.test.divide_chunks':{'queue':'for_task_A', 'routing_ke':'for_task_A'},
}
