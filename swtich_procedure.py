switch_status = False

def turn_on():
    global switch_status
    switch_status = True
    print("On")

def turn_off():
    global switch_status
    switch_status = False
    print("Off")

if __name__ == "__main__":
    print(f'status:{switch_status}')
    turn_on()
    turn_off()
    turn_off()
    turn_off()