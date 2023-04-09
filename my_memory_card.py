from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import shuffle

class Question():
    def __init__(self,question,right_ansewr,wrong_1,wrong_2,wrong_3):
        self.question = question
        self.right_answer = right_ansewr
        self.wrong_1 = wrong_1
        self.wrong_2 = wrong_2
        self.wrong_3 = wrong_3

question_list = []
question_list.append(Question('Какой год называют "Милениум"','2000','1999','2001','2222'))
question_list.append(Question('Как переводяться "Ряд" на английском языке?','row','raid','road','rail'))
question_list.append(Question('В каком году закончилась 2 мировая война','1945','1941','1935','2000'))

shuffle(question_list)

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
qu = QLabel('Какой национальности не существует?')

#начало группы
rad = QGroupBox('Варианты ответов')
rb1 = QRadioButton('Энцы')
rb2 = QRadioButton('Смурфы')
rb3 = QRadioButton('Чулымцы')
rb4 = QRadioButton('Алеуты')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rb1)
RadioGroup.addButton(rb2)
RadioGroup.addButton(rb3)
RadioGroup.addButton(rb4)

layout_qu1 = QHBoxLayout()
layout_qu2 = QVBoxLayout()
layout_qu3 = QVBoxLayout()

layout_qu2.addWidget(rb1,alignment = Qt.AlignCenter)
layout_qu2.addWidget(rb2,alignment = Qt.AlignCenter)
layout_qu3.addWidget(rb3,alignment = Qt.AlignCenter)
layout_qu3.addWidget(rb4,alignment = Qt.AlignCenter)

layout_qu1.addLayout(layout_qu2)
layout_qu1.addLayout(layout_qu3)
rad.setLayout(layout_qu1)
#конец группы

#Группа результата теста
AnswerGroup = QGroupBox('Результат теста')
lb_result = QLabel('правильно/неправильно')
lb_current = QLabel('Правильный ответ')
answer_line = QVBoxLayout()
answer_line.addWidget(lb_result, alignment = Qt.AlignCenter)
answer_line.addWidget(lb_current, alignment = Qt.AlignCenter)
AnswerGroup.setLayout(answer_line)
#Конец результата

btn = QPushButton('Ответить')
layoutH1 = QVBoxLayout()
layoutH1.addWidget(qu,alignment = Qt.AlignCenter)
layoutH1.addWidget(rad,alignment = Qt.AlignCenter)
layoutH1.addWidget(AnswerGroup,alignment =Qt.AlignCenter)
layoutH1.addWidget(btn,alignment = Qt.AlignCenter)
AnswerGroup.hide()
def show_result():
    rad.hide()
    AnswerGroup.show()
    btn.setText('Следуший вопрос')

def show_question():
    AnswerGroup.hide()
    rad.show()
    btn.setText('Ответить')
    RadioGroup.setExclusive(False)
    rb1.setChecked(False)
    rb2.setChecked(False)
    rb3.setChecked(False)
    rb4.setChecked(False)
    RadioGroup.setExclusive(True)

def start():
    if btn.text() == 'Ответить':
        check_answer()
    else:
        next_question()
    
answers = [rb1,rb2,rb3,rb4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong_1)
    answers[2].setText(q.wrong_2)
    answers[3].setText(q.wrong_3)
    qu.setText(q.question)
    lb_current.setText(q.right_answer)
    show_question()

def next_question():
    main_win.num_of_question += 1
    if main_win.num_of_question == len(question_list):
        main_win.num_of_question = 0
    q = question_list[main_win.num_of_question]
    ask(q)

def check_answer():
    if answers[0].isChecked() == True:
        lb_current.setText('Правильно!')
    else:
        lb_current.setText('Неверно!')
    show_result()

main_win.num_of_question = -1
next_question()
btn.clicked.connect(start)
main_win.setLayout(layoutH1)
main_win.show()
app.exec_()