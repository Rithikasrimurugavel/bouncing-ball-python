import time
# Set game time limit for 1 minute (60 seconds)
timeout = time.time() + 10*6
gametime = 0
if gametime == 6 or time.time() > timeout:
    gametime = gametime - 1
    break;

if (int(score) > int(comp_score)):
    mypen.setposition(0, 0)
    mypen.color("yellow")
    mypen.write("Game Over: You WIN", False, align="center", font=("Arial", 28, "normal"))
else:
    mypen.setposition(0, 0)
    mypen.color("yellow")
    mypen.write("Game Over: You LOSE")
delay = input("Press Enter to finish.")
