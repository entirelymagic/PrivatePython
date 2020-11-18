def salut():
    print("Salut prietene!")

def before_and_after(func):
    print("Before...")
    func()
    print("after...")

before_and_after(salut)