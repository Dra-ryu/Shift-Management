import os
import datetime


from cs50 import SQL
from flask import Flask, render_template, request

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///shift.db")

app = Flask(__name__)

@app.route('/attendance', methods=["GET", "POST"])
def attendance():
    if request.method == "POST":
        # ボタンが押されたタイミングの時間計測
        datetime_now = datetime.datetime.now()
        date_today = datetime.date.today()
        time_now = datetime.datetime.now().time()

        # データベースにボタンが押された時間を計測
        db.execute("INSERT INTO shifts (attendance_time) VALUES(?)",
        datetime_now)

        return render_template("attendance.html", time=datetime_now, date=date_today)


@app.route('/break-start', methods=["GET", "POST"])
def break_start():
    if request.method == "POST":
        # ボタンが押されたタイミングの時間計測
        datetime_now = datetime.datetime.now()
        date_today = datetime.date.today()
        time_now = datetime.datetime.now().time()

        # データベースにボタンが押された時間を計測
        db.execute("INSERT INTO shifts (attendance_time) VALUES(?)",
        datetime_now)

        return render_template("break-start.html", time=datetime_now, date=date_today)


@app.route('/break-end', methods=["GET", "POST"])
def break_end():
    if request.method == "POST":
        # ボタンが押されたタイミングの時間計測
        datetime_now = datetime.datetime.now()
        date_today = datetime.date.today()
        time_now = datetime.datetime.now().time()

        # データベースにボタンが押された時間を計測
        db.execute("INSERT INTO shifts (attendance_time) VALUES(?)",
        datetime_now)

        return render_template("break-end.html", time=datetime_now, date=date_today)

@app.route('/leave', methods=["GET", "POST"])
def leave():
    if request.method == "POST":
        # ボタンが押されたタイミングの時間計測
        datetime_now = datetime.datetime.now()
        date_today = datetime.date.today()
        time_now = datetime.datetime.now().time()

        # データベースにボタンが押された時間を計測
        db.execute("INSERT INTO shifts (attendance_time) VALUES(?)",
        datetime_now)

        return render_template("leave.html", time=datetime_now, date=date_today)


# 計算したい
# ボタン押したらデータベースからの取り出し、更新をするのがいいかも

@app.route('/calculate', methods=["GET", "POST"])
def calculate():
    if request.method == "POST":
        # ボタンが押されたタイミングの時間計測

        attendance_time = db.execute("SELECT attendance_time FROM shifts")
        leave_time = db.execute("SELECT leave_time FROM shifts")
        break_start = db.execute("SELECT break_start FROM shifts")
        break_end = db.execute("SELECT break_end FROM shifts")


        attendance_time = datetime.datetime.strptime(attendance_time, '%Y/%m/%d %H:%M:%S')
        leave_time = datetime.datetime.strptime(leave_time, '%Y/%m/%d %H:%M:%S')
        break_start = datetime.datetime.strptime(break_start, '%Y/%m/%d %H:%M:%S')
        break_end = datetime.datetime.strptime(break_end, '%Y/%m/%d %H:%M:%S')


        sum_time = leave_time - attendance_time - (break_end - break_start)

        datetime_now = datetime.datetime.now()
        date_today = datetime.date.today()
        time_now = datetime.datetime.now().time()

        # データベースにボタンが押された時間を計測
        db.execute("INSERT INTO shifts (attendance_time) VALUES(?)",
        datetime_now)

        return render_template("leave.html", time=datetime_now, date=date_today)


@app.route('/', methods=["GET", "POST"])
def input():
    if request.method == "POST":

        # 入力された値を変数に代入
        name = request.form.get("name")
        mailadress = request.form.get("mailadress")
        date = request.form.get("date")
        attendance_time = request.form.get("attendance")
        break_time = request.form.get("break")
        leave_time = request.form.get("leave")


        attendance_time = datetime.datetime.strptime(attendance_time, '%Y/%m/%d %H:%M:%S')
        break_time = datetime.datetime.strptime(break_time, '%Y/%m/%d %H:%M:%S')
        leave_time = datetime.datetime.strptime(leave_time, '%Y/%m/%d %H:%M:%S')

        sum_time = attendance_time - leave_time
        hour = sum_time.hour
        minute = sum_time.minute
        workfor = str(hour) + ":" + str(minute)



        """# 計算はできてる
        # エラーメッセージRuntimeError: unsupported value: 4:00:00
        attendance_time = datetime.datetime.strptime(attendance_time, '%H:%M')
        break_time = datetime.datetime.strptime(break_time, '%H:%M')
        leave_time = datetime.datetime.strptime(leave_time, '%H:%M')"""



        db.execute("INSERT INTO shifts (name, mailadress, date, attendance_time, break_time, leave_time, sum_time) VALUES(?, ?, ?, ?, ?, ?,?)",
        name, mailadress, date, attendance_time, break_time, leave_time, workfor)

        """if not request.form.get("symbol"):
            return render_template("input.html")
        elif not request.form.get("mailadress"):
            return render_template("input.html")
        elif not request.form.get("date"):
            return render_template("input.html")
        elif not request.form.get("attendance"):
            return render_template("input.html")
        elif not request.form.get("break"):
            return render_template("input.html")
        elif not request.form.get("leave"):
            return render_template("input.html")"""


        return render_template("output.html")

    else:
        return render_template("input.html")
if __name__ == '__main__':
    app.run()




"""import os
import datetime

from cs50 import SQL
from flask import Flask, redirect, render_template
# from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
# from werkzeug.security import check_password_hash, generate_password_hash


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

def ap():
    render_template("input.html")

ap()

@app.route("/input")
def inputs():
    if request.method == "POST":

        return render_template("/input")

        # 入力された値を変数に代入
        name = request.form.get("name")
        mailadress = request.form.get("mailadress")
        date = request.form.get("date")
        attendance_time = request.form.get("attendance")
        break_time = request.form.get("break")
        leave_time = request.form.get("leave")

        if name == None:
            return print("名前を入力してください")
        elif mailadress == None:
            return
        elif date == None:
            return
        elif attendance_time == None:
            return
        elif break_time == None:
            return
        elif leave_time == None:
            return

        db.execute("INSERT INTO shifts (name, mailadress, date, attendance_time, break_time, leave_time) VALUES(?, ?, ?, ?, ?, ?)",
        name, mailadress, date, attendance_time, break_time, leave_time)

    else:
        return render_template("input.html")

# メールアドレス登録
#def mailadress():


# 出勤時間
def attendance():
    # 現在の日付, 時刻を測定
    dt_now = datetime.datetime.now()

    print(dt_now)


# 退勤時間
#def leaving():



# 勤務時間fileをdownload
#def download():
if __name__ == "__main__":
    app.run()"""