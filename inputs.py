class Inputs:
    def __init__(self):
        None
    def catch():
        user_input = input()
        if user_input == 'z':
            return "top"
        elif user_input == 'q':
            return "left"
        elif user_input == 's':
            return "bottom"
        elif user_input == 'd':
            return "right"
        
    def relativeCatch():
        user_input = input()
        if user_input == 'z':
            return "continue"
        elif user_input == 'q':
            return "turnLeft"
        elif user_input == 'd':
            return "turnRight"