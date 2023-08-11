import requests

class SWAPI:
  
    """Получаем список фильмов, в которых присутствовал Дарт Вейдер"""
    def darth_vader_films(self):
        
        """Отправляем GET-запрос для получения списка фильмов"""
        darth_vader_url = 'https://swapi.dev/api/people/4/'
        response = requests.get(darth_vader_url)

        """Извлечение данных из ответа при успешном статус коде"""
        if response.status_code == 200:
            print('Успешно! Получены следующие URL фильмов:')
            darth_vader_data = response.json()
            films = darth_vader_data.get('films')
            print(films) # Получаем список URL фильмов
            return films
        else:
            print(f"Запрос к {darth_vader_url} завершился неудачно. Код статуса: {response.status_code}")
            return None
        
    """Получаем список URL персонажей, которые присутствовали в данных фильмах"""
    def character_url_names(self, films):
        """Отправляем GET-запрос для получения списка персонажей"""
        character_urls = set() 
        for film_url in films:
            response = requests.get(film_url)
            if response.status_code == 200:
                film_data = response.json()
                characters = film_data.get('characters')
                character_urls.update(characters) # Метод update не добавляет дубликаты, если они уже присутствуют в множестве
            else:
                print(f"Запрос к {film_url} завершился неудачно. Код статуса: {response.status_code}")
                return None    
        
        """Исключаем URL Дарта Вейдера, так как по условиям задачи нам нужен список персонажей, которые присутствовали вместе с Дартом Вейдером"""
        if 'https://swapi.dev/api/people/4/' in character_urls:
            character_urls.remove('https://swapi.dev/api/people/4/')
        
        print('\n' + 'Успешно! Получен следующий список URL персонажей:\n' + str(character_urls))
        return character_urls

    """Получаем список имён персонажей, которые присутствовали в данных фильмах"""
    def character_names(self, character_urls):
        names = []
        for character_url in character_urls:
            response = requests.get(character_url)
            if response.status_code == 200:
                character_data = response.json()
                name = character_data.get('name')
                names.append(name)
            else:
                print(f"Запрос к {character_url} завершился неудачно. Код статуса: {response.status_code}")
                return None
        print('\n' + 'Успешно! Получен следующий список персонажей:\n' + str(names))
        print('\n' + 'Всего было найдено персонажей: ' + str(len(names)))
        
        """Сохраняем имена персонажей в текстовый файл"""
        with open('char_names.txt', 'w', encoding='utf-8') as file:
            for name in names:
                file.write(name + '\n')
            print('\n' + 'Все имена персонажей сохранены в файл char_names.txt')
                    

'''Создаем экземпляр класса'''
swapi_dv = SWAPI()

'''Вызываем методы на созданном экземпляре'''
films_with_darth_vader = swapi_dv.darth_vader_films()
characters_with_darth_vader = swapi_dv.character_url_names(films_with_darth_vader)
names_with_darth_vader = swapi_dv.character_names(characters_with_darth_vader)