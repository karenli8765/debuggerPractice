from SparseArray import SparseArray


class ZorkMazeManager:

    def __init__(self, hop_interval: int = 5, clap_interval: int = 7, pat_interval: int = 11, num_vals: int = 100):
        self.sparseList: SparseArray[str] = SparseArray()
        for i in range(1, num_vals):
            if i % hop_interval == 0:
                self.sparseList.add_value_at("hop ", i)
            if i % clap_interval == 0:
                self.sparseList.add_value_at("clap", i)
            elif i % pat_interval == 0:
                self.sparseList.add_value_at("pat ", i)

    def __str__(self):
        return self.sparseList.__str__()
