import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token
        self.headers = {
            'content-type': 'application/json',
            'authorization': f'OAuth {self.token}'
        }

    def upload(self, file_path: str):
        href = self._href(file_path)
        requests.put(href)

    def _href(self, file_path):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.headers
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(url, headers=headers, params=params).json()
        href = response['href']
        return href


if __name__ == '__main__':
    path_to_file = ''
    token = ''
    uploader = YaUploader(token)
    uploader.upload(path_to_file)
