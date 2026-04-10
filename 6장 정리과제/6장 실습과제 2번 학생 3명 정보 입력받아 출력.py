'''
주석문달기
요구사항: 3명 학생의 이름, 국,영,수 점수를 입력받아 list변수에
저장하기(중첩리스트와 반복구조 사용)
화면에 아래와 같이 서식을 갖춰서 출력하기(평균값은 소수점1자리까지 표시)
'''

students_data = []
student_Num = 3
SUBJECTS = ['국어', '영어', '수학']

#과목별 총합
total_kor = 0
total_eng = 0
total_math = 0

print("=== 학생 3명의 성적을 입력하세요 ===")

# for 반복문을 사용하여 3명의 데이터를 효율적으로 입력받음
for i in range(student_Num):
    print(f"\n--- {i+1}번째 학생 정보 입력 ---")
    name = input("이름을 입력해주세요: ")
    
    scores = []
    total_score = 0
    for j in SUBJECTS :
        score = int(input(f"{j} 점수를 입력해주세요 : "))
        scores.append(score)
        total_score += score
        
    # 총점 및 평균 계산
    avg = total_score / len(SUBJECTS)
    
    # [이름, 국어, 영어, 수학, 총점, 평균] 순서로 중첩 리스트에 추가
    s_recode = []
    s_recode.append(name)
    s_recode.append(scores[0])
    s_recode.append(scores[1])
    s_recode.append(scores[2])
    s_recode.append(total_score)
    s_recode.append(avg)
    total_kor += scores[0]
    total_eng += scores[1]
    total_math += scores[2]
    students_data.append(s_recode)


#과목별 평균
kor_avg = total_kor/student_Num
eng_avg = total_eng/student_Num
math_avg = total_math/student_Num




# 헤더 출력
print("\n" + "="*64)
# %-5s: 왼쪽 정렬 5자리 문자열, %5s: 오른쪽 정렬 5자리 문자열
print("%8s%6s%6s%6s%6s%10s" % ("성명", "국어", "영어", "수학", "총점", "평균"))
print("-" * 64)


for s in students_data :
    name = s[0]
    kor = s[1]
    eng = s[2]
    math = s[3]
    total = s[4]
    avg = s[5]
    print("%8s%6d%6d%6d%6d%10.1f" % (name, kor, eng, math, total, avg))

    
print("="*64)
print("%8s%6d/%.1f%6d/%.1f%6d/%.1f" % ("총점/평균 ", total_kor, kor_avg,total_eng, eng_avg, total_math, math_avg ))
