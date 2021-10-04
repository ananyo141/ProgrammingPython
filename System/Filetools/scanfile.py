def scanner(filename: str, function) -> None:
    return [function(line) for line in open(filename)]
