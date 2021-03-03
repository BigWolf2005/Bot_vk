import vk_api, json
from vk_api.longpoll import VkLongPoll, VkEventType

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
                sender(id, 'Лови')
                send_photo(id, 'photo-201491242_457239017')

            elif msg == '2':
                sender(id, 'Лови')
                send_photo(id, 'photo-201491242_457239018')

            elif msg == '3':
                sender(id, 'Лови')
                send_photo(id, 'photo385821903_457251996')

            elif msg == '4':
                sender(id, 'Лови')
                send_photo(id, 'photo-181795746_457240618')

            elif msg == '5':
                sender(id, 'Лови')
                send_photo(id, 'photo-181795746_457240611')

            elif msg == '6':
                sender(id, 'Лови')
                send_photo(id, 'photo-201491242_457239019')

            elif msg == '7':
                sender(id, 'Лови')
                send_photo(id, 'photo-201491242_457239020')

            elif msg == '8':
                sender(id, 'Лови')
                send_photo(id, 'photo-201491242_457239022')

            elif msg == '9':
                sender(id, 'Лови')
                send_photo(id, 'photo-201491242_457239024')

            elif msg == '10':
                sender(id, 'Лови')
                send_photo(id, 'photo-201491242_457239025')

            elif msg == '11':
                sender(id, 'Лови')
                send_photo(id, 'photo-201491242_457239026')

            elif msg == '12':
                sender(id, 'Лови')
                send_photo(id, 'photo-201491242_457239027')

            elif msg == '13':
                sender(id, 'Лови')
                send_photo(id, 'photo-201491242_457239028')

            elif msg == '14':
                sender(id, 'Лови')
                send_photo(id, 'photo-201491242_457239029')

            elif msg == '15':
                sender(id, 'Лови')
                send_photo(id, 'photo-201491242_457239030')

            elif msg == '16':
                sender(id, 'Лови')
                send_photo(id, 'photo-201491242_457239031')

            elif msg == '17':
                sender(id, 'Лови')
                send_photo(id, 'photo-201491242_457239032')

            elif msg == '18':
                sender(id, 'Лови')
                send_photo(id, 'photo-201491242_457239033')

            elif msg == '19':
                sender(id, 'Лови')
                send_photo(id, 'photo-201491242_457239034')

            elif msg == '20':
                sender(id, 'Лови')
                send_photo(id, 'photo-201491242_457239035')

            elif msg == '21':
                sender(id, 'Лови')
                send_photo(id, 'photo-201491242_457239036')

            elif msg == '22':
                sender(id, 'Лови')
                send_photo(id, 'photo-201491242_457239037')

            elif msg == '23':
                sender(id, 'Лови')
                send_photo(id, 'photo-201491242_457239038')

            elif msg == '24':
                sender(id, 'Лови')
                send_photo(id, 'photo-201491242_457239040')

            elif msg == '25':
                sender(id, 'Лови')
                send_photo(id, 'photo-201491242_457239041')

            elif msg == '26':
                sender(id, 'Лови')
                send_photo(id, 'photo-201491242_457239042')

            elif msg == '27':
                sender(id, 'Лови')
                send_photo(id, 'photo-201491242_457239043')

            elif msg == '28':
                sender(id, 'Лови')
                send_photo(id, 'photo-201491242_457239044')

            elif msg == '29':
                sender(id, 'Лови')
                send_photo(id, 'photo-201491242_457239045')

            elif msg == '30':
                sender(id, 'Лови')
                send_photo(id, 'photo-201491242_457239046')

            elif msg == '31':
                sender(id, 'Лови')
                send_photo(id, 'photo-201491242_457239047')

            elif msg == '32':
                sender(id, 'Лови')
                send_photo(id, 'photo-201491242_457239048')

            elif msg == '33':
                sender(id, 'Лови')
                send_photo(id, 'photo-201491242_457239049')

            elif msg == '34':
                sender(id, 'Лови')
                send_photo(id, 'photo-201491242_457239050')

            elif msg == '35':
                sender(id, 'Лови')
                send_photo(id, 'photo-201491242_457239051')

            elif msg == '36':
                sender(id, 'Лови')
                send_photo(id, 'photo-201491242_457239052')

            elif msg == '37':
                sender(id, 'Лови')
                send_photo(id, 'photo-201491242_457239053')

            elif msg == '38':
                sender(id, 'Лови')
                send_photo(id, 'photo-201491242_457239054')

            elif msg == '39':
                sender(id, 'Лови')
                send_photo(id, 'photo-201491242_457239055')

            elif msg == '40':
                sender(id, 'Лови')
                send_photo(id, 'photo-201491242_457239056')




#Видео
            elif msg == '01':
                sender(id, 'Лови')
                send_photo(id, 'video-201426244_456239017')

            elif msg == '02':
                sender(id, 'Лови')
                send_photo(id, 'video-193098763_456245282')

            elif msg == '03':
                sender(id, 'Лови')
                send_photo(id, 'video256403283_456240327')

            elif msg == '04':
                sender(id, 'Лови')
                send_photo(id, 'video111989041_169786008')

            elif msg == '05':
                sender(id, 'Лови')
                send_photo(id, 'video355871213_456239324')

            elif msg == '06':
                sender(id, 'Лови')
                send_photo(id, 'video-88851361_456239968')

            elif msg == '07':
                sender(id, 'Лови')
                send_photo(id, 'video-173250963_456239103')

            elif msg == '08':
                sender(id, 'Лови')
                send_photo(id, 'video348606941_456239057')

            elif msg == '09':
                sender(id, 'Лови')
                send_photo(id, 'video-145709015_456239975')

            elif msg == '010':
                sender(id, 'Лови')
                send_photo(id, 'video-146305289_456240971')

            elif msg == '011':
                sender(id, 'Лови')
                send_photo(id, 'video-61052294_456241839')

            elif msg == '012':
                sender(id, 'Лови')
                send_photo(id, 'video-61052294_456240884')

            elif msg == '013':
                sender(id, 'Лови')
                send_photo(id, 'video140366885_456240402')

            elif msg == '014':
                sender(id, 'Лови')
                send_photo(id, 'video-184128423_456239051')

            elif msg == '015':
                sender(id, 'Лови')
                send_photo(id, 'video337200561_456239415')
