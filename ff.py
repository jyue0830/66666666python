#猜數字遊戲
sn=77 #謎底
gn=None #玩家輸入
gucount=0 #猜幾次
gulimit=3 #最多能猜幾次
outoflimil=False #有無超過猜測次數
while sn!=gn and not(outoflimil): #謎底不等於玩家輸入/有無超過次數
    gucount+=1 #每猜一次 次數加一
    if gucount<=gulimit: #如果沒超過次數 繼續猜
        gn=int(input("請輸入數字"))
        if gn>sn:
            print("smail")
        elif gn<sn:
            print("big")
    else:               #超過次數 跳出迴圈
        outoflimil=True
if outoflimil: #超過次數 
    print("you lose") #輸
else:          #猜對
    print("you win")  #贏