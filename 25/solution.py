#         1              1
#         2              2
#         3             1=
#         4             1-
#         5             10
#         6             11
#         7             12
#         8             2=
#         9             2-
#        10             20
#        15            1=0
#        20            1-0
#      2022         1=11-2
#     12345        1-0---0
# 314159265  1121-1110-1=0

#  SNAFU  Decimal
# 1=-0-2     1747
#  12111      906
#   2=0=      198
#     21       11
#   2=01      201
#    111       31
#  20012     1257
#    112       32
#  1=-1=      353
#   1-12      107    = 2*1 + 1*5 + -1*25 + 1 * 125 = 125 - 25 + 5 + 2 = 
#     12        7    = 2*1 + 5*1 = 7
#     1=        3    =-2*1 + 1*5
#    122       37    = 1 *25   2*5 +  2*1 = 25 + 10 + 2 = 37

hash = {
  "=": -2,
  "-": -1,
  "0": 0,
  "1": 1,
  "2": 2
}

nums = open('input', 'r').read().split('\n')

def to_decimal(snafu):
  p = 1
  val = 0
  for c in range(len(snafu) - 1, -1, -1):
    char = snafu[c]
    if str(char).isnumeric():
      d = int(char)
    else:
      d = hash[char]
    val += d * p
    p = p * 5
  return val

def to_snafu(decimal):
  if not decimal:
    return ""

  val = ""

  while decimal:
    rem = decimal % 5

    if rem == 4:
      val = "-" + val
      decimal += 1
    elif rem == 3:
      val = "=" + val
      decimal += 2
    else:
      val = str(rem) + val

    decimal //= 5

  return val

print(to_snafu(sum([to_decimal(num) for num in nums])))