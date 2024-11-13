# 6] Write a Python program to make a chain of function decorators (bold, italic, underline etc.)
# in Python. 
def bold_decorator(func):
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def italic_decorator(func):
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper

def underline_decorator(func):
    def wrapper(*args, **kwargs):
        return f"<u>{func(*args, **kwargs)}</u>"
    return wrapper

@bold_decorator
@italic_decorator
@underline_decorator
def formatted_text(text):
    return text

# Example usage
text = "Hello, World!"
formatted_result = formatted_text(text)
print("Formatted Text:", formatted_result)
