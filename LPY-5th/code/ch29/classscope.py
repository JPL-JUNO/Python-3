X = 1


def nester():
    print(X)  # Global: 1

    class C:
        print(X)  # Global: 1

        def method1(self):  # Global: 1
            print(X)

        def method2(self):
            X = 3  # Hides global
            print(X)  # Local: 3

    I = C()
    I.method1()
    I.method2()


print(X)  # Global: 1
nester()
print("-" * 40)


X = 1


def nester():
    X = 2  # Hides global
    print(X)  # Local: 2

    class C:
        X = 3  # Class local hides nester's: C.X or I.X (not scoped)
        print(X)  # Local: 3

        # 类是一个可以访问其外层作用域的局部作用域
        # 但其本身却不能作为一个外层作用域被访问
        def method1(self):
            # 不会搜索外层的 class 语句
            # 只会搜索 def 语句
            print(X)  # In enclosing def (not 3 in class!): 2
            print(self.X)  # Inherited class local: 3

        def method2(self):
            X = 4  # Hides enclosing (nester, not class)
            print(X)  # Local: 4
            self.X = 5  # Hides class
            print(self.X)  # Located in instance: 5

    I = C()
    I.method1()
    I.method2()


print(X)  # Global: 1
nester()
print("-" * 40)

X.data1, X.__dict__["data1"]
X.data3 = "toast"
X.__dict__
X.__dict__["data3"] = "ham"
