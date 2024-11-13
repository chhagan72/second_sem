try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"General Error: {e}")
else:
    print("No exception occurred.")
finally:
    print("Finally block executed.")


