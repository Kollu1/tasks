class Mis:
    
    def all_n_primes(self, no):
        return list(range(1, no + 1))

    # prime numbers using decorators

    def dec(func):
        def prime(num):
            if num <= 1:
                return False
            elif num == 2:
                return num
            else:
                c = 0
                for i in range(2, num + 1):
                    if num % i == 0:
                        c = c + 1
                if c == 1:
                    return num

        def primes(num):
            num = 2
            count = 0
            while count < n and num < n + 1:
                if prime(num):
                    yield num
                    count += 1
                num += 1

        def exc(num):
            try:
                if num < 0:
                    raise ValueError("Value must be positive")
                else:
                    prime_num = list(primes(n))
                    f = open('output.txt', 'w')
                    f.write(str(prime_num) + '\n')
            except ValueError as ve:
                print(f"Value Error occurred : {ve} ")
            finally:
                print("Executed using decorators")

        return exc


# prime numbers using Overriding


class Cor(Mis):
    def prime(self, num):
        if num <= 1:
            return False
        elif num == 2:
            return num
        else:
            c = 0
            for i in range(2, num + 1):
                if num % i == 0:
                    c = c + 1
                    i = i + 1
            if c == 1:
                return num

    def primes(self, num):
        num = 2
        count = 0
        while count < n and num < n + 1:
            if self.prime(num):
                yield num
                count += 1
            num += 1

    def all_n_primes(self, num):
        try:
            if n < 0:
                raise ValueError("Value must be positive")
            else:
                prime_num = list(self.primes(n))
                f = open('output.txt', 'w')
                f.write(str(prime_num) + '\n')
        except ValueError as ve:
            print(f"Value Error occurred : {ve}")
        finally:
            print("Executed using overriding")


n = int(input('Enter a number:'))
f1 = open('input.txt', 'w')
f1.write(str(n) + '\n')
x = int(input('Do you want to use decorators or overriding method?\n 1-Decorators\n 2-Overriding\n'))
if x == 1:
    Mis.all_n_primes = Mis.dec(Mis.all_n_primes)
    Mis.all_n_primes(n)
elif x == 2:
    correct = Cor()
    mistake = Mis()
    correct.all_n_primes(n)
else:
    print('Invalid Value')
