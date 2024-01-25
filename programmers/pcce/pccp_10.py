def solution(data, ext, val_ext, sort_by):
    answer = []
    dictionary = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    for d in data:
        val = d[dictionary[ext]]
        if val <= val_ext:
            answer.append(d)
    answer = sorted(answer, key=lambda item: item[dictionary[sort_by]])
    return answer


data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
ext = "date"
val_ext = 20300501
sort_by = "remain"

print(solution(data,ext,val_ext,sort_by))