def multiple_returns(sentence):
    length = len(sentence)

    if length > 0:
        first_character = sentence[0]
        return (length, first_character)
    else:
        return (length, None)