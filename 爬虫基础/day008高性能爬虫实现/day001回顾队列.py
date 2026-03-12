import queue
q=queue.Queue()
a="1"
print(q.put(a))
print(q.get())
q.task_done()
#获取数量
print(q.qsize())
q.join()#判断计数机是否为0