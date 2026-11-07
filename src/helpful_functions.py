""" I'm going to write some basic Python functions that should definitely be imported instead."""
import warnings

def split_vocab(text: str, delimiter: str = " ") -> list[str]:
    """Own function used in place of re.split. Behaviour won't match in all cases
    
    Args:
        text (str): The text to split. 
        delimiter (str): The delimiter on which to split text. Default to whitespace.

    Returns:
        vocab (list[str]): The full list of vocabulary used within text.

    Raises:
        ValueError: If the input text is empty. 

    Warns:
        UserWarning: If the delimiter is not present in the text.
    """
    if not text:
        raise ValueError("Input text must not be empty.")

    if delimiter not in text:
        warnings.warn("Delimiter not found in input text.", UserWarning)

    