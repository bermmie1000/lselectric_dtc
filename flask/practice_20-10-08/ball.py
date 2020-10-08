# 로또 번호 제조기 입니다 ㅎㅎ
# 자, 부자가 되어 봅시다.

import random


class ball:
    def __init__(self):

        number = random.randint(1, 45)
        self.number = number


if __name__ == "__main__":

    games = 5

    for game in enumerate(range(games)):

        container = []
        first_ball = ball().number
        container.append(first_ball)

        while len(container) != 6:

            next_ball = ball().number

            if next_ball not in container:
                container.append(next_ball)
            else:
                pass

        print(sorted(container))
