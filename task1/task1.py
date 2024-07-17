class Num(object):
    def __init__(self, max_value, val=1):
        self.val = val
        self.max_value = max_value

    def __add__(self, other):
        if isinstance(other, int):
            result = self.val + other
            if result <= self.max_value:
                return Num(max_value=self.max_value, val=result)
            else:
                return Num(max_value=self.max_value, val=result - self.max_value)
        raise TypeError

    def __eq__(self, other):
        if isinstance(other, int):
            if self.val == other:
                return True
            else:
                return False

    def __str__(self):
        return str(self.val)

def path_cycle_list(n: int, m: int):
    path = str(num := Num(max_value=n))
    while True:
        num += m - 1
        if num == 1:
            break
        path += str(num)
    return path


n, m = input(">>").split()
print(path_cycle_list(n=int(n), m=int(m)))
