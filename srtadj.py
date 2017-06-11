import re
import sys
"""adjust .srt scaler & offset
"""

#f = open("It's such a beautiful day.srt", "r")
f = open("The Sting.srt", "r")
out = f.read().split("\n")
f.close()

class SrtLine:
    def __init__(self, idx):
        self.idx = idx
        self.time_st = ""
        self.time_ed = ""
        self.lines = []

    def get_time(self, offset=0, scale=1):

        time_out = []

        for time in [self.time_st, self.time_ed]:
            m = re.search(r"([0-9]+):([0-9]+):([0-9]+),([0-9]+)", time)
            t_hr = int(m.group(1))
            t_min = int(m.group(2))
            t_sec = int(m.group(3))
            t_msec = int(m.group(4))
            total_m = (t_hr * 3600 + t_min * 60 + t_sec) * 1000 + t_msec

            # calculate new time
            total_m = total_m * scale + offset
            
            out_msec = total_m % 1000
            out_sec = (total_m / 1000) % 60
            out_min = ((total_m / 1000) % 3600) / 60
            out_hr = ((total_m / 1000) / 3600)
            time_out.append("%02d:%02d:%02d,%03d" % (out_hr, out_min, out_sec, out_msec))

        return time_out


srt_list = []
state = 0
line_cnt = 1

for idx, line in enumerate(out):
    if state == 0 and line:
        try:
            if int(line) == line_cnt:
                srt_list.append(SrtLine(line_cnt))
                line_cnt += 1
                state = 1
        except:
            break

    elif state == 1:
        m = re.search(r"(.*) --> (.*)", line)
        srt_list[-1].time_st = m.group(1)
        srt_list[-1].time_ed = m.group(2)
        state = 2

    else:
        if line:
            srt_list[-1].lines.append(line)
        else:
            state = 0

for srt in srt_list:
    print srt.idx
    curr_time = srt.get_time(200, 0.9592442)
    print "%s --> %s" % (curr_time[0], curr_time[1])
    print "\n".join(srt.lines)
    print 
print 
