from selenium import webdriver
from Live import between


def test_scores_service():
    url = 'http://127.0.0.1:5000/'
    my_driver = webdriver.Chrome(executable_path="c:/chromedriver.exe")
    my_driver.get(url)
    my_score = int(my_driver.find_element_by_id("score").text)
    score_range = between(1, 1000, my_score)
    if score_range:
        return True
    else:
        return False


def main_function():
    test_scores_service()
    if test_scores_service():
        print("0")
    else:
        print("1")


main_function()