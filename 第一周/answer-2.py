def c_to_f(c):
    return c * 1.8 + 32

c = 39
f = c_to_f(c)
print("摄氏度%.2f转换成华氏度为：%.2f"
      % (c, f))
