# https://www.acmicpc.net/problem/2229

# 문제이해 : https://blog.naver.com/PostView.nhn?blogId=occidere&logNo=221535723529
# 문제풀이 : https://nkw011.github.io/baekjoon/baekjoon-2229/

# 이게 무슨 문제에요??
# 점수가 가장 높은 학생과 낮은 학생의 차가 높을수록 좋음
# 단, 순서를 지켜야함 (나이차가 많이 나면 부정적인 영향이 있기 때문에)
# 순서를 지켜야 하기때문에 dp 문제

n = int(input())
li = list(map(int, input().split()))