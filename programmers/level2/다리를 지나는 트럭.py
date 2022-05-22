# 참고해서 푼 문제
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    
    while bridge:
        
        answer += 1 # 경과 시간
        bridge.pop(0)
        
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0) # 다리의 길이 유지하기 위해
        
        # print(bridge)
    
    return answer