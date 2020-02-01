import csv
import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.delete_all_cookies()
driver.get("https://open.spotify.com/playlist/0dyWi0y1RHqZeRvRHlpoXo?si=QL4YUlhLT46mwbEfrw3u8g")
for cookie in pickle.load(open("cookies.pkl", "rb")):
     if 'expiry' in cookie:
         del cookie['expiry']
     driver.add_cookie(cookie)
assert "Spotify" in driver.title
playlist_title = driver.title[10:]
no_of_songs = int(driver.find_element_by_class_name('TrackListHeader__text-silence.TrackListHeader__entity-additional-info').text[0:2])
songs = []

##for i in range(no_of_songs):
##    song = []
##    writer = csv.writer(file)
##    writer.writerows(songs)

driver.get("https://www.youtube.com")
##pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
try:
    element = WebDriverWait(driver, 800).until(
        EC.presence_of_element_located((By.ID, "avatar-btn"))
    )
    print("success")
finally:
    driver.quit()

driver.quit()
