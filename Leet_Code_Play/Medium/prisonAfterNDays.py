# https://www.youtube.com/watch?v=qBxsNCsFj4w

class Solution:
    def prisonAfterNDays(self, cells, n):
        cells = tuple(cells)
        holling = {}
        while n:
            holling[cells] = n
            n -= 1
            cells = tuple([0] + [cells[i - 1] ^ cells[i + 1] ^ 1 for i in range(1, 7)] + [0])
            if cells in holling:
                assert(holling[cells] - n in (1, 7, 14))
                n %= holling[cells] - n
                break

        while n:
            n -= 1
            cells = tuple([0] + [cells[i - 1] ^ cells[i + 1] ^ 1 for i in range(1, 7)] + [0])
        return list(cells)

cells = [0,1,0,1,1,0,0,1]
days = 7

print(Solution().prisonAfterNDays(cells, days))