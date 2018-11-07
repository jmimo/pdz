from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import links
import shutil
import re

# 237

# total of 158
START_INDEX = 1
STEP = 23


def main():
    local_index = 0
    has_error = False

    browser = webdriver.Chrome()
    browser.delete_all_cookies()

    for user in links.CLUB[START_INDEX:START_INDEX + STEP]:
        wait = WebDriverWait(browser, 10)
        browser.get(user[1])
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "table.XCinfo")))
        try:
            for element in browser.find_elements_by_tag_name('a'):
                link = str(element.get_attribute('href'))
                if 'https://www.xcontest.org/track.php?' in link:
                    element.click()
                    wait_for_download_to_finish()
                    rename_and_move(user[0], user[1], 'igc')
                if 'https://www.xcontest.org/trackmz.php?' in link:
                    element.click()
                    wait_for_download_to_finish()
                    rename_and_move(user[0], user[1], 'kmz')
        except Exception as e:
            print(e)
            print('ERROR AT INDEX: [{}:{}]'.format(START_INDEX, START_INDEX + local_index))
            print('Unable to download from: {}'.format(user))
            has_error = True
            break
        local_index += 1
        time.sleep(3)

    if not has_error:
        print('done @ [{}:{}]'.format(START_INDEX, START_INDEX + STEP))
    browser.close()


def wait_for_download_to_finish():
    seconds = 0
    dl_wait = True
    while dl_wait and seconds < 30:
        time.sleep(1)
        dl_wait = False
        for fname in os.listdir('/home/mimo/Downloads'):
            if fname.endswith('.crdownload'):
                dl_wait = True
        seconds += 1
    return seconds


def rename_and_move(user, link, file_ending):
    match = re.match('^.*detail:([a-zA-Z0-9\.\-_]*)\/([0-9]{1,2})\.([0-9]{1,2})\.([0-9]{4})', link)
    if not match:
        raise Exception("unable to match link: {}".format(link))

    filename = '{}-{:0=2d}-{:0=2d}-{}-({})'.format(match.group(4), int(match.group(3)), int(match.group(2)), user.replace(' ', '_'), match.group(1))
    for file in os.listdir('/home/mimo/Downloads'):
        file_with_path = '/home/mimo/Downloads/{}'.format(file)
        if os.path.isfile(file_with_path):
            target_file_with_path = '/home/mimo/Documents/pdz/{}.{}'.format(filename, file_ending)
            counter = 0
            while os.path.isfile(target_file_with_path):
                target_file_with_path = '/home/mimo/Documents/pdz/{}-{}.{}'.format(filename, counter, file_ending)
                counter += 1
            shutil.move(file_with_path, target_file_with_path)


if __name__ == '__main__':
    main()
