def word_count(sample_file):
  # 함수를 완성하세요
  """
  - def word_count(sample_file: List[str] -> dictionary
  - sorted 함수와, lambda 함수를 이용하여 딕셔너리 value 값을 내림차순 정렬하여 상위 10개 출력
  """
  lt = []
  for i in sample_file:
    words = i.strip().split(' ')
    lt.extend(words)

  dic = {}
  for i in lt:
    if i in dic:
      dic[i] += 1
    else:
      dic[i] = 1

  word_list = sorted(dic.items(), key=lambda x: x[1], reverse=True)
  print(word_list[:10])





###### do not edit here #######
with open('sample_file.txt', 'r', encoding='UTF8') as f:
  sample_file = f.readlines()

word_count_dic = word_count(sample_file)
word_count_dic