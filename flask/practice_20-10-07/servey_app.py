from flask import Flask, render_template, request, jsonify
import pymysql

app = Flask(__name__)

# 메인화면
@app.route("/")
def home():
    return render_template("servey.html")


# 결과화면
@app.route("/result", methods=["POST"])
def result():
    if request.method == "POST":
        result = request.form

        cursor = db.cursor()
        sql = f"""insert into survey_table (name, email, gender, date) values
                    (%(name)s, %(email)s, %(sex)s, %(date of birth)s);"""
        cursor.execute(sql, result)
        db.commit()
        db.close()

        return render_template("result.html", result=result)


# 모든결과화면
@app.route("/list")
def list():
    cursor = db.cursor()
    sql = f"select * from survey_table"
    data = cursor.execute(sql)
    db.commit()
    db.close()

    return render_template("list.html", data=data)


if __name__ == "__main__":
    db = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        passwd="1234",
        db="survey_db",
        charset="utf8",
    )

    app.run(debug=True)