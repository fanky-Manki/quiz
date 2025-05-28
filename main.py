from flask import Flask, redirect, url_for, session , request, render_template
from db_scripts import get_next_question, get_quiz_count, get_quizes, check_answer
from random import randint 
from random import shuffle

def start_quiz(quiz_id):
    session["quiz"] = quiz_id
    session["question"] = 0
    session["total_answers"] = 0
    session["right_answers"] = 0

def end_quiz():
    session.clear()


def save_answer():
    answer = request.form.get("answer")
    question_id = request.form.get("question_id")
    session['question'] = question_id
    session["total_answers"] += 1
    if check_answer(question_id, answer):
        session["right_answers"] += 1


def get_quizes_form():
    quizes = get_quizes()
    return render_template("start.html", quizes=quizes)

def get_question_form(question):
    answers = [question[2], question[3], question[4], question[5]]
    shuffle(answers)
    return render_template("test.html", quiz_id=session["quiz"], question_id=question[0], question=question[1],  answers=answers)

def get_result_form():
    right_answers = session["right_answers"] 
    total_answers = session["total_answers"] 
    rating = round(right_answers / total_answers, 1) * 100
    return render_template("result.html", quiz_id=session["quiz"], right_answers=right_answers, total_answers=total_answers, rating=rating)




def index():
    if request.method == "GET":
        start_quiz(-1)
        return get_quizes_form()
    elif request.method == "POST":
        quiz_id = request.form.get("quiz")
        start_quiz(quiz_id)
        return redirect(url_for("test"))



def test():
    if not ("quiz" in session) or int(session["quiz"]) <0:
        return redirect(url_for("index"))
    else:
        if request.method == "POST":
            save_answer()
        next_question = get_next_question(session["quiz"], session["question"])
        if next_question is None or len(next_question) == 0:
            return redirect(url_for("result"))
        else:
            return get_question_form(next_question)
 
def result():
    form = get_result_form()
    end_quiz()
    return form



app = Flask(__name__)
app.config["SECRET_KEY"] = 'sdsdsadfasf'
app.add_url_rule("/result", "result", result)
app.add_url_rule("/", "index", index, methods=["POST", "GET"])
app.add_url_rule("/test", "test", test, methods=["POST", "GET"])
if __name__ == "__main__":
    app.run()