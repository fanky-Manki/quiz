import sqlite3
db_name = 'quiz.sqlite'
conn = None
cursor = None

def open():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

def close():
    cursor.close()
    conn.close()

def do(query, params=()):
    cursor.execute(query, params)
    conn.commit()


def do_many(query, params):
    cursor.executemany(query, params)
    conn.commit()

def clear_db():
    ''' удаляет все таблицы '''
    open()
    query = '''DROP TABLE IF EXISTS quiz_content'''
    do(query)
    query = '''DROP TABLE IF EXISTS question'''
    do(query)
    query = '''DROP TABLE IF EXISTS quiz'''
    do(query)
    close()

    
def create():
    open()
    do("PRAGMA foreign_keys=on")

    do('''
        CREATE TABLE IF NOT EXISTS quiz (
        id INTEGER PRIMARY KEY, 
        name VARCHAR, 
        from_age INTEGER,
        to_age INTEGER
        )''')

    do('''
        CREATE TABLE IF NOT EXISTS question (
        id INTEGER PRIMARY KEY, 
        question VARCHAR, 
        answer VARCHAR,
        wrong1 VARCHAR,
        wrong2 VARCHAR,
        wrong3 VARCHAR
        )''')
    
    do('''
        CREATE TABLE IF NOT EXISTS quiz_content(
        id INTEGER PRIMARY KEY, 
        quiz_id INTEGER,
        question_id INTEGER,
        FOREIGN KEY (quiz_id) REFERENCES quiz (id),
        FOREIGN KEY (question_id) REFERENCES question (id)
        )''')

    close()

def add_quizes():
    quizes = [
        ('Своя игра', 14, 16,),
        ('Кто хочет стать миллионером?', 12, 14,),
        ('Самый умный', 10, 12,)]

    open()
    query = 'INSERT INTO quiz (name, from_age, to_age) VALUES (?,?,?)'
    do_many(query, quizes)
    close()

def add_questions():
    questions = [
        ('Сколько месяцев в году имеют 28 дней?', 'Все', 'Один', 'Ни одного', 'Два'),
        ('Каким станет зелёный утёс, если упадёт в Красное море?', 'Мокрым', 'Красным', 'Не изменится', 'Фиолетовым'),
        ('Какой рукой лучше размешивать чай?', 'Ложкой', 'Правой', 'Левой', 'Любой'),
        ('Что не имеет длины, глубины, ширины, высоты, а можно измерить?', 'Время', 'Глупость', 'Море', 'Воздух'),
        ('Когда сетью можно вытянуть воду?', 'Когда вода замерзла', 'Когда нет рыбы', 'Когда уплыла золотая рыбка', 'Когда сеть порвалась'),
        ('Что больше слона и ничего не весит?', 'Тень слона', 'Воздушный шар', 'Парашют', 'Облако')
    ]

    open()
    query = 'INSERT INTO question (question, answer, wrong1, wrong2, wrong3) VALUES (?,?,?,?,?)'
    do_many(query, questions)
    close()


def add_quiz_content():
    query = 'INSERT INTO quiz_content (quiz_id, question_id) VALUES (?,?)'

    open()
    answer = input("Дабвить связь (д/н)?")
    while answer != "н":
        quiz_id = int(input("id викторины: "))
        question_id = int(input("id вопроса: "))
        do(query, [quiz_id, question_id])
        answer = input("Дабвить связь (д/н)?")
    close()


def get_next_question(quiz_id=1, question_id=0):
    query = '''
    SELECT quiz_content.id, question.question, question.answer, question.wrong1, question.wrong2, question.wrong3
    FROM question, quiz_content
    WHERE quiz_content.question_id == question.id
    AND quiz_content.id > ?
    AND quiz_content.quiz_id == ?'''


    open()
    do(query, [question_id, quiz_id])
    result = cursor.fetchone()
    close()
    return result

def get_quiz_count():
    query = "SELECT * from quiz"
    
    open()
    do(query)
    result = cursor.fetchall()
    close()
    return len(result)

def get_quizes():
    query= "SELECT * from quiz ORDER BY id"
    
    open()
    do(query)
    result = cursor.fetchall()
    close()
    return result

def check_answer(question_id, answer):
    query = """
    SELECT question.answer
    FROM quiz_content, question
    WHERE quiz_content.question_id = question.id
    AND quiz_content.id = ?
    """

    open()
    cursor.execute(query, (str(question_id),))
    result = cursor.fetchone()
    close()
    if result:
        if result[0] == answer:
            return True
        else:
            return False
    else:
            return False



def show(table):
    query = 'SELECT * FROM ' + table
    open()
    cursor.execute(query)
    print(cursor.fetchall())
    close()

def show_tables():
    show('question')
    show('quiz')
    show('quiz_content')

def main():
    clear_db()
    create()
    add_quizes()
    add_questions()
    add_quiz_content()
    show_tables()

    print(get_next_question(1, 1))

if __name__ == "__main__":
    main()
