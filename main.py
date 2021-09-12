# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]


print(f"{row1}\n{row2}\n{row3}")
p= input("Where do you want to put the treasure? (mark as 'xy'):")

a=int((int(p)%10)-1)
b=int(int(p[0])-1)
#print(a,b)
map[b][a]="X"
print(f"{row1}\n{row2}\n{row3}")