class Triangle:
  """
  This class represents a triangle and provides methods to calculate its properties based on side lengths.
  """

  def __init__(self, side_a, side_b, side_c):
    """
    Initializes a Triangle object.

    Args:
      side_a: Length of the first side (float).
      side_b: Length of the second side (float).
      side_c: Length of the third side (float).

    Raises:
      ValueError: If the sides violate the triangle inequality.
    """

    self.side_a = side_a
    self.side_b = side_b
    self.side_c = side_c

    self._validate_triangle()

  def _validate_triangle(self):
    """
    Checks if the triangle sides satisfy the triangle inequality.

    Raises:
      ValueError: If the triangle inequality is violated.
    """
    sides = [self.side_a, self.side_b, self.side_c]
    for i in range(3):
      if sum(sides[:i]) <= sides[i]:
        raise ValueError("Sides do not form a valid triangle.")

  def is_right_angled(self):
    """
    Checks if the triangle is right-angled.

    Returns:
      True if the triangle is right-angled, False otherwise.
    """
    # Check if any side squared is equal to the sum of the squares of the other two sides
    a2 = self.side_a * self.side_a
    b2 = self.side_b * self.side_b
    c2 = self.side_c * self.side_c
    return (a2 == b2 + c2) or (b2 == a2 + c2) or (c2 == a2 + b2)

  def calculate_area(self):
    """
    Calculates the area of the triangle using Heron's formula.

    Returns:
      The area of the triangle (float), or None if the triangle is invalid.
    """
    if not self._is_valid_triangle():
      return None
    s = (self.side_a + self.side_b + self.side_c) / 2  # Semi-perimeter
    return (s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c)) ** 0.5

  def _is_valid_triangle(self):
    """
    Helper function to check if the triangle is valid (sides satisfy triangle inequality).

    Returns:
      True if the triangle is valid, False otherwise.
    """
    try:
      self._validate_triangle()
      return True
    except ValueError:
      return False

# Example usage
try:
  triangle = Triangle(3, 4, 5)  # Valid triangle
  print("Area:", triangle.calculate_area())
  print("Right angled:", triangle.is_right_angled())

  triangle = Triangle(1, 2, 4)  # Invalid triangle
  print(triangle.calculate_area())  # This will return None

except ValueError as e:
  print("Error:", e)
