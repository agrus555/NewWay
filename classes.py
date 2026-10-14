kinds = ("elf, ork")

class character:
    def __init__(self, name: str, kind: str) -> None:
        self.name = name
        self.kind = kind
        if self.kind not in kinds:
            raise TypeError("Invalid kind")

    def __str__(self):
        return f"Name: {self.name}, Kind: {self.kind}"

character1 = character("Elf_1", "elf")
print(character1)