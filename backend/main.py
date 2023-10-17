from fastapi import FastAPI
import urllib.request, json
import psycopg2

app = FastAPI()

def select_question():
    conn = psycopg2.connect(dbname='quiz', user='lucky', password='12345', host='db', port="5432")
    with conn.cursor() as cur:
        sql = "SELECT * FROM questions"
        cur.execute(sql)
        questions = cur.fetchall()
    conn.commit()
    conn.close()
    if not len(questions):
        return {}
    return questions[-1]
def insert_questions(question_list):
    inserted = 0
    conn = psycopg2.connect(dbname='quiz', user='lucky', password='12345', host='db', port="5432")
    with conn.cursor() as cur:
        sql = "SELECT question_id FROM questions"
        cur.execute(sql)
        ids = [x[0] for x in cur.fetchall()]
        for i in range(len(question_list)):
            if question_list[i]["id"] in ids:
                continue
            sql = "INSERT INTO questions(question_id, question, answer, created_at) VALUES (%s, %s, %s, %s)"
            cur.execute(sql, (question_list[i]["id"], question_list[i]["question"], 
                question_list[i]["answer"], question_list[i]["created_at"]))
            inserted += 1
    conn.commit()
    conn.close()
    return inserted

@app.post("/questions_num")
async def post_quensions(questions_dict: dict):
    if "questions_num" not in questions_dict.keys() or type(questions_dict["questions_num"]) != int:
        return {'error': 'the input must be of format {"questions_num": integer}'}
    if questions_dict["questions_num"] < 1:
        return {'error': 'questions_num must be positive'}
    questions_num = questions_dict["questions_num"]
    question = select_question()
    while questions_num:
        with urllib.request.urlopen(f"https://jservice.io/api/random?count={questions_num}") as url:
            question_list = json.load(url)
            questions_num -= insert_questions(question_list)
    return {"question": question}