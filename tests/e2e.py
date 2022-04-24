from selenium import webdriver

BASE_URL = 'http://127.0.0.1:5000'
def test_scores_service(url):
    """
    its purpose is to test our web service. It will get the application
    URL as an input, open a browser to that URL, select the score element in our web page,
    check that it is a number between 1 and 1000 and return a boolean value if it’s true or not.
    :param url:
    :return: True/Falsedonhj
    """
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--disable-gpu')
    try:
        driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=options)
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get(url)
        score_element_text = driver.find_element_by_id('score').text
    except:
        print("Failed to get score element value")
        return False

    try:
        score = int(score_element_text)
    except:
        print(f'Failed to convert value to int:{score}')
        return False

    if 0 < score < 1001:
        print(f'Test passed: the score is 0 < {score} < 1001')
        return True
    else:
        print(f'Test failed : the score is NOT 0 < {score} < 1001')
        return False

if __name__ == "__main__":
    test_scores_service(BASE_URL)