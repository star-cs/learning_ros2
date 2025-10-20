import threading
import requests

class Download:

    def download(self, url, callback):
        print(f'线程的ID:{threading.get_ident()}开始下载:{url}')
        response = requests.get(url)
        response.encoding = 'utf-8'
        callback(url, response.text)

    def start_download(self, url, callback):
        # self.download(url, callback)
        threading.Thread(target=self.download, args=(url, callback)).start()

def count_word(url, result):
    print(f"{url}:{len(result)} -> {result[:5]}")

def main():
    download = Download()
    # python3 -m http.server
    download.start_download("http://0.0.0.0:8000/novel1.txt", count_word)
    download.start_download("http://0.0.0.0:8000/novel2.txt", count_word)
    download.start_download("http://0.0.0.0:8000/novel3.txt, count_word)


