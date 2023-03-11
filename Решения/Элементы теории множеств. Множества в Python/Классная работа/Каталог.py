n = int(input())
st = set()

for i in range(n):
    s = input()

    if s in st:
        print("ДА")
    else:
        print("НЕТ")

    st.add(s)
