import hashlib
import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hashlib.sha256(password.encode()).hexdigest()
        self.age = age


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        for user in self.users:
            if user.nickname == nickname and user.password == password_hash:
                self.current_user = user
                print(f"Вход выполнен как {nickname}")
                return
        print("Неверный логин или пароль")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        print(f"Пользователь {nickname} успешно зарегистрирован!")
        self.current_user = new_user
        return

    def log_out(self):
        self.current_user = None
        print("Выход из системы.")

    def add(self, *videos):
        for video in videos:
            if not any(v.title.lower() == video.title.lower() for v in self.videos):
                self.videos.append(video)
                print('Видео добавлено')

    def get_videos(self, search_query):
        search_result = []
        print('Найденные фильмы:')
        for i in self.videos:
            if search_query.lower() in i.title.lower():
                search_result.append(i.title)
        return search_result

    def watch_video(self, search_query):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for i in self.videos:
            if search_query == i.title:
                if i.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
                for j in range(i.time_now + 1, i.duration + 1):
                    print(f"Просмотр '{i.title}' - {j} секунда")
                    time.sleep(1)
                    i.time_now = j
                print('Конец видео')
                i.time_now = 0


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)

print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user.nickname)
ur.watch_video('Лучший язык программирования 2024 года!')
