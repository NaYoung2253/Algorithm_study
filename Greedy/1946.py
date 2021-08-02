import sys

T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    applicant = []
    
    for i in range(N):
        grade = list(map(int, sys.stdin.readline().split()))
        applicant.append(grade)

    sort_apply = sorted(applicant)
    first = sort_apply[0][1]
    
    cnt = 1
    for i in range(1, N):
        if first > sort_apply[i][1]:
            cnt += 1
            first = sort_apply[i][1]

    print(cnt)