def parenthesis_generator(n: int) -> list[str]:
    if not n:
        return ['']

    answer: list[str] = []
    for closure in range(n):
        for left in parenthesis_generator(closure):
            for right in parenthesis_generator(n - 1 - closure):
                answer.append(f'({left}){right}')
    return answer
