class Rhomb:
    def __setattr__(self, name, value):
        if name == "length_a":
            if value <= 0:
                raise ValueError("The length of the rhomb must be greater than 0!")
            super().__setattr__(name, value)

        elif name == "angle_a":
            if not (0 < value < 180):
                raise ValueError("The angle of the rhomb must be greater than 0 and less than 180!")
            super().__setattr__(name, value)

            super().__setattr__("angle_b", 180 - value)

        elif name == "angle_b":
            raise AttributeError("angle_b is calculated automatically, do not set it directly.")

        else:
            super().__setattr__(name, value)


rhomb = Rhomb()
rhomb.length_a = 10
rhomb.angle_a = 60

print(f"The length of the rhomb is: {rhomb.length_a}")
print(f"The angle_a of the rhomb is: {rhomb.angle_a}")
print(f"The angle_b of the rhomb is: {rhomb.angle_b}")