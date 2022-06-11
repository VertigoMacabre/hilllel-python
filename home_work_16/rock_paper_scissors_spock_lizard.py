import random
from enum import IntEnum
from strenum import StrEnum


class GameActions(IntEnum):
    Rock = 1
    Scissors = 2
    Paper = 3
    Lizard = 4
    Spock = 5

    def __str__(self):
        return self.name


class Results(StrEnum):
    Win = 'You win!'
    Lose = "You lose"
    Tie = "Tie, try again"


class RepeatRequest(IntEnum):
    Yes = 1
    No = 2


class GameResult:
    result: Results
    user_choice: GameActions
    machine_choice: GameActions


combinations: dict = {
    GameActions.Rock: [GameActions.Lizard, GameActions.Scissors],
    GameActions.Scissors: [GameActions.Paper, GameActions.Lizard],
    GameActions.Paper: [GameActions.Rock, GameActions.Spock],
    GameActions.Lizard: [GameActions.Spock, GameActions.Paper],
    GameActions.Spock: [GameActions.Rock, GameActions.Scissors],
}


def rock_paper_scissors_spock_lizard(action: GameActions) -> GameResult:
    game_result: GameResult = GameResult()
    machine_choice: GameActions = GameActions(random.randint(1, len(combinations) - 1))
    game_result.user_choice = action
    game_result.machine_choice = machine_choice

    if users_choice == machine_choice:
        game_result.result = Results.Tie

    elif machine_choice in combinations[users_choice]:
        game_result.result = Results.Win

    else:
        game_result.result = Results.Lose

    return game_result


if __name__ == '__main__':

    gr: GameResult

    while True:
        try:
            users_input: int = int(input("1.Rock\n2.Scissors\n3.Paper\n4.Lizard\n5.Spock\n"))
            users_choice: GameActions = GameActions(users_input)
            gr = rock_paper_scissors_spock_lizard(users_choice)
            print(
                f"{gr.result}, your choice was {GameActions(gr.user_choice)} and machine choice was {GameActions(gr.machine_choice)}",
                end="\n")

            try:
                repeat_input = int(input("Repeat?\n1.Yes.\n2.No.\n"))
                request = RepeatRequest(repeat_input)

                if RepeatRequest.No == request:
                    break

            except ValueError:
                print(f"Choice should be a number in range from 1 to {len(RepeatRequest)}")
        except ValueError:
            print(f"Choice should be a number in range from 1 to {len(GameActions)}")
