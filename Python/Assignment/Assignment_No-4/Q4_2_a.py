class StatsOperations:
    @staticmethod
    def find_average(num1, num2, num3):
        return (num1 + num2 + num3) / 3

    @staticmethod
    def find_median(num1, num2, num3):
        numbers = [num1, num2, num3]
        numbers.sort()
        return numbers[1]  