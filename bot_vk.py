import vk_api, json
from vk_api.longpoll import VkLongPoll, VkEventType

with open('data_id.json') as k:
    dload = json.load(k)

with open('config.json') as f:
    templates = json.load(f)

#Токен группы
vk_session = vk_api.VkApi(token = templates['vk']['access_token'])
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

#Клавиатура
def get_but(text, color):
    return {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"" + "1" + "\"}",
                    "label": f"{text}"
                },
                "color": f"{color}"
            }

keyboard = {
    "one_time" : False,
    "buttons" : [
        [get_but('Задать вопрос', 'primary'), get_but('Предложить новость', 'primary')],
        [get_but('Пикчи', 'positive'), get_but('Видосы', 'positive')]
    ]
}

keyboard = json.dumps(keyboard, ensure_ascii = False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))

#Функция для отправки сообщений
def sender(id, text):
    vk.messages.send(user_id = id, message = text, random_id = 0, keyboard = keyboard)

#Функция для отправки стикеров
def send_stick(id, number):
    vk.messages.send(user_id = id, sticker_id = number, random_id = 0,)

#Функция для отправки фото и видео
def send_photo(id, url):
    vk.messages.send(user_id = id, attachment = url, random_id = 0)

#Функции вместе
def send_photo_wrapper(user_id, photo_id):
    sender(user_id, 'Лови')
    send_photo(id, photo_id)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:

            msg = event.text.lower()
            id = event.user_id

            if msg == 'привет':
                sender(id, 'Здравствуйте')
                send_stick(id, 6)

            elif msg == 'задать вопрос':
                sender(id, 'Напишите ваш вопрос, и мы постараемся скорее на него ответить')

            elif msg == 'предложить новость':
                sender(id, 'Что вы хотите предложить?')

            elif msg == 'пока':
                sender(id, 'До свидания')

            elif msg == 'пикчи':
                sender(id, 'Чтобы я вам отправил мем, напишите его номер. У нас есть такие мемы: \
                \n1) Бабка сидит и молчит; \
                \n2) Деб; \
                \n3) Я обязательно выживу; \
                \n4) Иногда моя гениальность пугает меня; \
                \n5) Хто я?; \
                \n6) Капирующий ниндзя; \
                \n7) Срывный нерв; \
                \n8) Я устал, босс; \
                \n9) Мирного решения не будет; \
                \n10) О вы из англии; \
                \n11) Украинская разведка; \
                \n12) Карта уно; \
                \n13) Боярская шутка; \
                \n14) Сомнение; \
                \n15) Эта шутка не смешная; \
                \n16) Бредятина; \
                \n17) Bruh; \
                \n18) Ну привет; \
                \n19) Ты чертовски прав; \
                \n20) Папочка добр; \
                \n21) Папочка зол; \
                \n22) Школа фу, кампутер класс; \
                \n23) PogChamp; \
                \n24) Ёк макарёк; \
                \n25) Когда увидел...; \
                \n26) О нет! А в прочем...; \
                \n27) Я какая-то шутка для тебя?; \
                \n28) Niggaдяй; \
                \n29) Я достиг комедии; \
                \n30) Ну да, ну да. Пошёл я нахер; \
                \n31) С Денчиком); \
                \n32) 0_0; \
                \n33) Почему ты до сих пор не умер?; \
                \n34) Понятно, хорошего дня; \
                \n35) Ты знаешь, что такое дратути?; \
                \n36) Гарольд, скрывающий боль; \
                \n37) Это не так много, но это честная работа; \
                \n38) Банальный вопрос, анальный ответ; \
                \n39) Хорошая пикча, теперь она наша; \
                \n40) Онжоможно.')

            elif msg == 'видосы':
                sender(id, 'Чтобы я вам отправил видео, напишите его номер. У нас есть такие видео: \
                \n01) Niggers; \
                \n02) Танцы...; \
                \n03) Чел, ты клоун; \
                \n04) Смекаешь?; \
                \n05) Flex Air (все части); \
                \n06) Directed By Robert B Weide Remix; \
                \n07) На случай баянов; \
                \n08) Где пруфы?; \
                \n09) Хардбасс тоже флекс; \
                \n010) А чё так можно было что ли?; \
                \n011) Вот это поворот; \
                \n012) Оу май гад, вау; \
                \n013) Ля ты крыса; \
                \n014) Ооо! Повезло, повезло; \
                \n015) Чумба.')




#Пикчи
            elif msg == '1':
                send_photo_wrapper(id, dload['1'])

            elif msg == '2':
                send_photo_wrapper(id, dload['2'])

            elif msg == '3':
                send_photo_wrapper(id, dload['3'])

            elif msg == '4':
                send_photo_wrapper(id, dload['4'])

            elif msg == '5':
                send_photo_wrapper(id, dload['5'])

            elif msg == '6':
                send_photo_wrapper(id, dload['6'])

            elif msg == '7':
                send_photo_wrapper(id, dload['7'])

            elif msg == '8':
                send_photo_wrapper(id, dload['8'])

            elif msg == '9':
                send_photo_wrapper(id, dload['9'])

            elif msg == '10':
                send_photo_wrapper(id, dload['10'])

            elif msg == '11':
                send_photo_wrapper(id, dload['11'])

            elif msg == '12':
                send_photo_wrapper(id, dload['12'])

            elif msg == '13':
                send_photo_wrapper(id, dload['13'])

            elif msg == '14':
                send_photo_wrapper(id, dload['14'])

            elif msg == '15':
                send_photo_wrapper(id, dload['15'])

            elif msg == '16':
                send_photo_wrapper(id, dload['16'])

            elif msg == '17':
                send_photo_wrapper(id, dload['17'])

            elif msg == '18':
                send_photo_wrapper(id, dload['18'])

            elif msg == '19':
                send_photo_wrapper(id, dload['19'])

            elif msg == '20':
                send_photo_wrapper(id, dload['20'])

            elif msg == '21':
                send_photo_wrapper(id, dload['21'])

            elif msg == '22':
                send_photo_wrapper(id, dload['22'])

            elif msg == '23':
                send_photo_wrapper(id, dload['23'])

            elif msg == '24':
                send_photo_wrapper(id, dload['24'])

            elif msg == '25':
                send_photo_wrapper(id, dload['25'])

            elif msg == '26':
                send_photo_wrapper(id, dload['26'])

            elif msg == '27':
                send_photo_wrapper(id, dload['27'])

            elif msg == '28':
                send_photo_wrapper(id, dload['28'])

            elif msg == '29':
                send_photo_wrapper(id, dload['29'])

            elif msg == '30':
                send_photo_wrapper(id, dload['30'])

            elif msg == '31':
                send_photo_wrapper(id, dload['31'])

            elif msg == '32':
                send_photo_wrapper(id, dload['32'])

            elif msg == '33':
                send_photo_wrapper(id, dload['33'])

            elif msg == '34':
                send_photo_wrapper(id, dload['34'])

            elif msg == '35':
                send_photo_wrapper(id, dload['35'])

            elif msg == '36':
                send_photo_wrapper(id, dload['36'])

            elif msg == '37':
                send_photo_wrapper(id, dload['37'])

            elif msg == '38':
                send_photo_wrapper(id, dload['38'])

            elif msg == '39':
                send_photo_wrapper(id, dload['39'])

            elif msg == '40':
                send_photo_wrapper(id, dload['40'])




#Видео
            elif msg == '01':
                send_photo_wrapper(id, dload['01'])

            elif msg == '02':
                send_photo_wrapper(id, dload['02'])

            elif msg == '03':
                send_photo_wrapper(id, dload['03'])

            elif msg == '04':
                send_photo_wrapper(id, dload['04'])

            elif msg == '05':
                send_photo_wrapper(id, dload['05'])

            elif msg == '06':
                send_photo_wrapper(id, dload['06'])

            elif msg == '07':
                send_photo_wrapper(id, dload['07'])

            elif msg == '08':
                send_photo_wrapper(id, dload['08'])

            elif msg == '09':
                send_photo_wrapper(id, dload['09'])

            elif msg == '010':
                send_photo_wrapper(id, dload['010'])

            elif msg == '011':
                send_photo_wrapper(id, dload['011'])

            elif msg == '012':
                send_photo_wrapper(id, dload['012'])

            elif msg == '013':
                send_photo_wrapper(id, dload['013'])

            elif msg == '014':
                send_photo_wrapper(id, dload['014'])

            elif msg == '015':
                send_photo_wrapper(id, dload['015'])
