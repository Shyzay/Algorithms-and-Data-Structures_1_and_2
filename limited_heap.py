class BinHeap:
    """
    Binary Heap with a limited Heap size
    """
    def __init__(self, n):
        self.heap_limit = n
        self.heap_list = [0]
        self.current_size = 0

    def perc_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp
            i = i // 2

    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def perc_down(self, i):
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = tmp
            i = mc
            #print (self.heap_list)

    #Insert Method modified for the Binary Heap with a limited heap size
    def insert(self, k):
        if self.current_size >= self.heap_limit:
            print("Removing the least item...")
            self.heap_list.pop()
            self.heap_list.append(k)
            self.perc_up(self.current_size)
            print(self.heap_list)
            print("Current size: ", str(self.current_size))

        else:
            self.heap_list.append(k)
            self.current_size = self.current_size + 1
            self.perc_up(self.current_size)
            print(self.heap_list)
            print("Item inserted")
            print("Current size: ", str(self.current_size))

    def build_heap_mod(self, a_list):
        new_list = self.heap_list
        for item in a_list:
            self.insert(item)

    def del_min(self):
        ret_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.perc_down(1)
        #return ret_val
        print (self.heap_list)

H = BinHeap(8)

H.insert(5)
H.insert(9)
H.insert(4)
H.insert(6)
H.insert(3)
H.insert(12)
H.insert(13)
H.insert(1)
H.insert(7)
