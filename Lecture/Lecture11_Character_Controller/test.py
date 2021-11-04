
class Star:
    type = 'Star'
    x=100

    # 파이썬 코드에서 생성자는 꼭 있어야 하는가? ( X )

    def change():
        x=200
        print('x is ', x)


print('x IS ',Star.x) #OK
Star.change() # OK
print('x IS ', Star.x)

star = Star() # OK
print('x IS ', star.x) # Ok
star.change() # Error

 # 파이썬은 그 자체가 포인터다.