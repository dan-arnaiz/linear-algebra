class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        total_beams = 0
        for i in range(len(bank)):
            devices_i = [k for k in range(len(bank[i])) if bank[i][k] == '1']
            for j in range(i + 1, len(bank)):
                if all(bank[k].count('1') == 0 for k in range(i + 1, j)):
                    devices_j = [k for k in range(len(bank[j])) if bank[j][k] == '1']
                    total_beams += len(devices_i) * len(devices_j)
        return total_beams