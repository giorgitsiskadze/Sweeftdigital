

def main():
  num_strs = int(input())
  ret =[]
  for word in range(num_strs):
    word = input()
    ret.append(bigger_Is_greater(word))

  print("\n".join(ret))


def bigger_Is_greater(w):
    w = list(w)
    # არამზარდი სუფიქსის პოვნა
    i = len(w)-1
    while i > 0 and w[i-1] >= w[i]:
        i -= 1

    if i <= 0:
        return 'no answer'

    # ყველაზე მარჯვენა მემკვიდრის პოვნა სუფიქსი დასაბრუნებლად
    j = len(w) - 1
    while w[j] <= w[i - 1]:
        j -= 1
    
    # პივოტის შეცვლა ყველაზე მარჯვენა სიმბოლოთი
    w[i-1], w[j] = w[j], w[i-1]

    # სუფიქსის შებრუნება
    w[i:] = w[len(w)-1:i-1:-1]

    return ''.join(w)
   
main()
