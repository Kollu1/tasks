class task:
    def __init__(self, inp_list, x):
        self.inp_list = inp_list
        self.x = x

    def pro(self):
        try:
            dict = {}
            for i in self.inp_list:
                count = 0
                for j in self.inp_list:
                    if i == j:
                        count += 1
                    else:
                        j = j + 1
                dict.update({i: count})
            f = open('output.txt', 'w')
            f.write(str(dict) + '\n')

            def div(ls, x):
                for i in ls:
                    yield i / x

            y = list(div(self.inp_list, self.x))
            f = open('output.txt', 'a')
            f.write(str(y) + '\n')
        except Exception as e:
            print(f"A number cannot be divided by zero! :{e}")
        finally:
            print("execution completed")


inp_list = list(map(int, input('Enter numbers:').split()))
x = int(input('Enter a number:'))
f1 = open('input.txt', 'w')
f1.write(str(inp_list) + '\n')
f1.write(str(x) + '\n')
run_task = task(inp_list, x)
run_task.pro()
