import json

def save_text_to_json(text, filename="output.json"):
    data = {
        "content": text
    }
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

user_text = """
This is some sample text that will be saved in a JSON file.
You can use this for storing structured data, messages, or notes.
"""
save_text_to_json(user_text, "sample_output.json")
