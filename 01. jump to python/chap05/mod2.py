pi = 3.141592

class Math:
    level='easy'
    def solv(self,r):
        return pi*(r**2)

def sum(a,b):
    return a+b

if __name__ == '__main__':
    print(pi)
    a = Math()
    print(a.solv(2))
    print(sum(pi,4.4))