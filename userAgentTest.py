import mechanize
def testUserAgent(url,userAgent):
    browser = mechanize.Browser()
    browser.addheaders = userAgent
    page = browser.open(url)
    source_code = page.read()
    print source_code
url = 'http://whatismyuseragent.dotdoh.cpm/'
useraAgent = [('User-agent','Mozilla/5.0 (X11;U;'+'Linux 2.4.2-2 i586;en-US;m18' Gecok/20010131 Netscaoe6/6.01)]
testUserAgent(url,userAgent)