'''
Explain generators with example. 
Ans:
Generators:
Generators in Python are a way to create iterators. They allow you to iterate over a sequence of items without creating the entire sequence in memory at once. This makes generators memory efficient, especially when dealing with large datasets.

Generators are defined using functions with the yield statement instead of return. When a generator function is called, it returns a generator object which can be iterated over to produce values one at a time.

Here's an example to illustrate generators:

def simple_generator():
    yield 1
    yield 2
    yield 3

# Using the generator
gen = simple_generator()

print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
# print(next(gen))  # Raises StopIteration error because the generator has no more values

# Alternatively, you can iterate over the generator using a for loop
for value in simple_generator():
    print(value)
# Output:
# 1
# 2
# 3

In this example, simple_generator() is a generator function that yields three values: 1, 2, and 3. When you call next(gen), it yields the next value in the sequence. The generator remembers its state between calls, so it resumes execution from where it left off.

Generators are particularly useful when dealing with large datasets or infinite sequences, as they allow you to generate values on-the-fly without loading everything into memory. They are commonly used with functions like range(), map(), filter(), etc., to produce iterable results without creating lists.
'''

# Generator using simple Function
def generator():
    yield 1
    yield 2
    yield 3
gen=generator()
print(next(gen))
print(next(gen))
print(next(gen))

#Generators using for loop
for value in generator():
    print("Generaotrs using for loop",value)