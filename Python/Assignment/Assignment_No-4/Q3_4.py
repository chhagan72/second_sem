# Example: Retrieve file properties
import os

file_path = "example.txt"
file_properties = os.stat(file_path)
print(f"File properties for {file_path}:\n{file_properties}")
