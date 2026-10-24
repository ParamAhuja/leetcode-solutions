# easy
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        def daysCount(date):
            mtd = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
            month = int(date[:2])-2
            days = int(date[3:])
            if month>=0:
                days+= mtd[month]
            return days
        arriveAlice = daysCount(arriveAlice)
        leaveAlice = daysCount(leaveAlice)
        arriveBob = daysCount(arriveBob)
        leaveBob = daysCount(leaveBob)

        if arriveAlice<=arriveBob and leaveAlice>=arriveBob:
            return min(leaveBob, leaveAlice) - arriveBob +1
        elif arriveAlice>=arriveBob and leaveBob>=arriveAlice:
            return min(leaveBob, leaveAlice) - arriveAlice +1
        else:
            return 0


