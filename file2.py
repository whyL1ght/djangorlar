import random
import time

class Weather:
    def __init__(self, city):
        self.city = city
        self.temperature = 20.0
        self.humidity = 50
        self.condition = "Sunny"

    def update(self):
        self.temperature += random.uniform(-3, 3)
        self.humidity = max(0, min(100, self.humidity + random.randint(-5, 5)))
        self.condition = random.choice(["Sunny", "Cloudy", "Rainy", "Stormy", "Windy", "Foggy"])

    def __str__(self):
        return f"{self.city}: {self.condition}, {self.temperature:.1f}°C, {self.humidity}% humidity"

class WeatherSimulator:
    def __init__(self):
        self.cities = [
            Weather("New York"),
            Weather("London"),
            Weather("Tokyo"),
            Weather("Berlin"),
            Weather("Moscow"),
            Weather("Ust-Kamenogorsk"),
        ]
        self.time_step = 0

    def step(self):
        print(f"\n--- Simulation step {self.time_step} ---")
        for city in self.cities:
            city.update()
            print(city)
        self.time_step += 1

    def run(self, steps=5, delay=1.0):
        for _ in range(steps):
            self.step()
            time.sleep(delay)

if __name__ == "__main__":
    sim = WeatherSimulator()
    sim.run(steps=10, delay=0.5)
