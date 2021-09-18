# NESTRO TECH 2021
*СИСТЕМА МОНИТОРИНГА УСТОЙЧИВОСТИ РАБОЧИХ ПРОЦЕССОВ и КОМПОНЕНТОВ*

Прототип системы мониторинга устойчивости рабочих процессов и компонентов.

Программное решение кейса от команды "NESTRO TECH" (АО "Зарубежнефть"), реализованого в рамках [IT-чемпионата нефтяной отрасли 2021](https://it-oilchamp.ru/)

Прототип системы доступен по адресу **http://dh.bitc.ru:8021/** до 3.10.2021 г.
>  доступ к панели администратора возможен после авторизации
>
> имя пользователя и пароль администратора можно получить у капитана команды NESTRO TECH

Класс графа устройчивости - **\monstability\visstability\grstead.py**

Для инсталляции необходимо клонировать репозиторий, собрать образ и запустить контейнер
```
git clone https://github.com/DmitriyMishanin/NESTRO_TECH_2021.git
cd NESTRO_TECH_2021
docker-compose build
docker-compose up -d
```
> требует docker и доступного контейнера PostgreSQL на порту 5432

*Описание графа устойчивости*

* Граф устойчивости направленный.
* Обход графа начинается с узлов метрик.
* Ребра имеют веса.
* Узлы типа 'metric', 'service', 'true' могут иметь только одно входящее ребро

* Атрибуты графа устойчивости:*
* Атрибуты узла графа:

        'type':string - тип узла

            'metric' - узел метрики
            
            'service' - узел сервиса
            
            'true' - узел единичной функции (доступность всегда 1)
            
            'and' - узел логического И
            
            'or' - улел логического ИЛИ
            
        'layer' - бизнес-слой узла графа
         
        'access':integer - текущая доступность
        
        'stead':float - текущая устойчивость
        
        'costdown':float - текущая стоимость простоя        

* Атрибуты ребра графа:

        'weight':float - вес ребра (коэффициент передачи)
    
