n = int(input())
st = set()

for i in range(n):
    a = input()

    for d in a:
        st.add(d)

print(len(st))
