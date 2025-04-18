''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QMessageBox)

from random import randint, shuffle
class Question():
        def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
                self.question = question
                self.right_answer = right_answer
                self.wrong1 = wrong1
                self.wrong2 = wrong2
                self.wrong3 = wrong3
question_list = list()
question_list.append(Question('Государственный язык бразилии','Португальский','Английский','Испанский','Бразильский'))
question_list.append(Question('Весит груша нельзя скушать','лампочка','яблоко','потолок','Америка'))
question_list.append(Question('Кокого цвета нет в Российском флаге',"зеленый",'синий','красный','белый'))
question_list.append(Question('главный враг России','Америка','Польша','Англий','Бразилия'))
question_list.append(Question('Первая буква Алфавита','а','л','х','й'))
app = QApplication([])
lb_Question = QLabel('самый сложный вопрос в мире')
btn_Ok = QPushButton('Ответить')
RadioGroupBox = QGroupBox('Варианты ответа')
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результаты теста')
lb_Result = QLabel('прав ты или нет')
lb_Correct = QLabel('Ответ будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft|Qt.AlignTop))
layout_res.addWidget(lb_Correct,  alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
RadioGroupBox.show()
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_Ok, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
        RadioGroupBox.hide()#показать панель ответов
        AnsGroupBox.show()
        btn_Ok.setText('Следующий вопрос')

def show_question():
        RadioGroupBox.show()
        AnsGroupBox.hide()
        btn_Ok.setText('Ответить')
        RadioGroup.setExclusive(False)
        rbtn_1.setChecked(False)
        rbtn_2.setChecked(False)
        rbtn_3.setChecked(False)
        rbtn_4.setChecked(False)
        RadioGroup.setExclusive(True)
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
        shuffle(answers)
        answers[0].setText(q.right_answer)
        answers[1].setText(q.wrong1)
        answers[2].setText(q.wrong2)
        answers[3].setText(q.wrong3)
        lb_Question.setText(q.question)
        lb_Correct.setText(q.right_answer)
        show_question()
        lb_Result.setText(res)
        show_result()

def chek_answer():
     
        if answers[0].isChecked():
                show_correct('Крутышка')
                
        else:
                if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
                        show_correct('Неверно')
                        

def next_question():
        mw.cur_question = mw.cur_question +1
        if mw.cur_question >= len(question_list):
                mw.cur_question = 0
        q = question_list[mw.cur_question]
        ask(q)

def click_OK():
        if btn_Ok.text() == 'Ответить':
                chek_answer() 
                
        else:
                next_question()
       

btn_Ok.clicked.connect(click_OK)

mw = QWidget()
mw.cur_question = -1
mw.setLayout(layout_card)
mw.setWindowTitle('Memory card')
mw.resize(500, 300)
mw.show()
app.exec()
17:57 18.04.2025