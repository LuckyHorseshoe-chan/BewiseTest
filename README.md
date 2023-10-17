Тестовое задание для Bewise на позицию Python-разработчик (Junior)
Собрать образы:  
```
docker-compose up -d --build
```
Остановить/запустить образы:  
```
docker-compose stop
docker-compose start
```
Работа с API:  
Заходим по адресу http://localhost:8000/docs  
Открываем POST-запрос /questions_num, нажимаем "Try it out"  
![alt text](https://github.com/LuckyHorseshoe-chan/BewiseTest/blob/main/imgs/main.jpg)  
Вводим тело запроса, нажимаем "Execute"  
![alt text](https://github.com/LuckyHorseshoe-chan/BewiseTest/blob/main/imgs/query.jpg)  
Выводится последний вопрос из БД до выполнения запроса (после него добавляется указанное число вопросов)  
![alt text](https://github.com/LuckyHorseshoe-chan/BewiseTest/blob/main/imgs/result.jpg)  
Если ввести некорректные данные, ошибка обработается  
![alt text](https://github.com/LuckyHorseshoe-chan/BewiseTest/blob/main/imgs/bad_query.jpg)  
![alt text](https://github.com/LuckyHorseshoe-chan/BewiseTest/blob/main/imgs/format_err.jpg)  
![alt text](https://github.com/LuckyHorseshoe-chan/BewiseTest/blob/main/imgs/bad_query_2.jpg)  
![alt text](https://github.com/LuckyHorseshoe-chan/BewiseTest/blob/main/imgs/num_err.jpg)  