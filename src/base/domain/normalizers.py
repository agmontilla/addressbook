def to_capitalize(string: str) -> str:
    return " ".join(word.capitalize() for word in string.split(" "))
