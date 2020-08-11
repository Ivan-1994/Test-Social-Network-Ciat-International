import requests, random, json
from time import sleep

class Bot:
    post = {"description": "123 231"}
    params = {}
    users = []
    tokens = []
    link_post_like = []

    def load_params(self):
        with open('params.json') as f:
            params = f.read()
        self.params = json.loads(params)

    def generate_users(self):
        count = self.params['number_of_users']
        for i in range(0, count):
            self.users.append({"username": f"user{i}", "password": "qazwsxedc12"})

    def create_user(self):
        for user in self.users:
            sleep(0.2)
            requests.post('http://127.0.0.1:8000/user/create/', data = user)
            sleep(0.2)
            self.tokens.append(requests.post('http://127.0.0.1:8000/user/login/', data = user).json()['token'])

    def create_post(self):
        for token in self.tokens:
            headers = {
                'Authorization': 'Token ' + token,
                'Content-Type': 'application/json',
            }
            for dont_use in range(0, random.randint(1, self.params['max_posts_per_user'])):
                sleep(0.2)
                r = requests.post('http://127.0.0.1:8000/post/create/', json = self.post, headers=headers)
                self.link_post_like.append(r.json()['Like_This'])

    def like_post(self):
        for token in self.tokens:
            headers = {
                'Authorization': 'Token ' + token,
                'Content-Type': 'application/json',
            }
            likes = []
            start_count = int(self.params['max_likes_per_user']/2)
            for dont_use in range(0, random.randint(start_count, self.params['max_likes_per_user'])):
                while True:
                    link_post = self.link_post_like[random.randint(0, len(self.link_post_like)-1)]
                    if link_post in likes:
                        continue
                    else:
                        sleep(0.2)
                        requests.put(link_post, headers=headers)
                        likes.append(link_post)
                        break

if __name__ == '__main__':
    bot = Bot()
    bot.load_params()
    bot.generate_users()
    bot.create_user()
    bot.create_post()
    bot.like_post()
