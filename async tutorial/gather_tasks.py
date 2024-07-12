import asyncio 

async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(sleep_time) #Simulates a network request or IO operation 
    return {"id": id, "data":f"Sample data from coroutine{id}"}#return some data as a result 

async def main():
    #Run results concurrently and gather their return values 
    results = await asyncio.gather(fetch_data(1,2), fetch_data(2,1), fetch_data(3,3))
    #process the results
    for result in results:
        print(f"Recieved results: {result}")

asyncio.run(main())
