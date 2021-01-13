import re
def solution(s):
  answer = False
  if len(s) == 4 or len(s) ==(6):  
    re_s = re.sub('[^0-9]', '', s)      
    if re_s == s:
      answer = True
  return answer