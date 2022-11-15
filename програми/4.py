class Name:
    def __init__(self, name) -> None:
        if name not in ["Богдан", "Данило"]:
            raise ValueError("Дозволені імена: Богдан, Данило")
        self.name = name

a = Name("Ладик")