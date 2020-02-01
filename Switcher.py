import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://open.spotify.com/playlist/0dyWi0y1RHqZeRvRHlpoXo?si=QL4YUlhLT46mwbEfrw3u8g")
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

print(songs)

with open('playlist.csv','w',newline='') as file:
    writer = csv.writer(file)
    writer.writerows(songs)

##driver.get("https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3D%252F&hl=en&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
##try:
##    element = WebDriverWait(driver, 60).until(
##        EC.presence_of_element_located((By.ID, "avatar-btn"))
##    )
##    print("success")
##finally:
##    driver.quit()

driver.quit()
