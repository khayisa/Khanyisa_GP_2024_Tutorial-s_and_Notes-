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