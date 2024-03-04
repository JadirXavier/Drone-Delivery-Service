class Drone:
    def __init__(self, name, max_weight):
        self.name = name
        self.max_weight = max_weight
        self.deliveries = []
    def __str__(self):
        return f"Drone(name={self.name}, max_weight={self.max_weight}, deliveries={self.deliveries})"

class Location:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    def __str__(self):
        return f"Location(name={self.name}, weight={self.weight})"

def main():
    drones, locations = read_data()
    make_deliveries(drones, locations)

def read_data():
    try:
        with open("input.txt", "r") as file:
            lines = file.readlines()
            drones = []
            locations = []
            drones_line = lines[0].strip().replace('[', '').replace(']', '').split(",")

            for line in lines[1:]:
                location_line = line.replace('[', '').replace(']', '').split(",")
                name = location_line[0].strip()
                weight = int(location_line[1].strip())
                locations.append(Location(name, weight))

            for i in range(0, len(drones_line), 2):
                name = drones_line[i].strip()
                max_weight = int(drones_line[i + 1].strip())
                drones.append(Drone(name, max_weight))

            locations.sort(key=lambda location: location.weight, reverse=True)
            drones.sort(key=lambda drone: drone.max_weight, reverse=True)

            return drones, locations

    except FileNotFoundError:
        print("Input file not found.")

def make_deliveries(drones, locations):
    while locations:
        for drone in drones:
            remaining_capacity = drone.max_weight
            current_trip = []

            for location in locations[:]:
                if location.weight <= remaining_capacity:
                    current_trip.append(location.name)
                    remaining_capacity -= location.weight
                    locations.remove(location)
            if current_trip:
                drone.deliveries.append(current_trip)
                drone.current_weight = 0

    with open("output.txt", "w") as file:
        for drone in drones:
            file.write(f"[{drone.name}]\n")
            for index, trip in enumerate(drone.deliveries):
                file.write(f"Trip {index + 1}\n")
                formatted_trip = [f"[{location}]" for location in trip]
                file.write(", ".join(formatted_trip) + "\n")
            file.write("\n")

if __name__ == "__main__":
    main()
