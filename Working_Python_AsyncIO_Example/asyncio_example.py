import asyncio


# coroutine 1
async def slow_func():
    print("slow func begins")
    await asyncio.sleep(3)
    print("slow func ends")


# coroutine 2
async def slower_func():
    print("slower func begins")
    await asyncio.sleep(5)
    print("slower func ends")


# main async function
async def main():
    # show when main async function begins
    print("main begins")
    
    # create tasks of different speeds. Order of creation doesn't matter
    task1 = asyncio.create_task(slow_func())
    task2 = asyncio.create_task(slower_func())
    
    # await for the completion of each task. does not block a subsequent await
    await task2
    await task1

    # show when the main async function ends. 
    print("main ends")  


asyncio.run(main())
