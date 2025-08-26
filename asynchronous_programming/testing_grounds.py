import asyncio
import time


async def request_api(n):
    print(f"Requesting {n} from API...")
    await asyncio.sleep(n)
    print(f"Done requesting {n} from API...")
    result = f"Result of {n} request."
    return result


async def main_simple():
    task1 = asyncio.create_task(request_api(3))
    task2 = asyncio.create_task(request_api(5))

    task1_result = await task1
    task2_result = await task2

    print("Main function is done")
    return [task1_result, task1_result]


async def main_gather():
    # Schedules requests to the loop manager.
    task_list = asyncio.gather(request_api(3), request_api(5), request_api(7))

    # Sets task_results to the list of results of the awaited requests.
    task_results = await task_list

    print("Main function is done")
    return task_results


start = time.perf_counter()
api_requests = asyncio.run(main_simple())
end = time.perf_counter()
print(api_requests, f"It took {end-start} seconds.\n\n")

start = time.perf_counter()
api_requests = asyncio.run(main_gather())
end = time.perf_counter()
print(api_requests, f"It took {end-start} seconds.")
