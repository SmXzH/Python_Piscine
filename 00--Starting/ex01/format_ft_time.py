import time

def format_date(timestamp):
    formatted_date = time.strftime("%b %d %Y", time.localtime(timestamp))
    return formatted_date

current_timestamp = time.time()

print(f"Seconds since January 1, 1970: {current_timestamp:.4f} or {current_timestamp:.2e} in scientific notation")
print(format_date(current_timestamp))
