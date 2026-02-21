n = int(input("Enter number of songs: "))
data = [0] * n
dup = False
total = 0

for i in range(n):
    data[i] = int(input())
    if data[i] <= 0:
        print("Invalid Playlist")
        break
    total += data[i]

else:
    # duplicate check
    for i in range(n):
        for j in range(i + 1, n):
            if data[i] == data[j]:
                dup = True
                break
        if dup:
            break

    print("Total Duration:", total, "seconds")
    print("Songs:", n)

    if total < 300:
        print("Category: Too Short Playlist")
        print("Recommendation: Add more songs")

    elif total > 3600:
        print("Category: Too Long Playlist")
        print("Recommendation: Take a break")

    elif dup:
        print("Category: Repetitive Playlist")
        print("Recommendation: Add variety")

    elif (max(data) - min(data)) <= 600:
        print("Category: Balanced Playlist")
        print("Recommendation: Good listening session")

    else:
        print("Category: Irregular Playlist")
        print("Recommendation: Work on song selection")