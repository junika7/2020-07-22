class C:
    def __init__(self): #대화형 모드에서 import a 후 c = a.C()
        print("class C의 인스턴스가 생성됨")
        self.name = "ccc"
        self.age = 0

    def say_hi(self): #c.say_hi()
        print("hi")

    def add_age(self, n: int): #c.add_age(5)
        self.age += n

    def __str__(self): #print 함수에서 호출되는 부분 print(c)
        return "__str__ 호출됨"

    def __repr__(self): #대화형 모드에서 그냥 호출되는 부분 c
        return "__repr__ 호출됨"

    def __abs__(self): #abs(c): abs라는 내장함수 실행 시 이 부분이 실행
        print("__abs__ 호출됨")

    def __len__(self): #len(c): len라는 내장함수 실행 시 이 부분이 실행 
        print("__len__ 호출됨")

    def __add__(self, other): #c1 + c2 가능
        return self.age + other.age
