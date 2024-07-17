cycle_path = input("Cycle coordinates file path: ")
points_path = input("Points coordinates file path: ")

def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def check_point_belonging(radius, _distance):
    if _distance < radius:
        return 1
    elif _distance > radius:
        return 2
    else:
        return 0


with open(cycle_path, 'r') as f_obj:
    x_c, y_c = f_obj.readline().split()
    x_c, y_c = float(x_c), float(y_c)
    r_c = int(f_obj.readline())

with open(points_path, 'r') as f_obj:
    for point in f_obj.readlines():
        x_p, y_p = point.strip().split()
        x_p, y_p = float(x_p), float(y_p)
        result = check_point_belonging(
            radius=r_c,
            _distance=distance(x_c, y_c, x_p, y_p)
        )
        print(result)
