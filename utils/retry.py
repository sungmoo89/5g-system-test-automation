import time

def retry(func, retries=3, delay=2):

    for attempt in range(retries):
        result = func()

        if result:
            return True

        print(f"Retry {attempt+1}/{retries}")
        time.sleep(delay)

    return False
