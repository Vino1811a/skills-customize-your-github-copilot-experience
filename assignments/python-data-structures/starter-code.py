"""
Starter code for Python Data Structures assignment.

This file provides the basic structure for learning and practicing Python data structures.
Complete the TODO sections to implement the required functionality.
"""

def work_with_lists_and_tuples():
    """
    Task 1: Demonstrate list and tuple operations
    """
    # TODO: Create a list of numbers
    numbers = []
    
    # TODO: Perform list operations:
    # - Add elements using append()
    # - Insert an element at a specific position
    # - Remove an element
    # - Sort the list
    # - Use list slicing to get a subset
    
    # TODO: Create a tuple with multiple values
    coordinates = ()
    
    # TODO: Unpack the tuple into variables
    # x, y = coordinates
    
    # TODO: Use list comprehension to create a new list
    # Example: create a list of squares
    
    print("List operations completed")
    pass


def work_with_dictionaries():
    """
    Task 2: Demonstrate dictionary operations
    """
    # TODO: Create a dictionary representing a student
    # Include keys like: name, age, grade, email
    student = {}
    
    # TODO: Add new key-value pairs to the dictionary
    
    # TODO: Access values using keys
    
    # TODO: Use dictionary methods:
    # - .keys() to get all keys
    # - .values() to get all values
    # - .items() to get key-value pairs
    # - .get() to safely access values
    
    # TODO: Iterate through the dictionary
    # Example: print each key-value pair
    
    # TODO: Create a frequency counter using a dictionary
    # Count occurrences of words in a sentence
    sentence = "the quick brown fox jumps over the lazy dog"
    word_count = {}
    
    print("Dictionary operations completed")
    pass


def work_with_sets():
    """
    Task 3: Demonstrate set operations and data structure selection
    """
    # TODO: Create two sets
    set1 = set()
    set2 = set()
    
    # TODO: Add elements to sets
    
    # TODO: Use set operations:
    # - Union (|) - all elements from both sets
    # - Intersection (&) - common elements
    # - Difference (-) - elements in set1 but not set2
    # - Symmetric difference (^) - elements in either but not both
    
    # TODO: Check membership in sets (membership testing)
    
    # TODO: Remove duplicates from a list using sets
    colors = ["red", "blue", "red", "green", "blue", "blue"]
    unique_colors = set()
    
    # TODO: Create a program that demonstrates choosing the right data structure
    # Example: which structure would be best for:
    # - Storing unique student IDs? (set)
    # - Storing student names and grades? (dictionary)
    # - Storing a sequence of test scores? (list)
    
    print("Set operations completed")
    pass


def data_structure_practice():
    """
    Task 3 (Part 2): Solve problems using appropriate data structures
    """
    # TODO: Problem 1: Find the most common word in a text
    # Use a dictionary to count word frequencies
    text = "python is great python is powerful python is fun"
    
    # TODO: Problem 2: Find common elements between two lists
    # Use sets for efficient comparison
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    
    # TODO: Problem 3: Store and manage student records
    # Use a combination of lists and dictionaries
    # Example: list of dictionaries, each containing student info
    
    print("Data structure practice completed")
    pass


# Main execution
if __name__ == "__main__":
    print("=== Task 1: Lists and Tuples ===")
    work_with_lists_and_tuples()
    
    print("\n=== Task 2: Dictionaries ===")
    work_with_dictionaries()
    
    print("\n=== Task 3: Sets and Data Structure Selection ===")
    work_with_sets()
    
    print("\n=== Practice Problems ===")
    data_structure_practice()
