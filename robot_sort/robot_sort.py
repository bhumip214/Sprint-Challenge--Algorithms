class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
    # Implementing Bubble Sort and gradually moving larger item towards the end of the array.
        # First turn on the light 
        # Loop through the list while Robot's light is on
            # Swap first and then move right 
            # Compare the item that robot is holding to the item in front of it in list.
            # If value of item holding is greater,
                    # 1. Then swap them so now robot is holding an item with smaller value
                    # 2. After that move left and drop the item with smaller value there 
                    # 3. Now, move right and pick up the next item 
            # If value of item holding is less or equal then repeat step 2 and 3 from above. 
        # When Robot's light is off then stop. Else, go back to the item at index 0 and repeat the process.
        
        self.set_light_on()
        while self.light_is_on():
            # print "start of the loopy loooooooooooop"
            self.set_light_off()

            if self.compare_item() is None:
                self.swap_item()

            while self.can_move_right() is True:
                self.move_right()
                
                # print "BEFORE ---------------------------"
                # print "compare item"
                # print self.compare_item()
                # print self._list

                if self.compare_item() == 1:
                    self.swap_item()
                    self.move_left()
                    self.swap_item()
                    self.move_right()
                    self.swap_item()
                    self.set_light_on()

                elif self.compare_item() == -1 or self.compare_item() == 0:
                    self.move_left()
                    self.swap_item()
                    self.move_right()
                    self.swap_item()

                if self.can_move_right() is not True:
                    self.swap_item()

                # print "AFTER ---------------------------"
                # print "position"
                # print self._position
                # print self._list
                
            while self.can_move_left() is True:
                self.move_left()



from time import time

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    # Store a startin time
    start_time = time()

    # Run our code
    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)

    # Store the ending time
    end_time = time()

    print (end_time - start_time)