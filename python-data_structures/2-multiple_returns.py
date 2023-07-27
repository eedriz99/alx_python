def multiple_returns(sentence):
    first_character = sentence[0]
    length = len(sentence)

    if length > 0:
        return (length, first_character)
    else:
        return (length, None)