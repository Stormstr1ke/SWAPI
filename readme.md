Задание:
1. Протестировать следующее API https://swapi.dev/

2. Необходимо отправить запрос методом GET https://swapi.dev/api/people/4/

3. Написать код который будет сохранять имена всех персонажей, которые присутствовали в фильмах вместе с Дартом Вейдером, в текстовый файл, при этом в файле не должны содержаться дубли


Решение:
1. В ответ на запрос методом GET https://swapi.dev/api/people/4/ приходит json с информацией о том, в каких эпизодах присутсвовал сам Дарт Вейдер (массив "films"):
https://swapi.dev/api/films/1/  "A New Hope"
https://swapi.dev/api/films/2/  "The Empire Strikes Back"
https://swapi.dev/api/films/3/  "Return of the Jedi"
https://swapi.dev/api/films/6/  "Revenge of the Sith"

2. Отправив запрос методом GET по каждому из этих URL по очереди получаем json с информацией о том, какие персонажи присутствовали в данных эпизодах

3. Данная информация содержится в массиве "characters", в котором указан список URL на каждого персонажа, присутствующего в каждом из интересующих нас фильмов

4. Убрать дубли и самого Дарта Вейдера

5. После отправки запросов методом GET по каждому из оставшихся URL по очереди получаем json с информацией об имени каждого персонажа, которая указана в поле "name"

6. Сохраняем данные имена в текстовый файл

