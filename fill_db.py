import sqlite3
from db_scripts import *

def populate_quiz_database():
    """Заполняет базу данных 5 викторинами с 15 вопросами в каждой"""
    
    # Очищаем и создаем базу данных
    clear_db()
    create()
    
    # Данные для 5 викторин (название, возраст_от, возраст_до)
    quizes = [
        ("Детская викторина", 6, 10),
        ("Школьная викторина", 11, 14), 
        ("Подростковая викторина", 15, 17),
        ("Молодежная викторина", 18, 25),
        ("Взрослая викторина", 26, 50)
    ]
    
    # Добавляем викторины
    open_db()
    query = "INSERT INTO quiz (name, from_age, to_age) VALUES (?,?,?)"
    do_many(query, quizes)
    close_db()
    
    # Подготавливаем 75 вопросов (15 для каждой викторины)
    questions = []
    
    # Вопросы для детской викторины (6-10 лет)
    children_questions = [
        ("Сколько лап у собаки?", "4", "2", "6", "8"),
        ("Какого цвета солнце?", "Желтое", "Синее", "Зеленое", "Красное"),
        ("Сколько дней в неделе?", "7", "5", "6", "8"),
        ("Что едят коровы?", "Траву", "Мясо", "Рыбу", "Конфеты"),
        ("Сколько пальцев на руке?", "5", "4", "6", "10"),
        ("Какое животное мяукает?", "Кот", "Собака", "Корова", "Лошадь"),
        ("Из чего делают хлеб?", "Из муки", "Из песка", "Из воды", "Из камня"),
        ("Когда идет дождь, небо какое?", "Серое", "Зеленое", "Красное", "Фиолетовое"),
        ("Сколько времен года?", "4", "3", "5", "2"),
        ("Что нужно делать перед едой?", "Мыть руки", "Бегать", "Спать", "Петь"),
        ("Какой формы мяч?", "Круглый", "Квадратный", "Треугольный", "Плоский"),
        ("Где живут рыбы?", "В воде", "На дереве", "В песке", "В небе"),
        ("Что светит ночью?", "Луна", "Солнце", "Лампочка", "Свеча"),
        ("Сколько глаз у человека?", "2", "1", "3", "4"),
        ("Какого цвета трава?", "Зеленая", "Синяя", "Красная", "Черная")
    ]
    
    # Вопросы для школьной викторины (11-14 лет)
    school_questions = [
        ("Столица России?", "Москва", "Санкт-Петербург", "Казань", "Новосибирск"),
        ("Сколько планет в солнечной системе?", "8", "7", "9", "10"),
        ("Кто написал 'Война и мир'?", "Толстой", "Пушкин", "Достоевский", "Чехов"),
        ("Сколько континентов на Земле?", "7", "5", "6", "8"),
        ("Какой газ мы вдыхаем?", "Кислород", "Углекислый газ", "Азот", "Водород"),
        ("В каком году началась Вторая мировая война?", "1939", "1940", "1938", "1941"),
        ("Самая длинная река в мире?", "Нил", "Амазонка", "Волга", "Енисей"),
        ("Сколько букв в русском алфавите?", "33", "32", "34", "31"),
        ("Что изучает биология?", "Жизнь", "Звезды", "Числа", "Языки"),
        ("Какой океан самый большой?", "Тихий", "Атлантический", "Индийский", "Северный Ледовитый"),
        ("Сколько сторон у треугольника?", "3", "4", "5", "6"),
        ("Кто открыл Америку?", "Колумб", "Магеллан", "Кук", "Васко да Гама"),
        ("Какая планета ближайшая к Солнцу?", "Меркурий", "Венера", "Земля", "Марс"),
        ("Сколько секунд в минуте?", "60", "50", "70", "100"),
        ("Что такое H2O?", "Вода", "Кислород", "Водород", "Соль")
    ]
    
    # Вопросы для подростковой викторины (15-17 лет)
    teen_questions = [
        ("Кто создал теорию относительности?", "Эйнштейн", "Ньютон", "Галилей", "Дарвин"),
        ("В каком году пал Берлин?", "1989", "1987", "1990", "1988"),
        ("Что означает аббревиатура ДНК?", "Дезоксирибонуклеиновая кислота", "Диоксид азота", "Дигидроксид калия", "Динитрат кальция"),
        ("Кто написал 'Гамлет'?", "Шекспир", "Байрон", "Мильтон", "Диккенс"),
        ("Какой элемент имеет символ Au?", "Золото", "Серебро", "Медь", "Железо"),
        ("Сколько хромосом у человека?", "46", "44", "48", "50"),
        ("В каком году началась Первая мировая война?", "1914", "1913", "1915", "1916"),
        ("Что изучает астрономия?", "Космос", "Атомы", "Растения", "Животных"),
        ("Кто автор картины 'Звездная ночь'?", "Ван Гог", "Пикассо", "Моне", "Дали"),
        ("Какая скорость света?", "300000 км/с", "150000 км/с", "450000 км/с", "600000 км/с"),
        ("Сколько лет длилась Столетняя война?", "116", "100", "120", "110"),
        ("Какой самый твердый природный материал?", "Алмаз", "Гранит", "Кварц", "Сталь"),
        ("Кто изобрел телефон?", "Белл", "Эдисон", "Тесла", "Маркони"),
        ("В каком году человек впервые полетел в космос?", "1961", "1960", "1962", "1963"),
        ("Что такое фотосинтез?", "Процесс образования органических веществ", "Деление клеток", "Дыхание растений", "Рост корней")
    ]
    
    # Вопросы для молодежной викторины (18-25 лет)
    youth_questions = [
        ("Кто режиссер фильма 'Криминальное чтение'?", "Тарантино", "Скорсезе", "Коппола", "Лукас"),
        ("В каком году был создан интернет?", "1969", "1975", "1980", "1985"),
        ("Что означает HTTP?", "HyperText Transfer Protocol", "High Transfer Text Protocol", "Home Transfer Text Protocol", "Host Transfer Text Protocol"),
        ("Кто основал компанию Apple?", "Джобс", "Гейтс", "Безос", "Маск"),
        ("Какая валюта в Японии?", "Йена", "Юань", "Вон", "Рупия"),
        ("Сколько Нобелевских премий получил Эйнштейн?", "1", "2", "3", "0"),
        ("В каком году распался СССР?", "1991", "1990", "1992", "1989"),
        ("Кто написал '1984'?", "Оруэлл", "Хаксли", "Брэдбери", "Азимов"),
        ("Какой самый посещаемый сайт в мире?", "Google", "YouTube", "Facebook", "Amazon"),
        ("Что означает ВВП?", "Валовый внутренний продукт", "Внешний валютный продукт", "Валютный внутренний продукт", "Валовый внешний продукт"),
        ("Кто изобрел World Wide Web?", "Бернерс-Ли", "Цукерберг", "Пейдж", "Брин"),
        ("В каком году была основана ООН?", "1945", "1944", "1946", "1947"),
        ("Что такое блокчейн?", "Цепочка блоков данных", "Тип компьютера", "Социальная сеть", "Игровая консоль"),
        ("Кто автор книги 'Код да Винчи'?", "Браун", "Кинг", "Толкин", "Мартин"),
        ("Какой самый популярный язык программирования?", "Python", "Java", "C++", "JavaScript")
    ]
    
    # Вопросы для взрослой викторины (26-50 лет)
    adult_questions = [
        ("В каком году закончилась Вторая мировая война?", "1945", "1944", "1946", "1943"),
        ("Кто был первым президентом России?", "Ельцин", "Горбачев", "Путин", "Медведев"),
        ("Что означает акроним НАТО?", "Северо-Атлантический договор", "Национальная армия", "Новый альянс", "Северный альянс"),
        ("В каком году случилась Чернобыльская катастрофа?", "1986", "1985", "1987", "1984"),
        ("Кто автор романа 'Мастер и Маргарита'?", "Булгаков", "Пастернак", "Солженицын", "Шолохов"),
        ("Какая самая высокая гора в мире?", "Эверест", "К2", "Канченджанга", "Лхоцзе"),
        ("В каком году пала Берлинская стена?", "1989", "1988", "1990", "1987"),
        ("Кто написал 'Архипелаг ГУЛАГ'?", "Солженицын", "Шаламов", "Гроссман", "Рыбаков"),
        ("Что такое дефляция?", "Снижение уровня цен", "Рост инфляции", "Девальвация", "Стагнация"),
        ("В каком году началась перестройка?", "1985", "1984", "1986", "1987"),
        ("Кто был архитектором Исаакиевского собора?", "Монферран", "Растрелли", "Росси", "Захаров"),
        ("Что означает ИНН?", "Идентификационный номер налогоплательщика", "Индивидуальный номер", "Именной номер", "Инвестиционный номер"),
        ("В каком году была принята Конституция РФ?", "1993", "1992", "1994", "1991"),
        ("Кто написал оперу 'Евгений Онегин'?", "Чайковский", "Мусоргский", "Римский-Корсаков", "Рахманинов"),
        ("Что такое ипотека?", "Кредит под залог недвижимости", "Страхование жизни", "Вклад в банке", "Покупка акций")
    ]
    
    # Объединяем все вопросы
    all_questions = children_questions + school_questions + teen_questions + youth_questions + adult_questions
    questions.extend(all_questions)
    
    # Добавляем вопросы в базу данных
    open_db()
    query = "INSERT INTO question (question, answer, wrong1, wrong2, wrong3) VALUES (?,?,?,?,?)"
    do_many(query, questions)
    close_db()
    
    # Привязываем вопросы к викторинам (по 15 вопросов на викторину)
    quiz_content = []
    question_id = 1
    
    for quiz_id in range(1, 6):  # 5 викторин
        for i in range(15):  # 15 вопросов на викторину
            quiz_content.append((quiz_id, question_id))
            question_id += 1
    
    # Добавляем связи викторина-вопрос
    open_db()
    query = "INSERT INTO quiz_content (quiz_id, question_id) VALUES (?,?)"
    do_many(query, quiz_content)
    close_db()
    
    print("База данных успешно заполнена!")
    print("Создано 5 викторин:")
    for i, (name, from_age, to_age) in enumerate(quizes, 1):
        print(f"  {i}. {name} ({from_age}-{to_age} лет)")
    print("Каждая викторина содержит 15 уникальных вопросов")

def open_db():
    """Открывает соединение с базой данных"""
    global conn, cursor
    conn = sqlite3.connect("quiz.sqlite")
    cursor = conn.cursor()

def close_db():
    """Закрывает соединение с базой данных"""
    cursor.close()
    conn.close()

def do_many(query, params):
    """Выполняет множественный запрос"""
    cursor.executemany(query, params)
    conn.commit()

if __name__ == "__main__":
    populate_quiz_database()
