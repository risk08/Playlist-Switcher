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

   
for i in range(no_of_songs):
    song = []
    song_borders = driver.find_elements_by_class_name('track-name-wrapper.tracklist-top-align')[i]
    song_title = song_borders.find_element_by_class_name('tracklist-name.ellipsis-one-line')
    song_artists = song_borders.find_element_by_class_name('TrackListRow__artists.ellipsis-one-line')
    song.append(song_title.text)
    song.append(song_artists.text)
    songs.append(song)

with open('playlist.csv','w',newline ='') as file:
    writer = csv.writer(file)
    writer.writerows(songs)



driver.get("https://music.youtube.com/library/playlists")
driver.implicitly_wait(1)
click_element = driver.find_element_by_class_name('image.style-scope.ytmusic-two-row-item-renderer')
driver.execute_script("arguments[0].click();", click_element)
driver.implicitly_wait(1)
# driver.execute_script("arguments[0].click();", click_element)
# driver.execute_script("arguments[0].click();", click_element)
# driver.implicitly_wait(5)
input_element = driver.find_element_by_class_name('input.style-scope.ytmusic-playlist-form')
input_element.send_keys(playlist_title)

input_element = driver.find_element_by_class_name('description-input.input.style-scope.ytmusic-playlist-form')
input_element.send_keys('Converted by Playlist Switcher')

click_element = driver.find_element_by_class_name('style-scope.paper-dropdown-menu')
driver.execute_script("arguments[0].click();", click_element)
driver.implicitly_wait(1)

click_element = driver.find_element_by_xpath("/html/body/ytmusic-dialog/paper-dialog-scrollable/div/div/ytmusic-playlist-form/paper-dropdown-menu/paper-menu-button/iron-dropdown/div/div/paper-listbox/paper-item[3]")
driver.execute_script("arguments[0].click();", click_element)

click_element = driver.find_element_by_class_name('submit-button.style-scope.ytmusic-playlist-form')
driver.execute_script("arguments[0].click();", click_element)
driver.implicitly_wait(1)

for j in range(len(songs)):
    click_element = driver.find_element_by_xpath('/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-nav-bar/div[2]/ytmusic-search-box/div/div[1]/paper-icon-button[1]/iron-icon')
    driver.execute_script("arguments[0].click();", click_element)
    input_element = driver.find_element_by_xpath('/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-nav-bar/div[2]/ytmusic-search-box/div/div[1]/input')
    input_element.clear()
    input_element.send_keys(songs[j][0])
    for n in range(len(songs[j])):
        input_element.send_keys(" ")
        input_element.send_keys(songs[j][n])
    input_element.send_keys("\n")
    driver.implicitly_wait(1)
    
# input_element = driver.find_element_by_class_name('style-scope.iron-autogrow-textarea')
# input_element.send_keys('Convertion by Playlist Switcher')
# pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))

# driver.quit()
