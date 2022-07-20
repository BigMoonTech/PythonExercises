import random
import copy


class Hat:

    def __init__(self, **kwargs):
        self.contents = [k for k, v in kwargs.items() for _ in range(v)]

    def draw(self, num_of_balls):

        if num_of_balls > len(self.contents):
            return self.contents

        else:
            draw = []

            for i in range(num_of_balls):
                popped = self.contents.pop(random.randint(0, len(self.contents)-1))
                draw.append(popped)

            return draw


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    successes = 0

    # turn dictionary argument into list of strings, ie. {'r': 1, 'g': 2} --> ['r', 'g', 'g']
    # expected_balls_lst = [k for k, v in expected_balls.items() for _ in range(v)]

    # save original argument value so it doesn't get modified
    draws = int(num_experiments)

    while num_experiments > 0:

        draw_dict = {}
        check_lst = []
        original_hat = copy.deepcopy(hat)
        draw = original_hat.draw(num_balls_drawn)

        for i in draw:
            draw_dict[i] = draw.count(i)

        for k, v in expected_balls.items():
            print(v, k)
            try:
                if draw_dict[k] >= v:
                    check_lst.append(True)
                else:
                    check_lst.append(False)
            except KeyError:
                check_lst.append(False)

        if all(check_lst):
            successes += 1

        # de-increment num_experiments by 1 so loop will run equal to draws
        num_experiments -= 1

    return successes/draws


new_hat = Hat(blue=3, red=2, green=6)
print(experiment(new_hat, {'blue': 2, 'green': 1}, 4, 1000))
