# Consider adding a module-level docstring to explain the purpose of this script and its functionality.
import json

# You could add a type hint for the 'text' and 'filename' parameters to improve code readability and maintainability.
def save_text_to_json(text, filename="output.json"):
    # Consider validating the 'text' parameter to ensure it is a string before proceeding, to avoid potential runtime errors.
    data = {
        # You might want to add a docstring to this function to describe its purpose, parameters, and return value.
        "content": text
    }
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
# It might be helpful to handle potential exceptions (e.g., IOError) when opening or writing to the file, to make the function more robust.

user_text = """
This is some sample text that will be saved in a JSON file.
You can use this for storing structured data, messages, or notes.
# Consider making the sample text a constant (e.g., SAMPLE_TEXT) at the module level for better readability and reusability.
"""
save_text_to_json(user_text, "sample_output.json")
