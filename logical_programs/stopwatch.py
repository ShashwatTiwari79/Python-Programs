import time
input("press enter to start the stopwatch ")
start = time.time()
input("press enter to stop the stopwatch ")
end = time.time()
total_time = end-start
print(f"total elapsed time = {total_time:.3f} seconds")
