from typing import Optional


class Wizard:

    def __init__(self):
        self.name: Optional[str] = None
        self.level: int = 0

    @staticmethod
    def train(base_level: int) -> "Wizard":
        w = Wizard()
        w.level = base_level

        return w

def main():
    gandolf: Wizard = Wizard.train(100)
    gandolf.level += 1
    gandolf.name = "Gandolf"
    print(f"The Wizard level is {gandolf.level}")

if __name__ == '__main__':
    main()