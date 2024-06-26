class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:

        seats = sorted(seats)
        students = sorted(students)

        diff = 0

        for i in range(len(students)):
            diff += abs(students[i] - seats[i])
        
        return diff

        