a=int(input())
b=int(input())
c=int(input())
d=int(input())
jam=float(a+b+c+d)
mian=float((a+b+c+d)/4)
zarb=float(a*b*c*d)
_max=float(max(a,b,c,d))
_min=float(min(a,b,c,d))
print("Sum : "+f"{jam:.6f}\n"
      "Average : "+f"{mian:.6f}\n"
      "Product : "+f"{zarb:.6f}\n"
      "MAX : "+f"{_max:.6f}\n"
      "MIN : "+f"{_min:.6f}")
