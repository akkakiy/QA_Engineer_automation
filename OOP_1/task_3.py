class PointsForPlace:
    def __init__(self):
        self.points = 0

    def get_points_for_place(self, place):
        if place > 100:
            print("Баллы начисляются только первым 100 участникам")
        elif place < 1:
            print("Спортсмен не может занять нулевое или отрицательное место")
        else:
            self.points = 101 - place
            return self.points


class PointsForMeters:
    @staticmethod
    def get_points_for_meters(meters):
        if meters < 0:
            print("Количество метров не может быть отрицательным")
        else:
            return meters * 0.5


class TotalPoints(PointsForPlace, PointsForMeters):
    def __init__(self):
        super().__init__()

    def get_total_points(self, place, meters):
        self.place = place
        self.meters = meters
        self.total = self.get_points_for_place(place) + self.get_points_for_meters(meters)
        return self.total


points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))
print()
points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))
print()
total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(10, 10))
