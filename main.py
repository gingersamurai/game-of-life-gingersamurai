import random
import time
import os

class field(set):
    def __init__(self, gen=0):
        self.gen = gen
        self.LU = (0, 0)
        self.RD = (0, 0)
        super().__init__()

    def get_LU(self):
        ans = list(self.LU)
        for i in self:
            ans[0] = min(ans[0], i[0])
            ans[1] = min(ans[1], i[1])
        return tuple(ans)
    
    def get_RD(self):
        ans = list(self.RD)
        for i in self:
            ans[0] = max(ans[0], i[0])
            ans[1] = max(ans[1], i[1])
        return tuple(ans)

    def add(self, x):
        super().add(x)
        self.LU = self.get_LU()
        self.RD = self.get_RD()

    def print_field(self):
        for i in range(self.LU[0], self.RD[0] + 1):
            for j in range(self.LU[1], self.RD[1] + 1):
                cell = '.'
                if (i, j) in self:
                    cell = '#'
                print(cell, end=' ')
            print()
        print('-' * 2 * (self.get_RD()[1] - self.get_LU()[1] + 1) ," gen = ", self.gen)

    def next_gen(self):
        nself = field(self.gen+1)
        nself.LU = self.get_LU()
        nself.RD = self.get_RD()
        for i in range(self.LU[0]-1, self.RD[0] + 2):
            for j in range(self.LU[1]-1, self.RD[1] + 2):
                nei_cnt = 0
                for ni in range(i-1, i+2):
                    for nj in range(j-1, j+2):
                        if ni == i and nj == j:
                            continue
                        if (ni, nj) in self:
                            nei_cnt += 1
                if 2 <= nei_cnt <= 3 and (i, j) in self:
                    nself.add((i, j))
                elif nei_cnt == 3 and not (i, j) in self:
                    nself.add((i, j))
        nself.LU = nself.get_LU()
        nself.RD = nself.get_RD()
        return nself

    def rand_fill(self, cnt=1, min_val=0, max_val=20):
        for _ in range(cnt):
            self.add((random.randint(min_val, max_val), random.randint(min_val, max_val)))

    def simulate(self, cnt=100, bu_out = True):
        self.print_field()
        for _ in range(cnt):
            self = self.next_gen()
            self.print_field()
            if bu_out:
                time.sleep(0.12)
                os.system('cls')
        

print("""
    GAME OF LIFE

    author: @gingersamurai

""")
game1 = field()
mode = int(input("""
    enter mode:
    1 - generate random field
    2 - create field 
"""))

if mode == 1:
    cnt = int(input("enter count of cells: "))
    game1.rand_fill(cnt)







