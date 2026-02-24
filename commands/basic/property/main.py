from aiogram import types, Dispatcher

import commands.basic.property.db as db
from assets.antispam import antispam
from commands.basic.property.lists import *
from assets.transform import transform_int as tr
from user import EtherionUser, EtherionConst


@antispam
async def helicopters_list(message: types.Message, user: EtherionUser):
    await message.answer(f'''{user.url}, доступные вертолёты:
🚁 1. Воздушный шар - 100.000$
🚁 2. RotorWay Exec 162F - 3.500.000$
🚁 3. Robinson R44 - 10.000.000$
🚁 4. Hiller UH-12C - 30.000.000$
🚁 5. AW119 Koala - 63.400.000$
🚁 6. MBB BK 117 - 150.000.000$
🚁 7. Eurocopter EC130 - 350.000.000$
🚁 8. Leonardo AW109 Power - 750.000.000$
🚁 9. Sikorsky S-76 - 1.240.000.000$
🚁 10. Bell 429WLG - 8.890.000.000$
🚁 11. NHI NH90 - 88.330.000.000$
🚁 12. Kazan Mi-35M - 225.750.000.000$
🚁 13. Bell V-22 Osprey - 945.300.000.000$

🛒 Для покупки вертолёта введите "Купить вертолет [номер]"''')


@antispam
async def cars_list(message: types.Message, user: EtherionUser):
    await message.answer(f'''{user.url}, доступные машины:
🚗 1. Самокат - 10.000.000$
🚗 2. Велосипед - 15.000.000$
🚗 3. Гироскутер - 30.000.000$
🚗 4. Сегвей - 50.000.000$
🚗 5. Мопед - 90.000.000$
🚗 6. Мотоцикл - 100.000.000$
🚗 7. ВАЗ 2109 - 250.000.000$
🚗 8. Квадроцикл - 400.000.000$
🚗 9. Багги - 600.000.000$
🚗 10. Вездеход - 900.000.000$
🚗 11. Лада Xray - 1.400.000.000$
🚗 12. Audi Q7 - 2.500.000.000$
🚗 13. BMW X6 - 6.000.000.000$
🚗 14. Toyota FT-HS - 8.000.000.000$
🚗 15. BMW Z4 M - 10.000.000.000$
🚗 16. Subaru WRX STI - 40.000.000.000$
🚗 17. Lamborghini Veneno - 100.000.000.000$
🚗 18. Tesla Roadster - 300.000.000.000$
🚗 19. Yamaha YZF R6 - 500.000.000.000$
🚗 20. Bugatti Chiron - 700.000.000.000$
🚗 21. Thrust SSC - 900.000.000.000$
🚗 22. Ferrari LaFerrari - 2.100.000.000.000$
🚗 23. Koenigsegg Regear - 3.100.000.000.000$
🚗 24. Tesla Semi - 4.430.000.000.000$
🚗 25. Venom GT - 6.430.000.000.000$
🚗 26. Rolls-Royce - 9.430.000.000.000$

🛒 Для покупки машины введите "Купить машину [номер]"''')


@antispam
async def house_list(message: types.Message, user: EtherionUser):
    await message.answer(f'''{user.url}, доступные дома:
🏠 1. Коробка - 500.000$
🏠 2. Подвал - 1.000.000$
🏠 3. Сарай - 3.000.000$
🏠 4. Маленький домик - 5.000.000$
🏠 5. Квартира - 7.000.000$
🏠 6. Огромный дом - 10.000.000$
🏠 7. Коттедж - 50.000.000$
🏠 8. Вилла - 100.000.000$
🏠 9. Загородный дом - 5.000.000.000$
🏠 10. Небоскрёб - 50.000.000.000$
🏠 11. Дом на мальдивах - 200.000.000.000$
🏠 12. Технологичный небосрёб - 1.000.000.000.000$
🏠 13. Собственный остров - 5.000.000.000.000$
🏠 14. Дом на марсе - 15.000.000.000.000$
🏠 15. Остров на марсе - 25.000.000.000.000$
🏠 16. Свой марс - 50.000.000.000.000$

🛒 Для покупки дома введите "Купить дом [номер]"''')


@antispam
async def yahta_list(message: types.Message, user: EtherionUser):
    await message.answer(f'''{user.url}, доступные дома:
🏠 1. Коробка - 500.000$
🏠 2. Подвал - 1.000.000$
🏠 3. Сарай - 3.000.000$
🏠 4. Маленький домик - 5.000.000$
🏠 5. Квартира - 7.000.000$
🏠 6. Огромный дом - 10.000.000$
🏠 7. Коттедж - 50.000.000$
🏠 8. Вилла - 100.000.000$
🏠 9. Загородный дом - 5.000.000.000$
🏠 10. Небоскрёб - 50.000.000.000$
🏠 11. Дом на мальдивах - 200.000.000.000$
🏠 12. Технологичный небосрёб - 1.000.000.000.000$
🏠 13. Собственный остров - 5.000.000.000.000$
🏠 14. Дом на марсе - 15.000.000.000.000$
🏠 15. Остров на марсе - 25.000.000.000.000$
🏠 16. Свой марс - 50.000.000.000.000$

🛒 Для покупки дома введите "Купить дом [номер]"''')


@antispam
async def phone_list(message: types.Message, user: EtherionUser):
    await message.answer(f'''{user.url}, доступные телефоны:
📱 1. Nokia 3310 - 100.000$
📱 2. ASUS ZenFone 4 - 3.500.000$
📱 3. BQ Aquaris X - 10.000.000$
📱 4. Huawei P40 - 30.000.000$
📱 5. Samsung Galaxy S21 Ultra - 63.400.000$
📱 6. Xiaomi Mi 11 - 150.000.000$
📱 7. iPhone 11 Pro - 350.000.000$
📱 8. iPhone 12 Pro Max - 750.000.000$
📱 9. Blackberry - 1.240.000.000$

🛒 Для покупки телефона введите "Купить телефон [номер]"''')


@antispam
async def yahts_list(message: types.Message, user: EtherionUser):
    await message.answer(f'''{user.url}, доступные яхты:
🛳 1. Ванна - 1.000.000$
🛳 2. Nauticat 331 - 10.000.000$
🛳 3. Nordhavn 56 MS - 30.000.000$
🛳 4. Princess 60 - 100.000.000$
🛳 5. Bayliner 288 - 500.000.000$
🛳 6. Dominator 40M - 800.000.000$
🛳 7. Sessa Marine C42 - 5.000.000.000$
🛳 8. Wider 150 - 15.000.000.000$
🛳 9. Palmer Johnson 42M SuperSport - 40.000.000.000$
🛳 10. Serene - 90.000.000.000$
🛳 11. Dubai - 200.000.000.000$
🛳 12. Azzam - 600.000.000.000$
🛳 13. Streets of Monaco - 1.600.000.000.000$

🛒 Для покупки яхты введите "Купить яхту [номер]"''')


@antispam
async def plane_list(message: types.Message, user: EtherionUser):
    await message.answer(f'''{user.url}, доступные самолеты:
✈️ 1. Параплан - 100.000.000$
✈️ 2. АН-2 - 350.000.000$
✈️ 3. Cessna-172E - 700.000.000$
✈️ 4. BRM NG-5 - 1.000.000.000$
✈️ 5. Cessna T210 - 1.400.000.000$
✈️ 6. Beechcraft 1900D - 2.600.000.000$
✈️ 7. Cessna 550 - 5.500.000.000$
✈️ 8. Hawker 4000 - 8.800.000.000$
✈️ 9. Learjet 31 - 450.000.000.000$
✈️ 10. Airbus A318 - 800.000.000.000$
✈️ 11. F-35A - 1.600.000.000.000$
✈️ 12. Boeing 747-430 - 2.250.000.000.000$
✈️ 13. C-17A Globemaster III - 3.500.000.000.000$
✈️ 14. F-22 Raptor - 4.000.000.000.000$
✈️ 15. Airbus 380 Custom - 6.000.000.000.000$
✈️ 16. B-2 Spirit Stealth Bomber - 13.500.000.000.000$

🛒 Для покупки самолёта введите "Купить самолёт [номер]"''')


@antispam
async def my_helicopter(message: types.Message, user: EtherionUser):
    win, lose = EtherionConst.emj()
    
    if int(user.property.helicopter) == 0:
        await message.answer(f'{user.url}, к сожалению у вас нет вертолёта {lose}')
        return

    hdata = helicopters.get(user.property.helicopter.get())

    txt = f'''{user.url}, информация о вашем вертолёте "{hdata[0]}"
⛽️ Максимальная скорость: {hdata[1]} км/ч
🐎 Лошадиных сил: {hdata[2]}'''

    await message.answer_photo(photo=hdata[3], caption=txt)


@antispam
async def my_phone(message: types.Message, user: EtherionUser):
    win, lose = EtherionConst.emj()
    
    if int(user.property.phone) == 0:
        await message.answer(f'{user.url}, к сожалению у вас нет телефона {lose}')
        return

    hdata = phones.get(user.property.phone.get())
    await message.answer_photo(photo=hdata[1], caption=f'{user.url}, ваш телефон "{hdata[0]}"')


@antispam
async def my_car(message: types.Message, user: EtherionUser):
    win, lose = EtherionConst.emj()
    
    if int(user.property.car) == 0:
        await message.answer(f'{user.url}, к сожалению у вас нет автомобиля {lose}')
        return

    hdata = cars.get(user.property.car.get())

    txt = f'''{user.url}, информация о вашем автомобиле "{hdata[0]}"
⛽️ Максимальная скорость: {hdata[1]} км/ч
🐎 Лошадиных сил: {hdata[2]}
⏱ Разгон до 100 за {hdata[3]} сек'''

    await message.answer_photo(photo=hdata[4], caption=txt)


@antispam
async def my_house(message: types.Message, user: EtherionUser):
    win, lose = EtherionConst.emj()
    
    if int(user.property.house) == 0:
        await message.answer(f'{user.url}, к сожалению у вас нет своего дома {lose}')
        return

    hdata = house.get(user.property.house.get())
    await message.answer_photo(photo=hdata[1], caption=f'{user.url}, ваш дом "{hdata[0]}"')


@antispam
async def my_yahta(message: types.Message, user: EtherionUser):
    win, lose = EtherionConst.emj()
    
    if int(user.property.yahta) == 0:
        await message.answer(f'{user.url}, к сожалению у вас нет своей яхты {lose}')
        return

    hdata = yahts.get(user.property.yahta.get())

    txt = f'''{user.url}, информация о вашей яхте "{hdata[0]}"
⛽️ Максимальная скорость: {hdata[1]} км/ч
🐎 Лошадиных сил: {hdata[2]}'''

    await message.answer_photo(photo=hdata[3], caption=txt)


@antispam
async def my_plane(message: types.Message, user: EtherionUser):
    win, lose = EtherionConst.emj()
    
    if int(user.property.plane) == 0:
        await message.answer(f'{user.url}, к сожалению у вас нет своего самолёта {lose}')
        return

    hdata = planes.get(user.property.plane.get())

    txt = f'''{user.url}, информация о вашем самолёте "{hdata[0]}"
⛽️ Максимальная скорость: {hdata[1]} км/ч
🐎 Лошадиных сил: {hdata[2]}'''

    await message.answer_photo(photo=hdata[3], caption=txt)


@antispam
async def buy_helicopter(message: types.Message, user: EtherionUser):
    win, lose = EtherionConst.emj()
    
    if int(user.property.helicopter) != 0:
        await message.answer(f'{user.url}, у вас уже есть данный тип имущества {lose}')
        return

    try:
        num = int(message.text.split()[2])
    except:
        await message.answer(f'{user.url}, вы не ввели число имущества или привелегии которое хотите купить {lose}')
        return

    hdata = helicopters.get(num)
    
    if not hdata:
        await message.answer(f'{user.url}, вы не ввели число имущества или привелегии которое хотите купить {lose}')
        return

    if int(user.balance) < hdata[4]:
        await message.answer(f'{user.url}, у вас недостаточно денег для покупки имущества {lose}')
        return

    await message.answer(f'{user.url}, вы успешно купили вертолёт "{hdata[0]}" 🎉')
    await db.buy_property(user.user_id, num, 'helicopter', hdata[4])


@antispam
async def buy_phone(message: types.Message, user: EtherionUser):
    win, lose = EtherionConst.emj()
    
    if int(user.property.phone) != 0:
        await message.answer(f'{user.url}, у вас уже есть данный тип имущества {lose}')
        return

    try:
        num = int(message.text.split()[2])
    except:
        await message.answer(f'{user.url}, вы не ввели число имущества или привелегии которое хотите купить {lose}')
        return

    hdata = phones.get(num)
    
    if not hdata:
        await message.answer(f'{user.url}, вы не ввели число имущества или привелегии которое хотите купить {lose}')
        return

    if int(user.balance) < hdata[2]:
        await message.answer(f'{user.url}, у вас недостаточно денег для покупки имущества {lose}')
        return

    await message.answer(f'{user.url}, вы успешно купили телефон "{hdata[0]}" 🎉')
    await db.buy_property(user.user_id, num, 'phone', hdata[2])


@antispam
async def buy_car(message: types.Message, user: EtherionUser):
    win, lose = EtherionConst.emj()
    
    if int(user.property.car) != 0:
        await message.answer(f'{user.url}, у вас уже есть данный тип имущества {lose}')
        return

    try:
        num = int(message.text.split()[2])
    except:
        await message.answer(f'{user.url}, вы не ввели число имущества или привелегии которое хотите купить {lose}')
        return

    hdata = cars.get(num)
    
    if not hdata:
        await message.answer(f'{user.url}, вы не ввели число имущества или привелегии которое хотите купить {lose}')
        return

    if int(user.balance) < hdata[5]:
        await message.answer(f'{user.url}, у вас недостаточно денег для покупки имущества {lose}')
        return

    await message.answer(f'{user.url}, вы успешно купили машину "{hdata[0]}" 🎉')
    await db.buy_property(user.user_id, num, 'car', hdata[5])


@antispam
async def buy_house(message: types.Message, user: EtherionUser):
    win, lose = EtherionConst.emj()
    
    if int(user.property.house) != 0:
        await message.answer(f'{user.url}, у вас уже есть данный тип имущества {lose}')
        return

    try:
        num = int(message.text.split()[2])
    except:
        await message.answer(f'{user.url}, вы не ввели число имущества или привелегии которое хотите купить {lose}')
        return

    hdata = house.get(num)
    
    if not hdata:
        await message.answer(f'{user.url}, вы не ввели число имущества или привелегии которое хотите купить {lose}')
        return

    if int(user.balance) < hdata[2]:
        await message.answer(f'{user.url}, у вас недостаточно денег для покупки имущества {lose}')
        return

    await message.answer(f'{user.url}, вы успешно купили дом "{hdata[0]}" 🎉')
    await db.buy_property(user.user_id, num, 'house', hdata[2])


@antispam
async def buy_yahta(message: types.Message, user: EtherionUser):
    win, lose = EtherionConst.emj()
    
    if int(user.property.yahta) != 0:
        await message.answer(f'{user.url}, у вас уже есть данный тип имущества {lose}')
        return

    try:
        num = int(message.text.split()[2])
    except:
        await message.answer(f'{user.url}, вы не ввели число имущества или привелегии которое хотите купить {lose}')
        return

    hdata = yahts.get(num)
    
    if not hdata:
        await message.answer(f'{user.url}, вы не ввели число имущества или привелегии которое хотите купить {lose}')
        return

    if int(user.balance) < hdata[4]:
        await message.answer(f'{user.url}, у вас недостаточно денег для покупки имущества {lose}')
        return

    await message.answer(f'{user.url}, вы успешно купили яхту "{hdata[0]}" 🎉')
    await db.buy_property(user.user_id, num, 'yahta', hdata[4])


@antispam
async def buy_plane(message: types.Message, user: EtherionUser):
    win, lose = EtherionConst.emj()
    
    if int(user.property.plane) != 0:
        await message.answer(f'{user.url}, у вас уже есть данный тип имущества {lose}')
        return

    try:
        num = int(message.text.split()[2])
    except:
        await message.answer(f'{user.url}, вы не ввели число имущества или привелегии которое хотите купить {lose}')
        return

    hdata = planes.get(num)
    
    if not hdata:
        await message.answer(f'{user.url}, вы не ввели число имущества или привелегии которое хотите купить {lose}')
        return

    if int(user.balance) < hdata[4]:
        await message.answer(f'{user.url}, у вас недостаточно денег для покупки имущества {lose}')
        return

    await message.answer(f'{user.url}, вы успешно купили самолёт "{hdata[0]}" 🎉')
    await db.buy_property(user.user_id, num, 'plane', hdata[4])


@antispam
async def sell_helicopter(message: types.Message, user: EtherionUser):
    win, lose = EtherionConst.emj()
    
    if int(user.property.helicopter) == 0:
        await message.answer(f'{user.url}, у вас нет данного имущества {lose}')
        return

    hdata = helicopters.get(int(user.property.helicopter))
    
    summ = int(hdata[4] * 0.75)

    await message.answer(f'{user.url}, вы успешно продали вертолёт за {tr(summ)}$ 🎉')
    await db.sell_property(user.user_id, 'helicopter', summ)


@antispam
async def sell_phone(message: types.Message, user: EtherionUser):
    win, lose = EtherionConst.emj()
    
    if int(user.property.phone) == 0:
        await message.answer(f'{user.url}, у вас нет данного имущества {lose}')
        return

    hdata = phones.get(int(user.property.phone))
    summ = int(hdata[2] * 0.75)

    await message.answer(f'{user.url}, вы успешно продали телефон за {tr(summ)}$ 🎉')
    await db.sell_property(user.user_id, 'phone', summ)


@antispam
async def sell_car(message: types.Message, user: EtherionUser):
    win, lose = EtherionConst.emj()
    
    if int(user.property.car) == 0:
        await message.answer(f'{user.url}, у вас нет данного имущества {lose}')
        return

    hdata = cars.get(int(user.property.car))
    summ = int(hdata[5] * 0.75)

    await message.answer(f'{user.url}, вы успешно продали машину за {tr(summ)}$ 🎉')
    await db.sell_property(user.user_id, 'car', summ)


@antispam
async def sell_house(message: types.Message, user: EtherionUser):
    win, lose = EtherionConst.emj()
    
    if int(user.property.house) == 0:
        await message.answer(f'{user.url}, у вас нет данного имущества {lose}')
        return

    hdata = house.get(int(user.property.house))
    summ = int(hdata[2] * 0.75)

    await message.answer(f'{user.url}, вы успешно продали дом за {tr(summ)}$ 🎉')
    await db.sell_property(user.user_id, 'house', summ)


@antispam
async def sell_yahta(message: types.Message, user: EtherionUser):
    win, lose = EtherionConst.emj()
    
    if int(user.property.yahta) == 0:
        await message.answer(f'{user.url}, у вас нет данного имущества {lose}')
        return

    hdata = yahts.get(int(user.property.yahta))
    summ = int(hdata[4] * 0.75)

    await message.answer(f'{user.url}, вы успешно продали яхту за {tr(summ)}$ 🎉')
    await db.sell_property(user.user_id, 'yahta', summ)


@antispam
async def sell_plane(message: types.Message, user: EtherionUser):
    win, lose = EtherionConst.emj()
    
    if int(user.property.plane) == 0:
        await message.answer(f'{user.url}, у вас нет данного имущества {lose}')
        return

    hdata = planes.get(int(user.property.plane))
    summ = int(hdata[4] * 0.75)

    await message.answer(f'{user.url}, вы успешно продали самолёт за {tr(summ)}$ 🎉')
    await db.sell_property(user.user_id, 'plane', summ)


def reg(dp: Dispatcher):
    dp.register_message_handler(helicopters_list, lambda message: message.text.lower().startswith(('вертолеты', 'вертолёты')))
    dp.register_message_handler(cars_list, lambda message: message.text.lower().startswith('машины'))
    dp.register_message_handler(yahta_list, lambda message: message.text.lower().startswith('дома'))
    dp.register_message_handler(phone_list, lambda message: message.text.lower().startswith('телефоны'))
    dp.register_message_handler(plane_list, lambda message: message.text.lower().startswith(('самолеты', 'самолёты')))
    dp.register_message_handler(yahts_list, lambda message: message.text.lower().startswith('яхты'))

    dp.register_message_handler(my_helicopter, lambda message: message.text.lower().startswith(('мой вертолет', 'мой вертолёт')))
    dp.register_message_handler(my_phone, lambda message: message.text.lower().startswith('мой телефон'))
    dp.register_message_handler(my_car, lambda message: message.text.lower().startswith('моя машина'))
    dp.register_message_handler(my_house, lambda message: message.text.lower().startswith('мой дом'))
    dp.register_message_handler(my_yahta, lambda message: message.text.lower().startswith('моя яхта'))
    dp.register_message_handler(my_plane, lambda message: message.text.lower().startswith(('мой самолет', 'мой самолёт')))

    dp.register_message_handler(buy_helicopter, lambda message: message.text.lower().startswith(('купить вертолет', 'купить вертолёт')))
    dp.register_message_handler(buy_phone, lambda message: message.text.lower().startswith('купить телефон'))
    dp.register_message_handler(buy_car, lambda message: message.text.lower().startswith('купить машину'))
    dp.register_message_handler(buy_house, lambda message: message.text.lower().startswith('купить дом'))
    dp.register_message_handler(buy_yahta, lambda message: message.text.lower().startswith('купить яхту'))
    dp.register_message_handler(buy_plane, lambda message: message.text.lower().startswith(('купить самолет', 'купить самолёт')))

    dp.register_message_handler(sell_helicopter, lambda message: message.text.lower().startswith(('продать вертолет', 'продать вертолёт')))
    dp.register_message_handler(sell_phone, lambda message: message.text.lower().startswith('продать телефон'))
    dp.register_message_handler(sell_car, lambda message: message.text.lower().startswith('продать машину'))
    dp.register_message_handler(sell_house, lambda message: message.text.lower().startswith('продать дом'))
    dp.register_message_handler(sell_yahta, lambda message: message.text.lower().startswith('продать яхту'))
    dp.register_message_handler(sell_plane, lambda message: message.text.lower().startswith(('продать самолет', 'продать самолёт')))
