from typing import Dict

# Import the GroqProvider from PocketGroq
from pocketgroq import GroqProvider

# Initialize the GroqProvider
groq = GroqProvider()

def print_pyramid(levels: int) -> Dict[str, str]:
    """ Generate a pyramid with the given number of levels. """
    pyramid = "\n".join(" " * (levels - i - 1) + "*" * (2 * i + 1) for i in range(levels))
    return {"pyramid": pyramid}

# Define the tool for PocketGroq
tools = [
    {
        "type": "function",
        "function": {
            "name": "print_pyramid",
            "description": "Generate a pyramid pattern of a given number of levels.",
            "parameters": {
                "type": "object",
                "properties": {
                    "levels": {
                        "type": "integer",
                        "description": "The number of levels in the pyramid.",
                    }
                },
                "required": ["levels"],
            },
            "implementation": print_pyramid
        }
    }
]

# Use the tool to generate a pyramid with 5 levels
response = groq.generate("Please create a pyramid with 5 levels", tools=tools)
print("Response:", response)
