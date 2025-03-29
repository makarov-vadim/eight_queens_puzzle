class EightQueensPuzzle:
    '''Класс, описывающий задачу о восьми ферзях'''
    def __init__(self, dimension=8):
        self._dimension = dimension
        self._target = dimension
        self._count = 0

        self._rows = []
        self._columns = []
        self._left_diagonals = []
        self._right_diagonals = []

        self._solutions = []

    @property
    def dimension(self):
        return self._dimension

    @property
    def target(self):
        return self._target

    @property
    def solutions(self):
        return tuple(self._solutions)

    @property
    def count_solutions(self):
        return len(self.solutions)

    def _get_left_diagonal(self, i, j):
        '''Метод, возвращающий идентификатор левой диагонали по координатам'''
        return i + j

    def _get_right_diagonal(self, i, j):
        '''Метод, возвращающий идентификатор правой диагонали по координатам'''
        return self.dimension - 1 - (j - i)

    def _is_valid_position(self, i, j):
        '''Метод, возвращающий True, если координаты являются допустимыми
        для установки ферзя и False в обратном случае'''
        is_not_rows = i not in self._rows
        is_not_columns = j not in self._columns
        is_not_in_left_diagonals = self._get_left_diagonal(i, j) not in self._left_diagonals
        is_not_in_right_diagonals = self._get_right_diagonal(i, j) not in self._right_diagonals

        if all((is_not_rows, is_not_columns, is_not_in_left_diagonals, is_not_in_right_diagonals)):
            return True
        return False

    def _add_queen(self, i, j):
        '''Метод, добавляющий ферзя по координатам'''
        self._rows.append(i)
        self._columns.append(j)
        self._left_diagonals.append(self._get_left_diagonal(i, j))
        self._right_diagonals.append(self._get_right_diagonal(i, j))

        self._count += 1

    def _pop_queen(self):
        '''Метод, удаляющий последнего добавленного ферзя'''
        self._rows.pop()
        self._columns.pop()
        self._left_diagonals.pop()
        self._right_diagonals.pop()

        self._count -= 1

    def _save_solution(self):
        '''Метод, сохраняющий и возвращающий найденное решение'''
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        get_letter = lambda i: letters[i % len(letters)] * (i // len(letters) + 1)

        solution = ' '.join([f'{get_letter(i)}{j + 1}' for i, j in zip(self._rows, self._columns)])
        self._solutions.append(solution)
        return solution

    def _search_rec(self, i=0):
        '''Рекурсивный метод, который определяет допустимые решения задачи о восьми ферзях'''
        for j in range(self.dimension):
            if self._is_valid_position(i, j):
                self._add_queen(i, j)
                if self._count == self.target:
                    self._save_solution()
                else:
                    self._search_rec(i + 1)
                self._pop_queen()

    def search(self):
        '''Метод, возвращающий решение задачи о восьми ферзях'''
        if not self.solutions:
            self._search_rec()
        return self.solutions

if __name__ == "__main__":
    eight_queens_puzzle = EightQueensPuzzle()

    eight_queens_puzzle.search()
    print(*eight_queens_puzzle.solutions, sep='\n')
    print(eight_queens_puzzle.count_solutions)