from datetime import datetime


# Decorator function used to log activity details
def log_activity(func):
 # Wrapper function receives all positional and keyword arguments
    def wrapper(*args, **kwargs):
        print("===================================")
        # Displays the name of the function being executed
        print(f"Function: {func.__name__}")
        print(f"Time: {datetime.now()}")
        print("Activity started...")

        result = func(*args, **kwargs)

        print("Activity completed.")
        print("===================================\n")

        return result

    return wrapper
