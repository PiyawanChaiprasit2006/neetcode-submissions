class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        temps = []
        result = [0] * len(temperatures)

        curr_temp = 0

        for i in range(len(temperatures)):
            while temps and temperatures[i] > temperatures[temps[-1]]:
                t = temps.pop()
                days = i - t
                result[t] = days
            temps.append(i)

        return result


            

        