class MaxHeap:

    def __init__(self):
        self.data = [None]


    def insert(self, item):
        self.data.append(item)
        insert_idx = self.data.index(item)
        parent_idx = insert_idx  // 2
        while (parent_idx >= 1) and (self.data[parent_idx] < item) :
            self.data[parent_idx], self.data[insert_idx] = item, self.data[parent_idx]
            insert_idx = parent_idx
            parent_idx = insert_idx // 2
