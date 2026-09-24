"""Reverse a string by iterating backward through its characters."""


def reverse_string(text: str) -> str:
    """Return the characters of text in reverse order."""
    reversed_text = ""

    # The Java version does: for (int i = text.length() - 1; i >= 0; i--) {
    #     reversed += text.charAt(i);
    # }
    # Python matches that behavior by walking indices from the end to the start.
    for i in range(len(text) - 1, -1, -1):
        reversed_text += text[i]

    return reversed_text


if __name__ == "__main__":
    text = "hello"
    print(f"Input: {text}")
    print(f"Output: {reverse_string(text)}")
