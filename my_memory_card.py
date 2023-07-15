#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)
from random import shuffle, randint

class Question():
        def __init__(
                self, question, right_answer,
                wrong1, wrong2, wrong3):
                self.question = question
                self.right_answer = right_answer
                self.wrong1 = wrong1
                self.wrong2 = wrong2
                self.wrong3 = wrong3

question_list = []
question_list.append(Question('Метро2033 это', 'книга', 'фильм', 'фирма', 'машина'))
question_list.append(Question('Самое быстрое существо', 'гепард', 'улитка', 'бабушка', 'тележка'))
question_list.append(Question('Мышь это', 'существо', 'материал', 'еда', 'транспорт'))
question_list.append(Question('Что кипит внедрах вулкана', 'лава', 'чай', 'смола', 'разум возмущенный'))
question_list.append(Question('Сколько океанов', 'пять', 'девять', 'один', 'шесть'))
question_list.append(Question('сколько планет в Солнечной системе', 'восемь', 'шесть', 'десять', 'две'))
question_list.append(Question('Кто такой Хан Соло', 'капитан Тысячилетнего сокола', 'начальник золотой орды', 'царь', 'король'))
question_list.append(Question('Рейзер это', 'игровая фирма', 'дом', 'машина', 'мозг'))
question_list.append(Question('Маршал это', 'фирма акустики', 'кружка', 'игра', 'дом'))
question_list.append(Question('Компот', 'напиток', 'еда', 'топливо', 'инекция'))

app = QApplication([])
qwer = QPushButton('Ответить')
Lb_Qeshon = QLabel('Какой национальности не сущечтвует?')

dfg = QGroupBox('Варианты ответов')

rt1 = QRadioButton('Энды')
rt2 = QRadioButton('Чулымцы')
rt3 = QRadioButton('Смурфы')
rt4 = QRadioButton('Алеуты')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rt1)
RadioGroup.addButton(rt2)
RadioGroup.addButton(rt3)
RadioGroup.addButton(rt4)

ghjk_r1 = QHBoxLayout()
ghjk_r2 = QVBoxLayout()
ghjk_r3 = QVBoxLayout()
ghjk_r2.addWidget(rt1)
ghjk_r2.addWidget(rt2)
ghjk_r3.addWidget(rt3)
ghjk_r3.addWidget(rt4)

ghjk_r1.addLayout(ghjk_r2)
ghjk_r1.addLayout(ghjk_r3)

dfg.setLayout(ghjk_r1)

AnsGroupBox = QGroupBox('Результат теста')
bmnn = QLabel('Правильно/Неправильно')
zxc = QLabel('Правильный ответ')

cvb = QVBoxLayout()
cvb.addWidget(bmnn, alignment=(Qt.AlignLeft | Qt.AlignTop))
cvb.addWidget(zxc, alignment=Qt.AlignHCenter , stretch=2)
AnsGroupBox.setLayout(cvb)


line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()

line1.addWidget(Lb_Qeshon, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
line2.addWidget(dfg)
line2.addWidget(AnsGroupBox)

line3.addStretch(1)
line3.addWidget(qwer, stretch=2)
line3.addStretch(1)

lkj = QVBoxLayout()

lkj.addLayout(line1, stretch=2)
lkj.addLayout(line2, stretch=8)
lkj.addStretch(1)
lkj.addLayout(line3, stretch=1)
lkj.addStretch(1)
lkj.addStretch(5)

def show_result():
        dfg.hide()
        AnsGroupBox.show()
        qwer.setText('Следующий вопропс')

def show_queshon():
        dfg.show()
        AnsGroupBox.hide()
        qwer.setText('Ответить')
        RadioGroup.setExclusive(False)
        rt1.setChecked(False)
        rt2.setChecked(False)
        rt3.setChecked(False)
        rt4.setChecked(False)
        RadioGroup.setExclusive(True)

answer = [rt1, rt2, rt3, rt4,]

def ask(q: Question):
        shuffle(answer)
        answer[0].setText(q.right_answer)
        answer[1].setText(q.wrong1)
        answer[2].setText(q.wrong2)
        answer[3].setText(q.wrong3)
        Lb_Qeshon.setText(q.question)
        zxc.setText(q.right_answer)
        show_queshon()

def show_correct(res):
        bmnn.setText(res)
        show_result()

def check_answer():
        if answer[0].isChecked():
                show_correct('Правильно!')
                window.score += 1
                print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)
                print('Рейтинг: ', (window.score / window.total * 100), '%')
        else:
                if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
                        show_correct('Неверно!')
                        print('Рейтинг: ', (window.score / window.total * 100), '%')

def next_question():
        window.total += 1
        print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)
        cup_question = randint(0, len(question_list) -1 )
        q = question_list[cup_question]
        ask(q)

def click_Ok():
        if qwer.text() == 'Ответить':
                check_answer()
        else:
                next_question()

window = QWidget()
window.setLayout(lkj)
window.setWindowTitle('Вопросы для гениев')

qwer.clicked.connect(click_Ok)
window.score = 0
window.total = 0
window.show()
next_question()
app.exec()
