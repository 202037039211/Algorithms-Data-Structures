class R2Vector:
    def __init__(self, *, x, y):
        """
        Initialize a 2D vector with x and y components.
        """
        self.x = x
        self.y = y

    def norm(self):
        """
        Compute the norm (magnitude) of the vector.
        """
        return sum(val**2 for val in vars(self).values())**0.5

    def __str__(self):
        """
        Return a tuple representation of the vector for printing.
        """
        return str(tuple(getattr(self, i) for i in vars(self)))

    def __repr__(self):
        """
        Return a formal string representation of the vector.
        """
        arg_list = [f'{key}={val}' for key, val in vars(self).items()]
        args = ', '.join(arg_list)
        return f'{self.__class__.__name__}({args})'

    def __add__(self, other):
        """
        Add two vectors.
        """
        if type(self) != type(other):
            return NotImplemented
        kwargs = {i: getattr(self, i) + getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)

    def __sub__(self, other):
        """
        Subtract one vector from another.
        """
        if type(self) != type(other):
            return NotImplemented
        kwargs = {i: getattr(self, i) - getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)

    def __mul__(self, other):
        """
        Multiply the vector by a scalar or another vector.
        """
        if type(other) in (int, float):
            kwargs = {i: getattr(self, i) * other for i in vars(self)}
            return self.__class__(**kwargs)        
        elif type(self) == type(other):
            args = [getattr(self, i) * getattr(other, i) for i in vars(self)]
            return sum(args)  # Dot product
        return NotImplemented

    def __eq__(self, other):
        """
        Check if two vectors are equal.
        """
        if type(self) != type(other):
            return NotImplemented
        return all(getattr(self, i) == getattr(other, i) for i in vars(self))

    def __ne__(self, other):
        """
        Check if two vectors are not equal.
        """
        return not self == other

    def __lt__(self, other):
        """
        Compare vectors by their norm (magnitude).
        """
        if type(self) != type(other):
            return NotImplemented
        return self.norm() < other.norm()

    def __gt__(self, other):
        """
        Compare vectors by their norm (magnitude).
        """
        if type(self) != type(other):
            return NotImplemented
        return self.norm() > other.norm()

    def __le__(self, other):
        """
        Check if the vector is less than or equal to another vector by norm.
        """
        return not self > other

    def __ge__(self, other):
        """
        Check if the vector is greater than or equal to another vector by norm.
        """
        return not self < other


class R3Vector(R2Vector):
    def __init__(self, *, x, y, z):
        """
        Initialize a 3D vector with x, y, and z components.
        """
        super().__init__(x=x, y=y)
        self.z = z
        
    def cross(self, other):
        """
        Compute the cross product of two 3D vectors.
        """
        if type(self) != type(other):
            return NotImplemented
        kwargs = {
            'x': self.y * other.z - self.z * other.y,
            'y': self.z * other.x - self.x * other.z,
            'z': self.x * other.y - self.y * other.x
        }
        
        return self.__class__(**kwargs)

# Example usage
if __name__ == "__main__":
    v1 = R3Vector(x=2, y=3, z=1)
    v2 = R3Vector(x=0.5, y=1.25, z=2)
    print(f'v1 = {v1}')
    print(f'v2 = {v2}')
    
    v3 = v1 + v2
    print(f'v1 + v2 = {v3}')
    
    v4 = v1 - v2
    print(f'v1 - v2 = {v4}')
    
    v5 = v1 * v2  # Dot product
    print(f'v1 * v2 (Dot Product) = {v5}')
    
    v6 = v1.cross(v2)
    print(f'v1 x v2 (Cross Product) = {v6}')
