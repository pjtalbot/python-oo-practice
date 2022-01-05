"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=1):
        self.start = self.next = start

    def generate(self):
        """Returns start on first call, and "next" on following calls"""
        self.next += 1
        return self.next - 1
    
    def reset(self):
        self.next = self.start
        print(f"reset to {self.start}")