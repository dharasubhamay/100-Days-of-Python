def turn_right():
    turn_left()
    turn_left()
    turn_left()

for _ in range(6):
    move()
    turn_left()
    for _ in range(2):
        move()
        turn_right()
    move()
    turn_left()    
