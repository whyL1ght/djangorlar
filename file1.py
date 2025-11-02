import math
import datetime

class Calculator4:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self._save("add", a, b, result)
        return result

    def subtract(self, a, b):
        result = a - b
        self._save("subtract", a, b, result)
        return result

    def multiply(self, a, b):
        result = a * b
        self._save("multiply", a, b, result)
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero!")
        result = a / b
        self._save("divide", a, b, result)
        return result

    def power(self, a, b):
        result = math.pow(a, b)
        self._save("power", a, b, result)
        return result

    def sqrt(self, a):
        result = math.sqrt(a)
        self._save("sqrt", a, None, result)
        return result

    def _save(self, operation, a, b, result):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = {"time": timestamp, "operation": operation, "a": a, "b": b, "result": result}
        self.history.append(entry)

    def show_history(self):
        for entry in self.history:
            print(f"[{entry['time']}] {entry['operation']}({entry['a']}, {entry['b']}) = {entry['result']}")

def main():
    calc = Calculator4()
    while True:
        print("\nAvailable operations: add, subtract, multiply, divide, power, sqrt, history, quit")
        cmd = input("Enter operation: ").strip().lower()
        if cmd == "quit":
            print("Goodbye!")
            break
        elif cmd == "history":
            calc.show_history()
        elif cmd == "sqrt":
            a = float(input("Enter a number: "))
            print("Result:", calc.sqrt(a))
        elif cmd in ("add", "subtract", "multiply", "divide", "power"):
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            func = getattr(calc, cmd)
            print("Your Result:", func(a, b))
        else:
            print("Unknown command!")

if __name__ == "__main__":
    main()
