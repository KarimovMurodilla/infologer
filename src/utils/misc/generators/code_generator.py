import random


class Generator:
    def _generate(self) -> list[str]:
        nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        random.shuffle(nums)

        return nums

    def generate_user_id(self):
        nums = self._generate()

        result = int("".join(nums)[:7])
        return result

    def generate_code(self) -> int:
        nums = self._generate()

        result = int("".join(nums)[:4])
        return result
