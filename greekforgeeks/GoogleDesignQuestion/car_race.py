class Calculator(object):
    @staticmethod
    def top_speed(i):
        return 41.66 + 2.77 * i

    @staticmethod
    def acceleration(i):
        return 2.0*i

    @staticmethod
    def handling_factor():
        return 0.8


class Car(object):
    def __init__(self, i, starting_position, finish_position):
        self.car_number = i
        self.top_speed = Calculator.top_speed(i)
        self.acceleration = Calculator.acceleration(i)
        self.handling_factor = Calculator.handling_factor()
        self.position = starting_position
        self.current_speed = 0.0
        self.finish_nitro = False
        self.finish_position = finish_position

    def set_current_speed(self, time, slow, nitro_on):
        if nitro_on:
            self.current_speed = self.nitro()
        elif slow:
            self.current_speed *= self.handling_factor
        else:
            self.current_speed += acceleration * time

    def set_current_position(self, time):
        if self.position < self.finish_position:
            self.position += current_speed * time
            return False
        else:
            return True

    def nitro(self):
        if self.finish_nitro:
            return self.current_speed *= acceleration * time
        else:
            self.finish_nitro = True
            return min(self.current_speed * 2, self.top_speed)

    def __cmp__(self, other_car):
        if self.position < other_car.position:
            return -1
        elif self.position == other_car.position:
            return 0
        else:
            return 1

class Race(object):
    def __init__(self, number_of_cars, length_of_track):
        self.length_of_track = length_of_track
        self.positions = []
        self.final_speeds = []
        self.completion_times = []
        position_i = 0.0
        for i in range(number_of_cars):
            p = Race.get_start_position(position_i, i)
            car = Car(i, p)
            self.positions.insert(0, car)
            self.final_speeds.append(0)
            self.completion_times.append(0)
            position_i = p

    @staticmethod
    def too_close(i, j):
        if abs(i-j) < 10:
            return True
        return False

    def run_race(self):
        time_interval = 2
        number_of_cars_left = len(self.positions)
        while number_of_cars_left != 0:
            for i in range(len(self.positions)):
                # Iterate through list while changing. 
                car
                if i < number_of_cars_left:
                    next_car_position = self.positions[i+1].position
                    if too_close(car_position, next_car_position):


    @staticmethod
    def get_start_position(i_position, i):
        return i_position - 200 * i
