class Solution(object):
    def numberOfWays(self, corridor):
        MOD = 10**9 + 7
        scount = corridor.count('S')
        if scount < 2 or scount % 2 != 0:
            return 0
        if scount == 2:
            return 1

        ways = 1
        seat_seen = 0
        plant_between = 0

        for ch in corridor:
            if ch == 'S':
                seat_seen += 1
                if seat_seen > 2 and seat_seen % 2 == 1:
                    ways = (ways * (plant_between + 1)) % MOD
                    plant_between = 0
            else:
                if seat_seen >= 2 and seat_seen % 2 == 0:
                    plant_between += 1

        return ways
