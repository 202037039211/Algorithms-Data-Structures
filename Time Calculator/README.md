# Time Calculator

This project provides a function that adds a time duration to a given start time and calculates the resulting time. It also supports an optional day of the week and will output the resulting time with the day of the week included, as well as an indication if the result crosses over to the next day(s).

## Function: `add_time(start, duration, day=None)`
- **Parameters**:
  - `start`: The starting time in 12-hour format (e.g., `3:00 PM`).
  - `duration`: The duration to be added in hours and minutes format (e.g., `2:32`).
  - `day`: (Optional) The starting day of the week (e.g., `Monday`).
  
- **Returns**: A string with the new time, the day of the week (if provided), and the number of days later (if applicable).

## Example:

```python
print(add_time('3:00 PM', '3:10'))        # Output: "6:10 PM"
print(add_time('11:30 AM', '2:32', 'Monday'))  # Output: "2:02 PM, Monday"
print(add_time('11:43 AM', '00:20'))      # Output: "12:03 PM"
print(add_time('10:10 PM', '3:30'))       # Output: "1:40 AM"
print(add_time('11:43 PM', '24:20', 'tueSday'))  # Output: "12:03 AM, Thursday (next day)"
print(add_time('6:30 PM', '205:12'))      # Output: "11:42 AM, Thursday (9 days later)"
```

# Error Handling:
  - The function supports edge cases such as time crossing over to the next day or multiple days later.
  - The function also formats the time correctly, adding AM or PM as needed.
