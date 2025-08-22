class Rhombus:

    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, name, value):
        if name == "angle_a":
            if value <= 0 or value >= 180:
                print ("Rhombus should have angle a more than 0 & less then 180")
                value = 10
            super().__setattr__(name, value)
            super().__setattr__("angle_b", 180 - value)

        elif name == "side_a":
            if value <= 0:
                print ("Rhombus should have side a more than 0")
                value = 1
            super().__setattr__(name, value)

        else:
            super().__setattr__(name, value)

    def __str__(self):
        return f"Rhombus has side a ({self.side_a}), angle a ({self.angle_a}) and angle b ({self.angle_b})"

rhombus_1 = Rhombus(5, 80)
print(rhombus_1)
print("_"*80)
rhombus_2 = Rhombus(0, 0)
print(rhombus_2)
