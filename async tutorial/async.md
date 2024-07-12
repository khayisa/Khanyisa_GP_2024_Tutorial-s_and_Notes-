# ASYNC TUTORIAL 
The essence of asynchronus programming is making our code more efficient by doing multiple things at once without the unecessary waiting 
#### when should we use Asyncio ?
1. ASYNCIO - for managing many waiting tasks 
1. Threads - for maximizing performance on intensive cpu tasks 
1. Processes - for parallel tasks that share data with minimal cpu use 

#### Five Key concepts we need to understand 

# 1. The Event Loop 
- In pythons asyncio the event loop is the core that manages and distributes tasks
- central hub with tasks circling around waiting to be executed
- each tasks takes its turn in the center 

# 2. Coroutine
###### Creating an enventloop and coroutine
- what is a coroutine function?
    - these functions are defined using `async def` syntax they can `await` expression to pause their execution until awaited result is ready allowing other tasks to run in the meantime 

    ```python
    async def fetch_data(delay):
    print("Fetching data...")
    await asyncio.sleep(delay) #simulates an I/O operation with a sleep
    print("Data fetched")
    return {"data":"Some data"} # return some data 

    ```
    The function `fetch_data` is an asynchronous coroutine function aimed at simulating some input output bound operation e.g going to the network to retrieve some data or reading data etc. something that is controlled by our program that would have to wait for  

Here is a step-by-step explanation of what the function does:

1. **Function Definition**: 
   - The function `fetch_data` is defined as an asynchronous coroutine using `async def`.

2. **Parameters**:
   - `delay`: This parameter specifies the number of seconds the function should "sleep" to simulate the time taken by an I/O operation.

3. **Execution Steps**:
   - `print("Fetching data...")`: This prints "Fetching data..." to the console, indicating that the data fetching process has started.
   
   - `await asyncio.sleep(delay)`: The `await` keyword pauses the execution of `fetch_data` for `delay` seconds. During this time, other tasks can run because the event loop is not blocked. This line simulates an I/O operation, like waiting for a response from a server or reading from a disk.
   
   - `print("Data fetched")`: After the `delay` period is over, this prints "Data fetched" to the console, indicating that the simulated data fetching process is complete.
   
   - `return {"data": "Some data"}`: Finally, the function returns a dictionary containing some dummy data (`{"data": "Some data"}`).
 
 another coroutine example 
 Sure! Here is an explanation of the provided code in markdown format:

---

### Code Explanation: Asynchronous Data Fetching

The following code demonstrates the use of asynchronous functions in Python to fetch data concurrently with the `asyncio` library.

```python
import asyncio

async def fetch_data(delay, id):
    print("Fetching data...id", id)
    await asyncio.sleep(delay)  # Simulates an I/O operation with a sleep
    print("Data fetched, id:", id)
    return {"data": "Some data", "id": id}  # Return some data

```

### Function: `fetch_data`

The `fetch_data` function is an asynchronous coroutine designed to simulate fetching data with a specified delay and identifier.

#### Parameters:
- `delay`: The number of seconds to wait, simulating the time taken by an I/O operation.
- `id`: An identifier for the data fetch operation.

#### Steps:
1. `print("Fetching data...id", id)`: Prints a message indicating the start of the data fetch operation along with the `id`.
2. `await asyncio.sleep(delay)`: Pauses execution for `delay` seconds to simulate an I/O operation without blocking the event loop.
3. `print("Data fetched, id:", id)`: Prints a message indicating the completion of the data fetch operation along with the `id`.
4. `return {"data": "Some data", "id": id}`: Returns a dictionary containing some dummy data and the `id`.

### Function: `main`
```python
async def main():
    task1 = fetch_data(2, 1)
    task2 = fetch_data(2, 2)

    result1 = await task1
    print(f"Received result: {result1}")

    result2 = await task2
    print(f"Received result: {result2}")
```

The `main` function is an asynchronous coroutine that coordinates the data fetching tasks.

#### Steps:
1. `task1 = fetch_data(2, 1)`: Initiates the `fetch_data` coroutine with a 2-second delay and `id` 1.
2. `task2 = fetch_data(2, 2)`: Initiates the `fetch_data` coroutine with a 2-second delay and `id` 2.
3. `result1 = await task1`: Awaits the completion of `task1` and stores the result.
4. `print(f"Received result: {result1}")`: Prints the result of `task1`.
5. `result2 = await task2`: Awaits the completion of `task2` and stores the result.
6. `print(f"Received result: {result2}")`: Prints the result of `task2`.

### Execution

To run the asynchronous `main` coroutine, the `asyncio.run(main())` function is used. This sets up and runs the event loop, executing `main` and handling the asynchronous tasks.


# 3. Task 
A task is a way to schedule a core routine as soon as possible and to allow us to run ultiple coroutines simultaneously 

```python

import asyncio 

async def fetch_data(id,sleep_time):
    print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(sleep_time)
    return {"id": id, "data" : f"Sample data from coroutine {id}"}

async def main():
    #create tasks for runningcoroutines concurrently
    task1 = asyncio.create_task(fetch_data(1,2))
    task2 = asyncio.create_task(fetch_data(2,3))
    task3 = asyncio.create_task(fetch_data(3,1))

    result1=await task1
    result2=await task2
    result3=await task3

    print(result1,result2,result3)

asyncio.run(main())
```   
### Function: `fetch_data`
#### Parameters:
- `id`: An identifier for the coroutine.
- `sleep_time`: The number of seconds to sleep, simulating the time taken to fetch data.

#### Steps:
1. `print(f"Coroutine {id} starting to fetch data.")`: Prints a message indicating that the coroutine has started fetching data.
2. `await asyncio.sleep(sleep_time)`: Pauses execution for `sleep_time` seconds without blocking the event loop.
3. `return {"id": id, "data": f"Sample data from coroutine {id}"}`: Returns a dictionary containing the coroutine's `id` and some sample data.

### Function: `main`

The `main` function is an asynchronous coroutine that manages the concurrent execution of multiple `fetch_data` coroutines by creating tasks.

#### Steps:
1. `task1 = asyncio.create_task(fetch_data(1, 2))`: Creates a task to run `fetch_data` with `id` 1 and a 2-second delay. This task will run concurrently with other tasks.
2. `task2 = asyncio.create_task(fetch_data(2, 3))`: Creates a task to run `fetch_data` with `id` 2 and a 3-second delay. This task will also run concurrently with other tasks.
3. `task3 = asyncio.create_task(fetch_data(3, 1))`: Creates a task to run `fetch_data` with `id` 3 and a 1-second delay. This task will run concurrently with the others.
4. `result1 = await task1`: Awaits the completion of `task1` and stores the result.
5. `result2 = await task2`: Awaits the completion of `task2` and stores the result.
6. `result3 = await task3`: Awaits the completion of `task3` and stores the result.
7. `print(result1, result2, result3)`: Prints the results of all three tasks.

 
## Gather function 
The gather function is a quick way to concurrently run multiple coroutines 
- the gather function is not that great at error handling and it will not automatically cancel other other coroutines if an error occours in one co-routine 
```python 
async def main():
    #Run results concurrently and gather their return values 
    results = await asyncio.gather(fetch_data(1,2), fetch_data(2,1), fetch_data(3,3))
    #process the results
    for result in results:
        print(f"Recieved results: {result}")
```
## Task group function 
The task group function is the slightly more preffered way to create multiple tasks and organise them together as it provides some built in error handling 

`async with` is known as asynchronus context manager with gives us access to the `tg` variable

```python
import asyncio

async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(sleep_time)  # Simulates a network request or IO operation
    return {"id": id, "data": f"Sample data from coroutine {id}"}

async def main():
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for i, sleep_time in enumerate([2, 1, 3], start=1):
            task = tg.create_task(fetch_data(i, sleep_time))
            tasks.append(task)

    results = [task.result() for task in tasks]

    for result in results:
        print(f"Received result: {result}")

# Run the main coroutine
asyncio.run(main())
```

### Function: `main`

The `main` function is an asynchronous coroutine that manages the concurrent execution of multiple `fetch_data` coroutines by using an `asyncio.TaskGroup`.

#### Steps:
1. `tasks = []`: Initializes an empty list to store the task objects.
2. `async with asyncio.TaskGroup() as tg:`: Creates a `TaskGroup` context, which manages a group of tasks that can run concurrently.
3. `for i, sleep_time in enumerate([2, 1, 3], start=1):`: Iterates over a list of sleep times and their corresponding indices, starting at 1.
   - `task = tg.create_task(fetch_data(i, sleep_time))`: Creates a new task for each coroutine using the `create_task` method of the `TaskGroup`. This schedules the `fetch_data` coroutine to run concurrently.
   - `tasks.append(task)`: Adds the created task to the `tasks` list.
4. `results = [task.result() for task in tasks]`: After the `TaskGroup` completes, retrieves the results of each task.
5. `for result in results:`: Iterates over the collected results.
6. `print(f"Received result: {result}")`: Prints each result to the console.

 
 
 

# 4.Future 
A promise of a future result 

```python

import asyncio

async def set_future_result(future,value):
    await asyncio.sleep(2)
    # set the result of the future 
    future.set_result(value)
    print (f"Set the future result to: {value}")

async def main():
    #Create a future object 
    loop = asyncio.get_running_loop()
    future = loop.create_future()

    #Schedule setting the future's result 
    asyncio.create_task(set_future_result(future, "Future result is ready"))

    #wait for the future results 
    result = await future
    print(f"Recieved the future's result: {result}")

asyncio.run(main())

```


# 5.Syncronization
Tools that allow us to synchronize the excution of various couroutines 

#### Lock 
```python
import asyncio

# a Shared varialble 
shared_resource = 0 

# an Asyncio lock
lock = asyncio.Lock() #creating the lock

async def modify_shared_resource():
    global shared_resource
    async with lock: #checks if any other coroutine is using the lock , if the is it waits , if not enters critical section
        #critical section starts 
        print(f"Resource before modification: {shared_resource}")
        shared_resource += 1   #modified the shared resource
        await asyncio.sleep(1) #Simulate an IO operation
        print(f"Resource after modification: {shared_resource}")
        # Critical section ends
        # the idea is the critical section must complete before the lock is released to another task 

async def main():
    await asyncio.gather(*(modify_shared_resource() for _ in range(5))) # five different instances of the coroutine are created 

asyncio.run(main())
```
#### Semaphore 
Allows multiple corountines to have access to the same object at the same time 

```python
import asyncio

async def access_resources(semaphore, resource_id):
    async with semaphore:
        #Simulate accessing a limited resource
        print(f"Accessing resource{resource_id}")
        await asyncio.sleep(1)# simulate work with resources
        print(f"Releasing resource {resource_id}")

async def main():
    semaphore = asyncio.Semaphore(2) #Allow 2 concurrent accesses
    await asyncio.gather(*(access_resources(semaphore, i) for i in range(5)))

    asyncio.run(main())
```
#### Event
allows us to do some simpler synchronization 

```python
import asyncio

async def waiter(event):
    print("waiting for the event to be set")
    await event.wait()
    print("event haa been set, continuing execution")

async def setter(event):
    await asyncio.sleep(2) #Simulate doing some work
    event.set()
    print("event has been set!")

async def main(): 
    event = asyncio.Event()
    await asyncio.gather(waiter(event), setter(event))

asyncio.run(main())
```