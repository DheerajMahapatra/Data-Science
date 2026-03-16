### Multithreading With Thread Pool Executor

from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    return f"Number: {number}"

number = [1,2,3,4,5,6,7,8,9,0,1,2,3]

# t = time.perf_counter()
'''Bhai perf_counter() high-precision timer hota hai jo Python me execution time accurately measure karne ke liye use hota hai. ⏱️Ye normal time.time() se zyada accurate hota hai.'''

t = time.time()

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_number, number)
    
for result in results:
    print(result)

    
finished_time = time.time() - t
print(finished_time)