### Multiprocessing With Process Pool Executor

from concurrent.futures import ProcessPoolExecutor
import time

def square_number(number):
    time.sleep(1)
    return f"Square: {number*number}"

numbers = [1,2,3,4,5]

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square_number, numbers)
        t = time.time()
        
    for result in results:
        print(result)
        
    finished_time = time.time() - t
    print(finished_time)