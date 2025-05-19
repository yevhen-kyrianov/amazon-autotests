

# import playwright
# from playwright.sync_api import sync_playwright


# page = "www.google.com"
# browser = None
# context = None

# def start_browser():
#     global browser, context
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         context = browser.new_context()
#         page = context.new_page()
#         page.goto("https://www.google.com")
#         return page

# def hi_li():
#     page = start_browser()
#     items = page.locator("button[id='hyperlink']").all_text_contents
#     page.close()
#     return items

# hyp_links = hi_li()

# def go_to_links(link):
#     global page
#     page.goto(link)
#     return page.locator("h1").text_content()

# for item in hyp_links:
#     print(item)
    
#     print(page)
#     page.close()
    

# word = "america"

# print(word.count('a')) # A




page = "www.amazon.com"
page.scroll_to_bottom()


string = "level"

if string == string.reverse():
    print("The string is a palindrome")