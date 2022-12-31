import datetime, calendar


def main():
    for i in range(1006, 1996, 10):
        d = datetime.date(i, 1, 26)
        if d.isoweekday() == 1 and calendar.isleap(i):
            print(d)

if __name__ == '__main__':
    main()