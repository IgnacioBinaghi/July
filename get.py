import requests
from bs4 import BeautifulSoup
import sys
import time

def progress_bar(progress, total, start_time):
    bar_length = 50
    try:
        filled_length = int(round(bar_length * progress / float(total)))
    except:
        filled_length = int(round(bar_length * 1 / float(total)))
    percents = round(100.0 * progress / float(total), 1)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    elapsed_time = time.time() - start_time
    if progress > 0:
        estimated_total_time = elapsed_time * total / progress
        remaining_time = estimated_total_time - elapsed_time
        eta_time = time.localtime(time.time() + remaining_time)
        eta_str = time.strftime('%I:%M:%S %p', eta_time)
        hours, remainder = divmod(remaining_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        if hours > 0:
            eta = f'{int(hours)}h {int(minutes)}m'
        elif minutes > 0:
            eta = f'{int(minutes)}m {int(seconds)}s'
        else:
            eta = f'{int(seconds)}s'
        sys.stdout.write(f'\r[{bar}] {percents}% | ETA: {eta} ({eta_str}) ')
    else:
        sys.stdout.write(f'\r[{bar}] {percents}% ')
    sys.stdout.flush()


def get_stats(usernames):

    users = []
    count = 0
    start_time = time.time()
    
    for username in usernames:

        progress_bar(count, len(usernames), start_time)


        url = 'https://www.tiktok.com/@'+username

        page = requests.get(url)

        soup = BeautifulSoup(page.content, 'html.parser')

        results = soup.find(id = 'main-content-others_homepage')

        try:
            elements = results.find_all("div", class_="css-1ic15oa-H2ShareDesc e1457k4r3")

            try:
                html = results.find_all(attrs={'class': 'tiktok-vdfu13-H2ShareDesc'})

                soup = BeautifulSoup(str(html), 'html.parser')

                text = soup.get_text()

                bio = text[1:-1]
            except:
                bio = ''


            html = results.find_all(attrs={'class': 'tiktok-rxe1eo-DivNumber e1457k4r1'})
            soup = BeautifulSoup(str(html), 'html.parser')

            try:
                followers = soup.find('strong', {'data-e2e': 'followers-count'}).text
            except:
                continue

            
            html = results.find_all(attrs={'class': 'tiktok-847r2g-SpanLink eht0fek2'})
            soup = BeautifulSoup(str(html), 'html.parser')

            try:
                link = soup.find('span', {'class': 'tiktok-847r2g-SpanLink'}).text
            except:
                link = ''


            user = [username, followers, bio, link]

            users.append(user)
        except:
            pass

        count+=1

    progress_bar(len(usernames), len(usernames), start_time)
    print('\nAccount Data Retrieval Successful')

    return users