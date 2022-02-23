
from flask import Flask, redirect, render_template, request
from vsearch import search4letters
app = Flask(__name__)

# 데코레이터 decorator 장식자



# 전달 방식
@app.route('/search4',methods=['POST']) 
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = '찾은 결과 입니다'
    results = str(search4letters(phrase, letters))
    return render_template('results.html',
                           the_phrase = phrase,
                           the_letters= letters,
                           the_title = title,
                           the_results = results,)

@app.route('/') # 사이트 접근 주소 
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='글자 찾기 사이트에 방문하신걸 환영합니다.  By 배본영')
# 로컬에서 테스트와 개발을 할때는 app.run() 가 실행이 되야 하지만 배포단계에서는 실행되면 안된다
if __name__ == '__main__' :     
    app.run(debug=True)