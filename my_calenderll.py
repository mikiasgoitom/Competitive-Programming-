class MyCalendarTwo:
    def __init__(self):
        self.single_booking = []
        self.double_booking = []

    def book(self, start: int, end: int) -> bool:
        for double_start, double_end in self.double_booking:
            if start < double_end and end > double_start:
                return False
        for single_start, single_end in self.single_booking:
            if start < single_end and end > single_start:
                overlap_start = max(single_start, start)
                overlap_end = min(single_end, end)
                self.double_booking.append([overlap_start, overlap_end])
        self.single_booking.append([start, end])
        
        return True

obj = MyCalendarTwo()
print(obj.book(10, 20))
print(obj.book(50, 60))
print(obj.book(10, 40))
print(obj.book(5, 15))
print(obj.book(5, 10))