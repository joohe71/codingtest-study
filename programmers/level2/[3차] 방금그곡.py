# 시간 변환 함수
def Time(t):
    h,m = t.split(":")
    return int(h) * 60 + int(m)

# '#'이 붙은 음을 소문자로 변환하는 함수
def change(music):
    if 'A#' in music:
        music = music.replace('A#', 'a')
    if 'F#' in music:
        music = music.replace('F#', 'f')
    if 'C#' in music:
        music = music.replace('C#', 'c')
    if 'G#' in music:
        music = music.replace('G#', 'g')
    if 'D#' in music:
        music = music.replace('D#', 'd')
    return music

def solution(m, musicinfos):
    answer = []
    for index,i in enumerate(musicinfos):
        
        intime, outtime, name, music = i.split(",")
        # 시간계산
        time = Time(outtime) - Time(intime)
        # 재생 시간에 따른 음
        music = change(music) * (time//len(change(music))) + change(music)[:time%len(change(music))]
        
        # 기억한 멜로디도 # 제거
        m = change(m)
    
        if m in music:
            answer.append([time, index, name])
    
    if not answer:
        return "(None)"
    elif len(answer) == 1:
        return answer[0][2]
    
    # 결과 배열의 크기가 2보다 크다면 재생된 시간이 긴 음악, 먼저 입력된 음악순으로 정렬
    else:
        answer = sorted(answer, key=lambda x: (-x[0], x[1]))
        return answer[0][2] # 첫번째 제목을 리턴