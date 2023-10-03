"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-03 15:06:25
@Description: 
"""
# contrasts duck typing and nominal typing, as well
# as static type checking and runtime behavior.


class Bird:
    pass


class Duck(Bird):
    def quack(self):
        print("Quack")


def alert(birdie):
    """alert has no type hints, so the type checker ignores it."""
    birdie.quack()


def alert_duck(birdie: Duck) -> None:
    """takes one argument of type Duck."""
    birdie.quack()


def alert_bird(birdie: Bird) -> None:
    """takes one argument of type Bird."""
    birdie.quack()
