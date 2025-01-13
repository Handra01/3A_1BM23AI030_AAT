class QueueUsingTwoStacks:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, x):
        self.stack_in.append(x)

    def dequeue(self):
        self.shift_stacks()
        if self.stack_out:
            self.stack_out.pop()

    def print_front(self):
        self.shift_stacks()
        if self.stack_out:
            print(self.stack_out[-1])

    def shift_stacks(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())


if __name__ == "__main__":
    q = QueueUsingTwoStacks()
    n = int(input())
    for i in range(n):
        command = input().strip().split()
        if command[0] == "1":
            q.enqueue(int(command[1]))
        elif command[0] == "2":
            q.dequeue()
        elif command[0] == "3":
            q.print_front()
