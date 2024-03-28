class MaxHeap:

    def __init__(self):
        self.data = [None]


    def insert(self, item):
        self.data.append(item)
        if len(self.data) == 2:
            return
        now = len(self.data)-1
        parent = now // 2
        if self.data[parent] < self.data[now]:
            while (parent > 0) and (self.data[parent] < self.data[now]):
                self.data[parent], self.data[now] = self.data[now], self.data[parent]
                now = parent
                parent = now // 2

    def remove(self):
        if len(self.data) > 1:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop(-1)
            self.maxHeapify(1)
        else:
            data = None
        return data

    def maxHeapify(self, i):
        # 왼쪽 자식 (left child) 의 인덱스를 계산합니다.
        left =2 * i

        # 오른쪽 자식 (right child) 의 인덱스를 계산합니다.
        right =2 * i + 1
        smallest = i
        # 왼쪽 자식이 존재하는지, 그리고 왼쪽 자식의 (키) 값이 (무엇보다?) 더 큰지를 판단합니다.
        if right < len(self.data) and self.data[left] > self.data[right]:
        # 조건이 만족하는 경우, smallest 는 왼쪽 자식의 인덱스를 가집니다.
            smallest = left

        # 오른쪽 자식이 존재하는지, 그리고 오른쪽 자식의 (키) 값이 (무엇보다?) 더 큰지를 판단합니다.
        if right < len(self.data) and self.data[left] < self.data[right]:
            # 조건이 만족하는 경우, smallest 는 오른쪽 자식의 인덱스를 가집니다.
            smallest = right
        if smallest != i:
        # 현재 노드 (인덱스 i) 와 최댓값 노드 (왼쪽 아니면 오른쪽 자식) 를 교체합니다.
            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]

        # 재귀적 호출을 이용하여 최대 힙의 성질을 만족할 때까지 트리를 정리합니다.
            self.maxHeapify(smallest)

heap = MaxHeap()
heap.insert(3)
heap.insert(10)
heap.insert(4)
print(heap.data)
print(heap.remove())
print(heap.remove())
print(heap.remove())