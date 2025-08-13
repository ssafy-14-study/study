def pattern_lps(pattern):
    #패턴의 LPS 생성
    lps = [0] * len(pattern)
    length = 0  # 현재까지 일치한 접두사 길이

    for i in range(1, len(pattern)):
        while length > 0 and pattern[i] != pattern[length]:
            length = lps[length - 1]
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
    return lps

def kmp_search(text, pattern):
    #패턴이 시작되는 모든 위치 반환
    if not pattern:
        return []
    lps = pattern_lps(pattern)
    match_starts = []
    j = 0  # 패턴 인덱스

    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]
        if text[i] == pattern[j]:
            j += 1
            if j == len(pattern):
                match_starts.append(i - len(pattern) + 1)
                j = lps[j - 1]
    return match_starts

T = int(input())
for case_num in range(1, T + 1):
    text, pattern = input().split()

    # KMP로 모든 매치 시작 위치 찾기
    match_starts = kmp_search(text, pattern)

    # 겹치지 않게 최대 매치 선택
    match_count = 0
    last_end_index = -1
    pattern_len = len(pattern)

    for start_index in match_starts:
        if start_index >= last_end_index:
            match_count += 1
            last_end_index = start_index + pattern_len

    # 최소 키 입력 횟수 계산
    min_key = len(text) - match_count * (pattern_len - 1)

    print(f"#{case_num} {min_key}")
