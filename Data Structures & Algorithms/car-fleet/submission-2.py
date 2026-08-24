class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        from operator import itemgetter
        # sort cars backwards in monotonic stack
        # find the time that they will arrive to the target using their speed
        # if a car that is behind a car ahead reaches before or the same time, they become a fleet
        # find the number of distinct fleets using this

        # times = {}
        # position.sort()
        # position = position[::-1]
        # speed.sort()
        # speed = speed[::-1]
        # # calc time of arrival for every car

        cars = []

        for i in range(len(position)):
            distance = target - position[i]
            toa = distance / speed[i]
            cars.append((position[i], toa))

        cars = sorted(cars, key=itemgetter(0))
        cars = cars[::-1]
        fleetStack = []

        # using a stack, check if cars will arrive in fleets

        for i in range(len(position)):
            # check with last item in carStack
            # if the toa of the last fleet is after or equal to the car to be added, the new car becomes a part of the fleet
            # otherwise it becomes a new fleet as it arrives later
            # only need to look at the first time of the fleet, because it will be the smallest

            if i == 0:
                fleetStack.append([cars[i][1]])
            else:
                topFleet = fleetStack[-1][0]
                if cars[i][1] <= topFleet:
                    pass
                else:
                    fleetStack.append([cars[i][1]])
        
        return len(fleetStack)

