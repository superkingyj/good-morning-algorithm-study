from sys import stdin
import heapq


def solution(n):
    student = {}
    data = list(map(int, stdin.readline().split()))
    for s in data:
        if s not in student:
            if len(student) >= n:
                a = heapq.nsmallest(min(student), student, key=student.get)
                student.pop(a[0])

            student[s] = 1
        else:
            student[s] += 1

    return sorted(student.keys())


n = int(stdin.readline().rstrip())
r = int(stdin.readline().rstrip())
print(*solution(n))