# 필요한 패키지 import 하는것 
from flask import Flask, render_template
import flask
from flask import Flask, request, render_template
import os

# 여기서 flask 로컬호스트를 여는 부분
import numpy as np
app = Flask(__name__)

# 웹 시작했을때 첫화면에 나오는 html 정의한것
@app.route("/")
def template_test():
    return render_template(
                'index.html',
                # 웹 메인이름 지정                      
                title="3이1최",     
            )
# 웹 상에서 iframe을 통해서 띄울 목록들을 flask가 인식하도록 하는것
@app.route("/test_0823.html")
# 전체지도
def data1():
    return render_template('test_0823.html')
# 연평균
@app.route("/year_mean_line.html")
def data2():
    return render_template('year_mean_line.html')
#연별 적발 평균
@app.route("/year_jucval.html")
def data3():
    return render_template('year_jucval.html')
# 월별 품목별 평균
@app.route("/pum_mok.html")
def data4():
    return render_template('pum_mok.html')
# 업태별 평균
@app.route("/up_tae.html")
def data5():
    return render_template('up_tae.html')
# 동별지도
@app.route("/new_dong_up.html")
def data6():
    return render_template('new_dong_up.html')
# 최종 결과 지도
@app.route("/final_grid.html")
def data7():
    return render_template('final_grid.html')
# 적발횟수 시각화 지도
@app.route("/count.html")
def data8():
    return render_template('count.html')
# allaao~allaao24까지가 카카오 api상에서 띄울 지도
@app.route("/allaa0.html")
def data9():
    return render_template('allaa0.html')
@app.route("/allaa1.html")
def data10():
    return render_template('allaa1.html')
@app.route("/allaa2.html")
def data11():
    return render_template('allaa2.html')
@app.route("/allaa3.html")
def data12():
    return render_template('allaa3.html')
@app.route("/allaa4.html")
def data13():
    return render_template('allaa4.html')
@app.route("/allaa5.html")
def data14():
    return render_template('allaa5.html')
@app.route("/allaa6.html")
def data15():
    return render_template('allaa6.html')
@app.route("/allaa7.html")
def data16():
    return render_template('allaa7.html')
@app.route("/allaa8.html")
def data17():
    return render_template('allaa8.html')
@app.route("/allaa9.html")
def data18():
    return render_template('allaa9.html')
@app.route("/allaa10.html")
def data19():
    return render_template('allaa10.html')
@app.route("/allaa11.html")
def data20():
    return render_template('allaa11.html')
@app.route("/allaa12.html")
def data21():
    return render_template('allaa12.html')
@app.route("/allaa13.html")
def data22():
    return render_template('allaa13.html')
@app.route("/allaa14.html")
def data23():
    return render_template('allaa14.html')
@app.route("/allaa15.html")
def data24():
    return render_template('allaa15.html')
@app.route("/allaa16.html")
def data25():
    return render_template('allaa16.html')
@app.route("/allaa17.html")
def data26():
    return render_template('allaa17.html')
@app.route("/allaa18.html")
def data27():
    return render_template('allaa18.html')
@app.route("/allaa19.html")
def data28():
    return render_template('allaa19.html')
@app.route("/allaa20.html")
def data29():
    return render_template('allaa20.html')
@app.route("/allaa21.html")
def data30():
    return render_template('allaa21.html')
@app.route("/allaa22.html")
def data31():
    return render_template('allaa22.html')
@app.route("/allaa23.html")
def data32():
    return render_template('allaa23.html')
@app.route("/allaa24.html")
def data33():
    return render_template('allaa24.html')
#예측한 지역안에 있는 업체들 띄운 지도
@app.route("/point.html")
def data34():
    return render_template('point.html')
# flask 실행 자동화 하는 부분
if __name__ == '__main__':
    app.run()
