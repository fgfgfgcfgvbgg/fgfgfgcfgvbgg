from graphics import *


# Save data in file
def save_file(data: list, cvb: list):
    with open("hu.txt", "a") as file:
        for x in data:
            slip_list = ",".join(map(str, x)).rsplit(",")
            file.write(slip_list[0] + "-" + slip_list[1] + "," + slip_list[2] + "," + slip_list[-1])
            file.write("\n")
        file.write("Histogram Counts:\n")
        for x in cvb:
            file.write(",".join(map(str, x)))
            file.write("\n")


# Read data from file
def read_data(data: list = [], cvb: list = []):
    try:
        with open("hu.txt", "r") as file:
            lines = file.readlines()
            str_line = [string.rstrip() for string in lines]

            for line in str_line:

                if len(line) == 7:
                    num_list = line.split(",")
                    cvb = [int(num) for num in num_list]
                elif line == "Histogram Counts:":
                    pass
                else:
                    jkl = line.split(",")
                    data.append([jkl[0].split("-")[0], jkl[0].split("-")[1], jkl[1], jkl[2]])

            return data, cvb

    except FileNotFoundError:
        return data, cvb


# Output what is the progress
def abc(Pass, defear, fail):
    zxc = ""
    count_exclude = 0
    count_donot_progress = 0
    count_progress = 0
    count_Progress_m = 0

    if Pass == 120:
        zxc = "progress"
        count_progress += 1
    elif defear <= 20 and fail <= 20:
        zxc = "progress(m)"
        count_Progress_m += 1
    elif fail < 80:
        zxc = "do not progress"
        count_donot_progress += 1
    else:
        zxc = "exclude"
        count_exclude += 1

    print(zxc)
    return count_exclude, count_donot_progress, count_progress, count_Progress_m, zxc


# Getting inputs function
def getting_inputs():
    while True:
        while True:
            try:
                pass_value = int(input("Enter your Pass: "))
            except ValueError:
                print("Please enter a valid integer")
                continue
            if pass_value not in range(0, 121, 20):
                print("Out of range")
                continue
            break

        while True:
            try:
                defear_value = int(input("Enter your defear: "))
            except ValueError:
                print("Please enter a valid integer")
                continue
            if defear_value not in range(0, 121, 20):
                print("Out of range")
                continue
            break

        while True:
            try:
                fail_value = int(input("Enter your fail: "))
            except ValueError:
                print("Please enter a valid integer")
                continue
            if fail_value not in range(0, 121, 20):
                print("Out of range")
                continue
            break

        if pass_value + defear_value + fail_value != 120:
            print("Total incorrect")
            continue
        break
    return pass_value, defear_value, fail_value


# Display histogram function
def display_histogram(count_exclude, count_donot_progress, count_progress, count_Progress_m):
    b1len = 600 - (count_exclude * 15)
    b2len = 600 - (count_donot_progress * 15)
    b3len = 600 - (count_progress * 15)
    b4len = 600 - (count_Progress_m * 15)

    try:
        desktop = GraphWin("Histogram", 800, 845)
        desktop.setBackground("gray")

        label = Text(Point(150, 50), "Histogram Results")
        label.setStyle("bold")
        label.setSize(18)
        label.draw(desktop)

        bottom = Line(Point(100, 600), Point(750, 600))
        bottom.draw(desktop)

        b1name = Text(Point(175, b1len - 10), str(count_exclude))
        b1name.draw(desktop)

        bl1 = Text(Point(175, 610), "Exclude")
        bl1.draw(desktop)

        box1 = Rectangle(Point(125, 600), Point(225, b1len))
        box1.setFill("Pale Violet Red")
        box1.draw(desktop)

        b2name = Text(Point(290, b2len - 10), str(count_donot_progress))
        b2name.draw(desktop)

        bl2 = Text(Point(290, 610), "Do not progress")
        bl2.draw(desktop)

        box2 = Rectangle(Point(240, 600), Point(340, b2len))
        box2.setFill("Saddle Brown")
        box2.draw(desktop)

        b3name = Text(Point(405, b3len - 10), str(count_progress))
        b3name.draw(desktop)

        bl3 = Text(Point(405, 610), "Progress")
        bl3.draw(desktop)

        box3 = Rectangle(Point(355, 600), Point(455, b3len))
        box3.setFill("ForestGreen")
        box3.draw(desktop)

        b4name = Text(Point(520, b4len - 10), str(count_Progress_m))
        b4name.draw(desktop)

        bl4 = Text(Point(520, 610), "Progress(M)")
        bl4.draw(desktop)

        box4 = Rectangle(Point(470, 600), Point(570, b4len))
        box4.setFill("Deep Sky Blue")
        box4.draw(desktop)

        bl5 = Text(Point(100, 650),
                   f" {count_exclude + count_progress + count_Progress_m + count_donot_progress} outcomes in Total")
        bl5.setStyle("bold")
        bl5.draw(desktop)

        desktop.getMouse()  # Wait for a mouse click
        desktop.close()

    except GraphicsError:
        pass
    except Exception as e:
        print(f"Some Error Occurred: {e}")
    return None


# program variables
data = []
count_exclude = 0
count_donot_progress = 0
count_progress = 0
count_Progress_m = 0
cvb = []

# main program loop
while True:
    kZXC = input("Enter mode (teacher mode(pm) or student mode(sm)): ")
    if kZXC.lower() == "sm" or kZXC.lower() == "pm":
        break
    else:
        print("Not valid")
        continue

while True:
    if kZXC.lower() == "sm":
        pass_value, defear_value, fail_value = getting_inputs()
        count_exclude_temp, count_donot_progress_temp, count_progress_temp, count_Progress_m_temp, zxc = abc(pass_value,
                                                                                                             defear_value,
                                                                                                             fail_value)
        amara = [zxc, pass_value, defear_value, fail_value]
        data.append(amara)
        count_exclude += count_exclude_temp
        count_donot_progress += count_donot_progress_temp
        count_progress += count_progress_temp
        count_Progress_m += count_Progress_m_temp
        mnb = [count_exclude, count_donot_progress, count_Progress_m, count_progress]
        cvb.append(mnb)

    elif kZXC.lower() == "tm":
        data, cvb = read_data(data, cvb)
        display_histogram(cvb[0], cvb[1], cvb[2], cvb[3])
        break

    # Ask the user if they want to play again
    while True:
        user_again_input = input("\n'y' for play again, 'q' for quit: ")
        if user_again_input.lower() == "y" or user_again_input.lower() == "q":
            break
        else:
            print('Not valid')
            continue

    if user_again_input.lower() == "y":
        continue
    elif user_again_input.lower() == "q":
        save_file(data, cvb)
        break
