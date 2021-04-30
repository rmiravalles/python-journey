# 
# Example file for retrieving data from the internet
#

# the urllib.request defines functions and classes which help in opening URLs
import urllib.request

def main():
      webUrl = urllib.request.urlopen("http://www.google.com")
      print("result code:", str(webUrl.getcode()))
      data = webUrl.read()
      print(data)
      


if __name__ == "__main__":
  main()
