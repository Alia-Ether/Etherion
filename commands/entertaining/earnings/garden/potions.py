from aiogram import Dispatcher, types

from commands.entertaining.earnings.garden import db
from assets.antispam import antispam
from user import EtherionUser, EtherionConst


@antispam
async def potions_list(message: types.Message, user: EtherionUser):
    await message.answer(f'''{user.url}, доступные зелья:
🍸 1. Чай: 40 зёрен
Прибыль: 1 энергия

🍸 2. Чефир: 240 зёрен
Прибыль: 5 энергии

🍸 3. Кофе: 520 зёрен
Прибыль: 10 энергии

🍸 4. Энергетик: 1.120 зёрен
Прибыль: 20 энергии

🍸 5. Крепкий кофе: 2.400 зёрен
Прибыль: 40 энергии

🍸 6. Настойка из вишни: 3.000 зёрен
Прибыль: 50 энергии

🍸 7. Сыворотка из плазмы: 30.000 зёрен
Прибыль: 400 энергии

🛒 Для покупки зелья введите "Создать зелье [номер]"
⛔ При покупке зелья энергия начисляется сразу.''')


@antispam
async def bay_potions(message: types.Message, user: EtherionUser):
    win, lose = EtherionConst.emj()

    potions = {
        1: {"name": "Чай", "summ": 1, "st": 40},
        2: {"name": "Чефир", "summ": 5, "st": 240},
        3: {"name": "Кофе", "summ": 10, "st": 520},
        4: {"name": "Энергетик", "summ": 20, "st": 1120},
        5: {"name": "Крепкий кофе", "summ": 40, "st": 2400},
        6: {"name": "Настойка из вишни", "summ": 50, "st": 3000},
        7: {"name": "Сыворотка из плазмы", "summ": 400, "st": 30000}
    }

    try:
        n = int(message.text.split()[2])
        potion = potions[n]
    except:
        await message.answer(f'{user.url}, вы ввели неверный номер зелья или не ввели его вовсе. {lose}')
        return

    if user.corn < potion["st"]:
        await message.answer(f'{user.url}, у вас недостаточно зёрен для создания данного зелья. {lose}')
        return

    await message.answer(f'{user.url}, вы успешно создали "{potion["name"]}", вам начислено {potion["summ"]} энергии. {win}')
    await db.buy_postion(potion["summ"], potion["st"], user.user_id)


def reg(dp: Dispatcher):
    dp.register_message_handler(potions_list, lambda message: message.text.lower() == 'зелья')
    dp.register_message_handler(bay_potions, lambda message: message.text.lower().startswith('создать зелье'))
