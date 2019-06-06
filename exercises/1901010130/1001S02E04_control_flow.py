for i in range(1,10):
    for j in range(1,10):
        print(j,"x",i,"=",i*j,"\t",end="")  # 如果去掉 end=""，那么每一次打印后都要换行
        if i==j:
            print("hh")
            break
