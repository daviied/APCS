lows = 0
meds = 0
highs = 0
grounds = 0
parkeds = False
history = []
stri = ""


class Scores:
    def small(self):
        global lows
        lows += 1

    def med(self):
        global meds
        meds += 1

    def high(self):
        global highs
        highs += 1

    def ground(self):
        global grounds
        grounds += 1

    def park(self):
        global parkeds
        if (parkeds == False):
            parkeds = True
        elif (parkeds == True):
            parkeds = False

    def new(self):
        global history
        global lows
        global meds
        global highs
        global grounds
        global parkeds
        history.append(grounds)
        history.append(lows)
        history.append(meds)
        history.append(highs)
        history.append(parkeds)
        lows = 0
        meds = 0
        highs = 0
        grounds = 0
        parkeds = False
        print(history)
    def current(self):
        global history
        global lows
        global meds
        global highs
        global grounds
        global parkeds
        return "Grounds: " + str(grounds) + " Lows: " + str(lows) + " Mediums: " + str(meds) + " Highs: " + str(highs) + " Parked?: " + str(parkeds)

    def __str__(self):
        global history
        if (len(history) == 0):
            return "please enter runs"
        x = 0
        stri = ""
        while (x < len(history)):
            stri += "Grounds: " + str(history[x]) + " Lows: " + str(history[x + 1]) + " Meds: " + str(history[x + 2]) + " Highs: " + str(history[x + 3]) + " Parked?: " + str(history[x + 4]) + "<br> \n"
            x += 5

        return stri
