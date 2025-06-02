# Solution for https://coderun.yandex.ru/problem/sorting-reverse-order
# Other solutions: https://github.com/Melodiz/CodeRun

from urllib.request import urlopen
import json

def main():
    server_url = input()
    port = int(input())
    a = int(input())
    b = int(input())

    url = "%s:%s?a=%s&b=%s" % (server_url, port, a, b)
    data = json.loads(urlopen(url).read())
    print("\n".join(map(str, filter(lambda x : x > 0, sorted(data, reverse = True)))))

if __name__ == "__main__":
    main()
