class calculator():
    def __init__(self, number):
        self.number = number
        self.num1 = int(number[0])
        self.num2 = int(number[1])
        self.num3 = int(number[2])
        self.num4 = int(number[3])
        self.num5 = int(number[4])
        self.sum_result = 0
        self.count_num = len(self.number)

    def sum(self):
        self.sum_result = self.num1+self.num2+self.num3+self.num4+self.num5
        print(self.sum_result)
        return self.sum_result

    def avg(self):
        dis = self.sum_result / self.count_num
        print(dis)
        return dis

if __name__ == '__main__':
    cal1 = calculator([1,2,3,4,5])
    cal1.sum()
    cal1.avg()

    cal2 = calculator([6,7,8,9,10])
    cal2.sum()
    cal2.avg()
