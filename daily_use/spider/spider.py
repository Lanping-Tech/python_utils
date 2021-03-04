from selenium import webdriver
from bs4 import BeautifulSoup

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('executable_path = config/chromedriver')

chrome_driver = 'config/chromedriver'  #chromedriver的文件位置
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path = chrome_driver)

driver.get('https://i.snssdk.com/ugc/hotboard_fe/hot_list/template/hot_list/forum_tab.html')
# driver.refresh()
#time.sleep(0.01)
driver.maximize_window()
driver.execute_script(
    """
    (function () {
      var y = 0;
      var step = 100;
      window.scroll(0, 0);

      function f() {
        if (y < (document.body.scrollHeight)/5) {
          y += step;
          window.scroll(0, y);
          setTimeout(f, 100);
        } else {
          window.scroll(0, 0);   //滑动到顶部
          document.title += "scroll-done";
        }
      }
      setTimeout(f, 1000);
    })();
    """
)
sleep(5)
# 模拟点击
ActionChains(driver).move_to_element(driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div/div/div/div[8]/div[1]/div/div[13]')).click().perform()
driver.execute_script(
    """
    (function () {
      var y = 0;
      var step = 100;
      window.scroll(0, 0);

      function f() {
        if (y < (document.body.scrollHeight)/5) {
          y += step;
          window.scroll(0, y);
          setTimeout(f, 100);
        } else {
          window.scroll(0, 0);   //滑动到顶部
          document.title += "scroll-done";
        }
      }
      setTimeout(f, 1000);
    })();
    """
)
sleep(5)
soup = BeautifulSoup(driver.page_source, "html.parser")
soup.find_all("a", class_="url")


#打印数据内容
print(driver.page_source)