from random import choice

answer = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом',
          'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да',
          'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать','Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять',
          'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно']

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')

user_name = input('Представьтесь пожалуйста: ')

print(f'Привет, {user_name}')

flag = True

while flag:
    print('Введите Ваш вопрос, на который можно ответить да или нет:')
    question = input()
    print(choice(answer))
    again = input('Может еще один вопрос? да / нет:')
    if again.lower() != 'да':
        flag = False

print('Возвращайся, если возникнут вопросы!')
