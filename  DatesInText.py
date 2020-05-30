# Task: Dates in text

Months = {
    "January": 31,    "1": 31,
    "February": 28,   "2": 28,
    "March": 31,      "3": 31,
    "April": 30,      "4": 30,
    "May": 31,        "5": 31,
    "June": 30,       "6": 30,
    "July": 31,       "7": 31,
    "August": 31,     "8": 31,
    "September": 30,  "9": 30,
    "October": 31,    "10": 31,
    "November": 30,   "11": 30,
    "December": 31,   "12": 31
}
digitMonth = {"1": "January", "2": "February", "3": "March", "4": "April", "5": "May", "6": "June",
              "7": "July", "8": "August", "9": "September", '10': "October", "11": "November", "12": "December"
              }


def closestDay(dList, n):
    range = float("inf")
    day = dList[0][0]
    for j in dList:
        if abs(n-j[1]) < range:
            range = abs(n-j[1])
            day = j[0]
    return day


N = int(input())
for line in range(N):
    row, digits = [], []
    currentString = input().split()

    for word in currentString:
        indx = currentString.index(word)
        word = word.rstrip(',')
        word = word.rstrip('.')
        if word[0].isdigit():
            day_month = word.split('.')

            # case 1: S contains one DM-date and it does not contain any month name.
            if len(day_month) == 2 and day_month[0].isdigit() and day_month[1].isdigit():
                d, m = int(day_month[0]), day_month[1]
                if m in Months and Months[m] >= d: row.append((digitMonth[m], d, line, 1))

            # case 2: S contains exactly one month name, at least 1 integer = day
            elif len(day_month) == 1 and day_month[0].isdigit():
                if int(day_month[0]) <= 31: digits.append((int(day_month[0]), indx))

        elif word in Months:
            row.append(((word, indx), digits, line, 2))

    if len(row) == 1:
        D = row[0]
        # D[0]=month, D[1]=days, D[2]=row, D[3]=case
        if D[3] == 1:
            print(str(D[2] + 1) + '. ', D[0], D[1])
        else:
            if D[1]:
                m, idx = D[0][0], D[0][1]
                newDigits = [i for i in D[1] if Months[m] >= i[0]]
                # print(" - - - ",D[2]+1, newDigits)
                closeDay = closestDay(newDigits, idx)
                print(str(D[2] + 1) + '. ', m, closeDay)



