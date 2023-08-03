import time


class Game:

    def __init__(self):
        self.present_state = [[',', '.', ','],
                              [',', '.', ','],
                              [',', '.', ',']]
        self.player_turn = 'X'

    def print_board(self):
        for i in self.present_state:
            for j in i:
                print(f"{j} |", end=" ")
            print()
        print()

    def is_valid(self, px, py):
        if px < 0 or px > 2 or py < 0 or py > 2:
            return False
        elif self.current_state[px][py] != '.':
            return False
        else:
            return True

    def is_end(self):
        for i in range(3):
            if self.present_state[0][i] != '.' and self.present_state[1][i] == self.present_state[0][i] and self.present_state[1][i] == self.present_state[2][i]:
                return self.present_state[0][i]

        for i in self.present_state:
            if i == ['X', 'X', 'X']:
                return 'X'
            elif i == ['O', 'O', 'O']:
                return 'O'

            if (self.current_state[0][0] != '.' and
                self.current_state[0][0] == self.current_state[1][1] and
                    self.current_state[0][0] == self.current_state[2][2]):
                return self.current_state[0][0]

        if (self.current_state[0][2] != '.' and
            self.current_state[0][2] == self.current_state[1][1] and
                self.current_state[0][2] == self.current_state[2][0]):
            return self.current_state[0][2]

        for i in range(0, 3):
            for j in range(0, 3):
                if (self.current_state[i][j] == '.'):
                    return None

        return '.'
