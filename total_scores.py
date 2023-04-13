lows = 0
meds = 0
highs = 0
grounds = 0
parkeds = False
history = []
stri = ""


class Scores:
    global history
    global lows
    global meds
    global highs
    global grounds

    def add(User_in):
        global history
        global lows
        global meds
        global highs
        global grounds
        if (User_in == "ground"):
            grounds += 1
        elif (User_in == "low"):
            lows += 1
        elif (User_in == "med"):
            meds += 1
        elif (User_in == "high"):
            highs += 1
        elif (User_in == "park"):
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
        return "Grounds: " + str(grounds) + " Lows: " + str(lows) + " Mediums: " + str(meds) + " Highs: " + str(
            highs) + " Parked?: " + str(parkeds)

    def __str__(self):
        global history
        if (len(history) == 0):
            return "please enter runs"
        x = 0
        stri = ""
        while (x < len(history)):
            stri += "Grounds: " + str(history[x]) + " Lows: " + str(history[x + 1]) + " Meds: " + str(
                history[x + 2]) + " Highs: " \
                    + str(history[x + 3]) + " Parked?: " + str(history[x + 4]) + "<br> \n"
            x += 5

        return stri
