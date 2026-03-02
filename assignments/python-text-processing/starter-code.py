"""
Starter code for Python Text Processing assignment.

This file provides the basic structure for building a text processing application.
Complete the TODO sections to implement the required functionality.
"""

def manipulate_strings():
    """
    Task 1: Demonstrate string manipulation techniques
    """
    # TODO: Create a string variable with sample text
    text = ""
    
    # TODO: Use string methods to:
    # - Convert text to uppercase and lowercase
    # - Split text into words
    # - Count occurrences of a specific word
    # - Replace a word with another word
    
    pass


def read_and_process_file(filename):
    """
    Task 2: Read a file and process its contents
    
    Args:
        filename (str): The path to the file to read
    
    Returns:
        list: Processed lines from the file
    """
    processed_lines = []
    
    try:
        # TODO: Open the file in read mode
        # TODO: Read all lines from the file
        # TODO: Process each line (strip whitespace, convert to uppercase, etc.)
        # TODO: Store processed lines in the list
        # TODO: Close the file (or use context manager)
        pass
    except FileNotFoundError:
        # TODO: Handle the case when file doesn't exist
        print(f"Error: File '{filename}' not found.")
        return []
    
    return processed_lines


def analyze_text(filename):
    """
    Task 3: Analyze text file and write results to output file
    
    Args:
        filename (str): The path to the input file
    
    Returns:
        str: The name of the output file created
    """
    
    # TODO: Read the file and calculate:
    # - Total number of lines
    # - Total number of words
    # - Total number of characters
    # - List of unique words
    # - Word frequency (how many times each word appears)
    
    # TODO: Open an output file for writing
    # TODO: Write a formatted report including:
    # - File analysis header
    # - Summary statistics (lines, words, characters)
    # - Top 10 most frequent words
    # - Any other interesting analysis
    
    # TODO: Return the output filename
    output_filename = "analysis_report.txt"
    return output_filename


# Main execution
if __name__ == "__main__":
    # Test Task 1
    print("=== Task 1: String Manipulation ===")
    manipulate_strings()
    
    # Test Task 2 - create a sample file or use existing one
    print("\n=== Task 2: File Reading ===")
    lines = read_and_process_file("sample.txt")
    print(f"Processed {len(lines)} lines")
    
    # Test Task 3
    print("\n=== Task 3: Text Analysis ===")
    output_file = analyze_text("sample.txt")
    print(f"Analysis results written to {output_file}")
