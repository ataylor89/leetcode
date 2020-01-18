class Solution(object):
    def readBinaryWatch(self, num):
        times = []
        self._readBinaryWatch([0] * 10, 0, 0, num, times)
        return times
        
    def _readBinaryWatch(self, time, index, leds, maxLeds, times):
        if leds == maxLeds:
            h = self.hours(time)
            m = self.minutes(time)
            times.append(str(h) + ':' + format(m, '02d'))
            
        elif index == len(time):
            return
            
        elif index < 6:
            timeA = list(time)
            timeB = list(time)
            timeA[index] = 1
            
            if self.minutes(timeA) < 60:
                self._readBinaryWatch(timeA, index+1, leds+1, maxLeds, times)
            self._readBinaryWatch(timeB,index+1, leds, maxLeds, times)
            
        else:
            timeA = list(time)
            timeB = list(time)
            timeA[index] = 1
            
            if self.hours(timeA) < 12:
                self._readBinaryWatch(timeA, index+1, leds+1, maxLeds, times)
            self._readBinaryWatch(timeB, index+1, leds, maxLeds, times)
        
        
    def hours(self, time):
        return time[9]*8 + time[8]*4 + time[7]*2 + time[6]
    
    def minutes(self, time):
        return time[5]*32 + time[4]*16 + time[3]*8 + time[2]*4 + time[1]*2 + time[0]
