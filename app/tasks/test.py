import celery
import time

@celery.task()
def print_numbers(n):
	print 'chunks size is', n
	for i in range(n):
		print i
	time.sleep(10)

@celery.task()
def print_hello():
    print 'Hello'

'''
This method divides the input param into chunks
and then it calls the print_numbers task to 
execute in parallel asynchronously
'''
@celery.task()
def divide_chunks(n):
	items = zip(xrange(n))
	print_numbers.chunks(iter(items), 10).group().apply_async(queue='for_task_A')
