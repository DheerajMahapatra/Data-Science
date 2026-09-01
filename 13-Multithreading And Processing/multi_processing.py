## Processes that run in parallel
## CPU-Bond Tasks-Tasks that are heavy on CPU usage (e.g., mathematical computations, data processing).
## Parallel execution- Multiple cores of the CPU

import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i*i}")
        
def cube_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Cube: {i*i*i}")


if __name__ == "__main__":
    ## create 2 processes
    p1 = multiprocessing.Process(target = square_numbers)
    p2 = multiprocessing.Process(target = cube_numbers)
    t = time.time()

    ## start the process
    p1.start()
    p2.start()

    ## Wait for the process to complete
    p1.join()
    p2.join()

    finished_time = time.time() - t
    print(finished_time)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
'''
Main Difference :-
| Feature       | Multithreading      | Multiprocessing |
| ------------- | ------------------- | --------------- |
| Memory        | Shared              | Separate        |
| Speed         | Faster creation     | Slower creation |
| Communication | Easy                | Harder          |
| CPU usage     | Limited (GIL issue) | Full CPU cores  |
| Best for      | I/O tasks           | CPU tasks       |



Python me important concept: GIL

Python me Global Interpreter Lock (GIL) hota hai.
Iska matlab:
    👉 Ek time pe sirf 1 thread Python bytecode execute kar sakta hai.

Isliye CPU-heavy tasks me multithreading fast nahi hota.

Example:
    Thread 1 -> wait
    Thread 2 -> wait

Is problem ko solve karne ke liye multiprocessing use karte hain.



Use Multithreading when:
✔ Network requests
✔ File reading/writing
✔ Web scraping
✔ Database calls
✔ API calls

Example:
    Download 10 images at same time
    
    
    
Use Multiprocessing when:
✔ Heavy calculations
✔ Machine learning
✔ Data analysis
✔ Image processing
✔ Scientific computing

Example:
    Calculate squares of 1 million numbers
    
    
    
❓ If threads can run concurrently why use processes?

Answer:
    Because Python GIL prevents true parallel CPU execution in threads, so for CPU-intensive tasks we use multiprocessing to utilize multiple CPU cores.
    
    
    
Short Memory Trick
    I/O work → Threads
    CPU work → Processes
'''
    