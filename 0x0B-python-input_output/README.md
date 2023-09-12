0-read_file.py - opens a file and reads it in utf-8 encoding scheme and prints the file contents to stdout
1-write_file.py - opens a file writes and overwrides if there is an existing one and encodes with utf-8 scheme
2-append_write.py - opens a file appends string encodes with utf-8 scheme and creates a file if it doesnt exist
3-to_json_string.py - converts a string in to json format
4-from_json_string.py - an object of python data structure returned as a JSON representation
5-save_to_json_file.py - writes a text file to an object using JSON representation
6-load_from_json_file.py - creates an object from a "JSON file"
7-add_item.py - Overall, this code aims to collect command-line arguments, add them to a list (or initialize a new list if the file doesn't exist), and save the list to a JSON file for future use or persistence.
8-class_to_json.py - returns a dictionary representation of an object for JSON serialization. Please note that this implementation assumes that the obj being serialized has a dict attribute that holds all the relevant data to be serialized. This approach may not work for objects that don't follow this structure.
9-student.py - it has a Public method that retrieves a dictionary representation of a Student instance _(same as 8-class_to_json.py)
10-student.py - has a public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py):
If attrs is a list of strings, only attribute names contained in this list must be retrieved.
Otherwise, all attributes must be retrieved
11-student.py - Overall, this code defines a Student class with methods to create student instances, obtain a dictionary representation of the student object, and reload the attributes from a JSON dictionary.
12-pascal_triangle.py - It uses nested lists to represent the triangle and iteratively calculates each row based on the previous row.
100-append_after.py - function that inserts a line of text to a file, after each line containing a specific string
