
#linear queue

# DECLARE names : ARRAY [0:9] OF STRING
#DECLARE head_ptr,tail_ptr : INTEGER

names=[""]*10
head_ptr=-1
tail_ptr=0

def enqueue (data):
  
  global names
  global head_ptr
  global tail_ptr


  print("enter the item u want to store",data)
  if tail_ptr == 10 :
    print("the queue is full ")
  else :
    names[tail_ptr] = data
    tail_ptr+=1

   
    if head_ptr == -1 :
      head_ptr=0




def dequeue ():
  
   
  global names
  global head_ptr
  global tail_ptr



  if head_ptr == -1 :
    print("the queue is empty")
  else:
    val=names[head_ptr]
    head_ptr-=1

  if tail_ptr == head_ptr:
    head_ptr=-1
    tail_ptr=0  



# circular queue

# DECLARE queue : ARRAY [0:9] AS STRING
# DECLARE head, tail : INTEGER

SIZE = 10
queue = [None] * SIZE
head = 0        # index of the front item (next to dequeue)
tail = 0        # index where the next item will be added
count = 0       # number of items currently in the queue


def enqueue(data):
    global queue, tail, count
    if count == SIZE:
        print("Queue is full")
        return False
    queue[tail] = data
    tail = (tail + 1) % SIZE      # wrap around to 0 after index 9
    count += 1
    return True


def dequeue():
    global queue, head, count
    if count == 0:
        print("Queue is empty")
        return None
    data = queue[head]
    queue[head] = None
    head = (head + 1) % SIZE      # wrap around
    count -= 1
    return data


def display():
    print("Queue:", queue, "| head =", head, "| tail =", tail, "| count =", count)


# Test
for name in ["A", "B", "C"]:
    enqueue(name)
display()

print("Dequeued:", dequeue())
print("Dequeued:", dequeue())
display()

# Fill it up to test wrap-around and the full check
for i in range(10):
    enqueue("X" + str(i))
display()











    

