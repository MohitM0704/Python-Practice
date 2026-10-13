coding = set()
sports = set()
music = set()
print("Interested for coding")
for i in range(1,4):
    code = input("Enter your name: ")
    coding.add(code)

print("\n--------------")
print("Interested for sports")
for j in range(1,4):
    spo = input("Enter your name: ")
    sports.add(spo)

print("\n--------------")
print("Interested for music")
for k in range(1,4):
    mus = input("Enter your name: ")
    music.add(mus)

print("\n---------------")
print(f"Students interested for both coding and sports: \n{coding.intersection(sports)}")
print(f"Students only intersted in Music: \n{music.difference(coding.union(sports))}")
print(f"Students interested in any club: \n{coding.union(sports.union(music))}")
print(f"Count of unique students: {len(coding.union(sports.union(music)))}")