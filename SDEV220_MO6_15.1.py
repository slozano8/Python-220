import multiprocessing
import random
import time

def process_function():
  """Function executed by each process."""
  sleep_time = random.uniform(0, 1)  # Random sleep between 0 and 1 seconds
  time.sleep(sleep_time)
  print(f"Current time in process: {time.ctime()}")

if __name__ == "__main__":
  processes = [multiprocessing.Process(target=process_function) for _ in range(3)]
  for process in processes:
    process.start()

  for process in processes:
    process.join()

  print("The processes finished properly!")

