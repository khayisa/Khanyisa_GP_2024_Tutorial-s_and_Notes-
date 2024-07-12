import asyncio


# Define a coroutine tht simulates a time consuming task 

async def fetch_data(delay):
    print("Fetching data...")
    await asyncio.sleep(delay) #simulates an I/O operation with a sleep
    print("Data fetched")
    return {"data":"Some data"} # return some data 

#defining a coroutine functionthat calls the first coroutine function 

async def main(): 
    print("Start of main coroutine")
    task = fetch_data(2)
    #await the fetch_data coroutine, pausing execution of main until fetch_data completes 
    results = await task
    print(f"Recieved result: {results}")
    print("End of main coroutine") 



#run the main coroutine (or call the function )
asyncio.run(main())
