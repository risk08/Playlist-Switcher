import csv
import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.delete_all_cookies()

driver.get("https://www.google.com")

for cookie in pickle.load(open("cookies.pkl", "rb")):
     if 'expiry' in cookie:
         del cookie['expiry']
     driver.add_cookie(cookie)

songs = []

def rSpotify():
    driver.get("https://open.spotify.com/playlist/0dyWi0y1RHqZeRvRHlpoXo?si=QL4YUlhLT46mwbEfrw3u8g")
    assert "Spotify" in driver.title
    playlist_title = driver.title[10:]
    no_of_songs = int(driver.find_element_by_class_name('TrackListHeader__text-silence.TrackListHeader__entity-additional-info').text[0:2])
    for i in range(no_of_songs):
        song = []
        song_borders = driver.find_elements_by_class_name('track-name-wrapper.tracklist-top-align')[i]
        song_title = song_borders.find_element_by_class_name('tracklist-name.ellipsis-one-line')
        song_artists = song_borders.find_element_by_class_name('TrackListRow__artists.ellipsis-one-line')
        song.append(song_title.text)
        song.append(song_artists.text)
        songs.append(song)
    return playlist_title

def wCSV(songs):
    with open('playlist.csv','w',newline ='') as file:
        writer = csv.writer(file)
        writer.writerows(songs)


def wYoutube(songs, playlist_title):
    driver.get("https://music.youtube.com/library/playlists")
    click_element = driver.find_element_by_class_name('image.style-scope.ytmusic-two-row-item-renderer')
    driver.execute_script("arguments[0].click();", click_element)
    time.sleep(1)
    input_element = driver.find_element_by_class_name('input.style-scope.ytmusic-playlist-form')
    input_element.send_keys(playlist_title)

    input_element = driver.find_element_by_class_name('description-input.input.style-scope.ytmusic-playlist-form')
    input_element.send_keys('Converted by Playlist Switcher')

    click_element = driver.find_element_by_class_name('style-scope.paper-dropdown-menu')
    driver.execute_script("arguments[0].click();", click_element)
    time.sleep(1)

    click_element = driver.find_element_by_xpath("/html/body/ytmusic-dialog/paper-dialog-scrollable/div/div/ytmusic-playlist-form/paper-dropdown-menu/paper-menu-button/iron-dropdown/div/div/paper-listbox/paper-item[3]")
    driver.execute_script("arguments[0].click();", click_element)

    click_element = driver.find_element_by_class_name('submit-button.style-scope.ytmusic-playlist-form')
    driver.execute_script("arguments[0].click();", click_element)

    for j in range(len(songs)):
        if j == 0:
            click_element = driver.find_element_by_xpath('/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-nav-bar/div[2]/ytmusic-search-box/div/div[1]/paper-icon-button[1]/iron-icon')
            driver.execute_script("arguments[0].click();", click_element)
        input_element = driver.find_element_by_xpath('/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-nav-bar/div[2]/ytmusic-search-box/div/div[1]/input')
        input_element.clear()
        input_element.send_keys(songs[j][0])
        for n in range(len(songs[j])-1):
            input_element.send_keys(" ")
            input_element.send_keys(songs[j][n+1])
        input_element.send_keys("\n")
        time.sleep(1)
        try:
            click_element = driver.find_element_by_xpath('/html/body/ytmusic-app/ytmusic-app-layout/div[3]/ytmusic-search-page/ytmusic-header-renderer/ytmusic-chip-cloud-renderer/div/ytmusic-chip-cloud-chip-renderer[1]/a')
            driver.execute_script("arguments[0].click()", click_element)
            action = ActionChains(driver)
            time.sleep(1)
            action.move_to_element(driver.find_element_by_xpath('//*[@id="contents"]/ytmusic-responsive-list-item-renderer[1]')).perform()
            action.context_click().perform()
            click_element = driver.find_element_by_xpath('/html/body/ytmusic-app/ytmusic-popup-container/iron-dropdown/div/ytmusic-menu-popup-renderer/paper-listbox/ytmusic-menu-navigation-item-renderer[2]/a')
            driver.execute_script("arguments[0].click();", click_element)
            click_element = driver.find_elements_by_xpath('//*[@id="playlists"]/ytmusic-playlist-add-to-option-renderer[*]/button')
            click_element = click_element[0]
            driver.execute_script("arguments[0].click();", click_element)
        except:
            print('Song not found')
            j += 1

playlist_title = rSpotify()
wYoutube(songs, playlist_title)
driver.quit()
    
# pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))

# driver.quit()
