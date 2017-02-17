import re
def findCreditCard(raw):
    americanRE = re.findall("3[47][0-9]{13}",raw)
    if americanRE:
        print "[+] Found American Express Card:"+americanRE[0]
def main():
    tests = []
    tests.append('I would like to buy 1337 copies if that dvd')
    tests.append('Bill my card:378282246310005 for \$2600')
    for test in tests:
        findCreditCard(test)
if __name__ == '__main__':
    main()