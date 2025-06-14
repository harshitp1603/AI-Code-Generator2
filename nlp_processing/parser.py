import spacy
import re

nlp = spacy.load("en_core_web_sm")

def extract_info(sentence):
    doc = nlp(sentence.lower())

    # Map keywords to standard operation names
    operations_map = {
        "add": ["add", "plus", "sum"],
        "subtract": ["subtract", "minus", "difference"],
        "multiply": ["multiply", "times", "product"],
        "divide": ["divide", "divided", "quotient"],
        "modulus": ["mod", "modulus", "remainder"],
        "power": ["power", "raised to", "exponent"],
        "sqrt": ["sqrt", "square root"],
        "factorial": ["factorial", "fact"],
        "gcd": ["gcd", "greatest common divisor"],
        "lcm": ["lcm", "least common multiple"],
        "palindrome": ["palindrome", "is palindrome", "check palindrome"],
        "odd_even": ["odd", "even", "odd or even", "check if odd", "check if even"],
        "armstrong": ["armstrong", "is armstrong", "check armstrong"]
    }

    operation = None
    variables = []

    # Match operation
    for token in doc:
        word = token.text.lower()
        for key, synonyms in operations_map.items():
            if word in synonyms:
                operation = key
                break
        if operation:
            break

    # Clean phrasing like "What is", "Calculate", etc.
    sentence = re.sub(r"(what is|calculate|how much is|find|compute)\s+", "", sentence, flags=re.I)

    # Extract numbers or simple variable names
    for token in doc:
        if token.pos_ in ["NUM", "NOUN", "SYM", "PROPN"]:
            if token.text.lower() not in operations_map.get(operation, []):
                variables.append(token.text)

    return {"operation": operation, "variables": variables}


# Example Usage
if __name__ == "__main__":
    print(extract_info("Multiply 4 by 6"))  # Expected: {'operation': 'multiply', 'variables': ['4', '6']}
    print(extract_info("Divide 100 by 4"))  # Expected: {'operation': 'divide', 'variables': ['100', '4']}
