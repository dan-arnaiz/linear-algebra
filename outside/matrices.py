class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        total_beams = 0
        rows_with_devices = [i for i in range(len(bank)) if '1' in bank[i]]
        for i in range(len(rows_with_devices) - 1):
            devices_i = [k for k in range(len(bank[rows_with_devices[i]])) if bank[rows_with_devices[i]][k] == '1']
            devices_j = [k for k in range(len(bank[rows_with_devices[i + 1]])) if bank[rows_with_devices[i + 1]][k] == '1']
            total_beams += len(devices_i) * len(devices_j)
        return total_beams