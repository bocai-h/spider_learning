from urllib.request import urlopen

if __name__ == '__main__':
  for i in range(1, 10001):
    print("i=", i)
    html = urlopen("https://nftlogo.s3.ap-southeast-1.amazonaws.com/{}.png".format(i));