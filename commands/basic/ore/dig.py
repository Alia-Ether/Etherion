import random

from aiogram import types, Dispatcher

from assets.transform import transform_int as tr
from user import EtherionUser, EtherionConst
from assets.antispam import antispam
from commands.basic.ore import db


@antispam
async def energy_cmd(message: types.Message, user: EtherionUser):
    await message.answer(f'{user.url}, на данный момент у тебя {user.energy} ⚡')


@antispam
async def mine_cmd(message: types.Message, user: EtherionUser):
    await message.answer(f'''{user.url}, добро пожаловать на вашу шахту! 🏞️

Здесь вы можете добывать различные ресурсы для продажи, используя свою энергию ⚡.

✨ Для добычи ресурсов используйте:- копать железо
- копать золото
- копать алмазы
- копать аметисты
- копать аквамарин
- копать изумруды
- копать материю
- копать плазму
- копать никель
- копать титан
- копать кобальт
- копать эктоплазму
<b>«Статусы» увеличивают количество выпадаемой руды и получаемого опыта.</b>

🛒 Для продажи ресурсов:
- продать железо
- продать золото
- продать алмазы
- продать аметисты
- продать аквамарин
- продать изумруды
- продать материю
- продать плазму
- продать никель
- продать титан
- продать кобальт
- продать эктоплазму
- продать палладий

📊 Для статистики:
- Моя шахта''')


@antispam
async def price_cmd(message: types.Message, user: EtherionUser):
    await message.answer(f'''{user.url}, курс руды:
⛓ 1 железо - 230.000$
🌕 1 золото - 1.000.000$
💎 1 алмаз - 116.000.000$
🎆 1 аметист - 217.000.000$
💠 1 аквамарин - 461.000.000$
🍀 1 изумруд - 792.000.000$
🌌 1 материя - 8.000.000.000$
💥 1 плазма - 12.000.000.000$
🪙 1 никель - 30.000.000.000$
⚙ 1 титан - 70.000.000.000.000$
🧪 1 кобальт - 120.000.000.000.000$
☄️ 1 эктоплазма - 270.000.000.000.000$
⚗ 1 палладий - 2.000.000.000.000.000$''')


@antispam
async def inventary_cmd(message: types.Message, user: EtherionUser):
    resources = {
        "iron": {"name": "⛓ Железо", "quantity": user.mine.iron},
        "gold": {"name": "🌕 Золото", "quantity": user.mine.gold},
        "diamond": {"name": "💎 Алмаз", "quantity": user.mine.diamond},
        "amethyst": {"name": "🎆 Аметист", "quantity": user.mine.amestit},
        "aquamarine": {"name": "💠 Аквамарин", "quantity": user.mine.aquamarine},
        "emeralds": {"name": "🍀 Изумруд", "quantity": user.mine.emeralds},
        "matter": {"name": "🌌 Материя", "quantity": user.mine.matter},
        "plasma": {"name": "💥 Плазма", "quantity": user.mine.plasma},
        "nickel": {"name": "🪙 Никель", "quantity": user.mine.nickel},
        "titanium": {"name": "⚙️ Титан", "quantity": user.mine.titanium},
        "cobalt": {"name": "🧪 Кобальт", "quantity": user.mine.cobalt},
        "ectoplasm": {"name": "☄️ Эктоплазма", "quantity": user.mine.ectoplasm},
        "palladium": {"name": "⚗️ Палладий", "quantity": user.mine.palladium},
        "corn": {"name": "🥜 Зёрна", "quantity": user.corn},
        "biores": {"name": "☣️ Биоресурсы", "quantity": user.biores},
    }

    positive_resources = {name: info for name, info in resources.items() if int(info["quantity"]) > 0}

    if positive_resources:
        result_message = "\n".join([f'{info["name"]}: {int(info["quantity"]):,} шт.' for name, info in positive_resources.items()])
        await message.answer(f"{user.url},\n{result_message}")
    else:
        await message.answer(f"{user.url}, ваш инвентарь пуст.")


def mine_level(expe: int) -> tuple:
    levels = [
        ('Эктоплазма ☄️', 'SOON...', '???', 10000000000),
        ('Кобаль 🧪', 'Эктоплазма ☄️', '10.000.000.000', 20000000),
        ('Титан ⚙️', 'Кобаль 🧪', '20.000.000', 5000000),
        ('Никель 🪙', 'Титан ⚙️', '5.000.000', 950000),
        ('Плазма 💥', 'Никель 🪙', '950.000', 500000),
        ('Материя 🌌', 'Плазма 💥', '500.000', 100000),
        ('Изумруд 🍀', 'Материя 🌌', '100.000', 60000),
        ('Аквамарин 💠', 'Изумруд 🍀', '60.000', 25000),
        ('Аметист 🎆', 'Аквамарин 💠', '25.000', 10000),
        ('Алмазы 💎', 'Аметист 🎆', '10.000', 2000),
        ('Золото 🌕', 'Алмазы 💎', '2.000', 500),
        ('Железо ⛓', 'Золото 🌕', '500', 0)
    ]

    for level, next_level, limit, threshold in levels:
        if int(expe) >= threshold:
            return level, next_level, limit


@antispam
async def my_mine_cmd(message: types.Message, user: EtherionUser):
    mine_level_t, mine_level_s, opit = mine_level(user.expe)

    await message.answer(f'''{user.url}, это ваш профиль шахты:
🏆 Опыт: {user.expe.tr()}
⚡ Энергия: {user.energy}
⛏ Ваш уровень: {mine_level_t}
➡ Следующий уровень: {mine_level_s}
⭐️ Требуется {opit} опыта''')


@antispam
async def dig_mine_cmd(message: types.Message, user: EtherionUser):
    ads = EtherionConst.ads
    win, lose = EtherionConst.emj()

    if int(user.energy) <= 0:
        await message.answer(f'{user.url}, у вас недостаточно энергии для копки {lose}')
        return

    status_limits = {0: 1, 1: 2, 2: 3, 3: 5, 4: 10}
    coff = status_limits.get(user.status, status_limits[0])

    txt = message.text.split()
    
    if len(txt) < 2:
        await message.answer(f'{user.url}, данной руды не существует {lose}')
        return
 
    ruda = txt[1].lower()

    ruda_data = {
        'железо': ('iron', 40, 1, 0),
        'золото': ('gold', 4, 3, 500),
        'алмазы': ('diamond', 2, 5, 2000),
        'аметисты': ('amethyst', 1, 15, 10000),
        'аквамарин': ('aquamarine', 1, 30, 25000),
        'изумруды': ('emeralds', 1, 55, 60000),
        'материю': ('matter', 1, 65, 100000),
        'плазму': ('plasma', 1, 180, 500000),
        'никель': ('nickel', 1, 500, 950000),
        'титан': ('titanium', 1, 2300, 5000000),
        'кобальт': ('cobalt', 1, 3600, 20000000),
        'эктоплазму': ('ectoplasm', 1, 7200, 10000000000)
    }

    if ruda in ruda_data:
        eng_ruda, min_i, op, min_expe = ruda_data[ruda]
        if user.expe.get() < min_expe:
            await message.answer(f'{user.url}, чтобы копать {ruda} вам требуется {tr(min_expe)} опыта {lose}')
            return

        i = random.randint(min_i, min_i + 5) * coff
        await db.digdb(i, user.user_id, eng_ruda, op)
        opit = user.expe.get() + op

        await message.answer(f'{user.url}, +{i} {ruda}.\n💡 Энергия: {user.energy.get() - 1}, опыт: {tr(opit)}\n\n{ads}')
    else:
        await message.answer(f'{user.url}, данной руды не существует {lose}')


@antispam
async def sell_cmd(message: types.Message, user: EtherionUser):
    user_id = message.from_user.id
    txt = message.text.split()
    win, lose = EtherionConst.emj()

    if len(txt) < 2:
        return
    
    ruda = txt[1].lower()

    ruda_data = {
        'железо': ('iron', 230000, user.mine.iron),
        'золото': ('gold', 1000000, user.mine.gold),
        'алмазы': ('diamond', 116000000, user.mine.diamond),
        'аметисты': ('amestit', 217000000, user.mine.amestit),
        'аквамарин': ('aquamarine', 461000000, user.mine.aquamarine),
        'изумруды': ('emeralds', 792000000, user.mine.emeralds),
        'материю': ('matter', 8000000000, user.mine.matter),
        'плазму': ('plasma', 12000000000, user.mine.plasma),
        'никель': ('nickel', 30000000000, user.mine.nickel),
        'титан': ('titanium', 70000000000000, user.mine.titanium),
        'кобальт': ('cobalt', 120000000000000, user.mine.cobalt),
        'эктоплазму': ('ectoplasm', 270000000000000, user.mine.ectoplasm),
        'палладий': ('palladium', 2000000000000000, user.mine.palladium)
    }

    if ruda in ruda_data:
        balance = int(ruda_data[ruda][2])
        if len(txt) >= 3:
            try:
                kolvo = int(txt[2].lower())
            except:
                return
        else:
            kolvo = int(balance)

        if kolvo <= 0 or kolvo > balance:
            await message.answer(f'{user.url}, у вас недостаточно {ruda} {lose}')
            return

        i = kolvo * int(ruda_data[ruda][1])
        await db.sell_ruda_db(i, user_id, ruda_data[ruda][0], kolvo)
        await message.answer(f'{user.url}, вы продали {kolvo} {ruda} за {tr(i)}$ ✅')


ruds = ['железо', 'золото', 'алмазы', 'аметисты', 'аквамарины', 'изумруды', 'материю',
        'плазму', 'никель', 'титан', 'кобальт', 'эктоплазму', 'палладий']


def reg(dp: Dispatcher):
    dp.register_message_handler(mine_cmd, lambda message: message.text.lower() == 'шахта')
    dp.register_message_handler(energy_cmd, lambda message: message.text.lower() == 'энергия')
    dp.register_message_handler(price_cmd, lambda message: message.text.lower() == 'курс руды')
    dp.register_message_handler(my_mine_cmd, lambda message: message.text.lower() == 'моя шахта')
    dp.register_message_handler(dig_mine_cmd, lambda message: message.text.lower().startswith('копать '))
    dp.register_message_handler(sell_cmd, lambda message: message.text.lower().startswith('продать') and any(ruda in message.text.lower() for ruda in ruds))
    dp.register_message_handler(inventary_cmd, lambda message: message.text.lower() == 'инвентарь')
