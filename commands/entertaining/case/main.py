import random
from aiogram import Dispatcher, types
import commands.entertaining.case.db as db
from assets.transform import transform_int as tr
from assets.antispam import antispam
from user import EtherionUser, EtherionConst


@antispam
async def my_cases_cmd(message: types.Message, user: EtherionUser):
    ycase = {
        "case1": {"name": "📦 Обычный кейс", "quantity": user.case[1].get()},
        "case2": {"name": "🏵 Золотой кейс", "quantity": user.case[2].get()},
        "case3": {"name": "🏺 Рудный кейс", "quantity": user.case[3].get()},
        "case4": {"name": "🌌 Материальный кейс", "quantity": user.case[4].get()},
    }

    positive_resources = {name: info for name, info in ycase.items() if info["quantity"] > 0}

    if positive_resources:
        result_message = "\n".join(
            [f'{info["name"]} - {tr(info["quantity"])} шт.' for name, info in positive_resources.items()])
        txt = f"{result_message}\n\n🔐 Для открытия кейсов используйте - «Кейс открыть [1/2/3/4] [кол-во]»"
    else:
        txt = f"😕 У вас нету кейсов."

    await message.answer(f'''{user.url}, доступные кейсы:
🎁 1. Обычный кейс — 750 квдр $
🎁 2. Золотой кейс - 5 квнт $
🎁 3. Рудный кейс - 50 ⚙️
🎁 4. Материальный кейс - 200 🌌

{txt}
🛒 Для покупки введите «Купить кейс [1/2/3] [кол-во]»

{EtherionConst.ads}''')


@antispam
async def buy_case_cmd(message: types.Message, user: EtherionUser):
    win, lose = EtherionConst.emj()
    
    try:
        case = int(message.text.split()[2])
    except:
        await message.answer(f'{user.url}, вы ввели не числовые данные для покупки кейсов {lose}')
        return
    
    try:
        amount = int(message.text.split()[3])
    except:
        amount = 1
    
    if amount <= 0:
        return
    
    if case == 1:
        summ = 750_000_000_000_000_000 * amount
        
        if summ > int(user.balance):
            await message.answer(f'{user.url}, у вас недостаточно средств для покупки данного кейса {lose}')
            return
        
        await user.case[1].upd(amount, '+')
        await user.balance.upd(summ, '-')
        await message.answer(f'{user.url}, вы успешно купили {amount} «Обычный кейс» за {tr(summ)}$ ✅')
    
    elif case == 2:
        summ = 5_000_000_000_000_000_000 * amount
        
        if summ > int(user.balance):
            await message.answer(f'{user.url}, у вас недостаточно средств для покупки данного кейса {lose}')
            return
        
        await user.case[2].upd(amount, '+')
        await user.balance.upd(summ, '-')
        await message.answer(f'{user.url}, вы успешно купили {amount} «Золотой кейс» за {tr(summ)}$ ✅')
    
    elif case == 3:
        summ = 50 * case
        
        if summ > int(user.mine.titanium):
            await message.answer(f'{user.url}, у вас недостаточно средств для покупки данного кейса {lose}')
            return
        
        await message.answer(f'{user.url}, вы успешно купили {case} «Рудный кейс» за {tr(summ)}⚙️ ✅')
        await user.case[3].upd(amount, '+')
        await user.mine.titanium.upd(summ, '-')
    
    elif case == 4:
        summ = 200 * case
        
        if summ > int(user.mine.matter):
            await message.answer(f'{user.url}, у вас недостаточно средств для покупки данного кейса {lose}')
            return
        
        await message.answer(f'{user.url}, вы успешно купили {case} «Материальный кейс» за {tr(summ)}🌌 ✅')
        await user.case[4].upd(amount, '+')
        await user.mine.matter.upd(summ, '-')


@antispam
async def open_case_cmd(message: types.Message, user: EtherionUser):
    win, lose = EtherionConst.emj()

    try:
        case = int(message.text.split()[2])
    except:
        await message.answer(f'{user.url}, к сожалению вы ввели неверный номер кейса {lose}')
        return

    if case not in range(1, 5):
        await message.answer(f'{user.url}, к сожалению вы ввели неверный номер кейса {lose}')
        return

    try:
        amount = int(message.text.split()[3])
    except:
        amount = 1

    ncase = int({1: user.case[1], 2: user.case[2], 3: user.case[3], 4: user.case[4]}.get(case, 0))
    climit = {0: 10, 1: 20, 2: 40, 3: 60, 4: 100}.get(user.status, 10)

    if amount <= 0:
        await message.answer(f'🎁 | {user.url}, нельзя открывать отрицательное количество кейсов! {lose}\n\n{EtherionConst.ads}')
        return

    if ncase < amount:
        await message.answer(f'🎁 | {user.url}, у вас недостаточно кейсов! {lose}\n\n{EtherionConst.ads}')
        return

    if climit < amount:
        await message.answer(f'🎁 | {user.url}, вы не можете открывать более {climit} кейсов за раз! {lose}\n\n{EtherionConst.ads}')
        return

    await open_case_logic(message, amount, case, user)
    
    
async def open_case_logic(message: types.Message, amount: int, case: int, user: EtherionUser) -> None:
    coff = 11 if case == 2 else 1
    smoney = srating = sexpe = stitan = spalladium = smatter = 0
    txt = ''
    
    for _ in range(amount):
        prize = random.randint(1, 100)

        if case in [1, 2]:
            if prize in range(1, 45):
                smoney += random.randint(100_000_000_000_000_000, 1_000_000_000_000_000_000) * coff
            elif prize in range(45, 70):
                srating += random.randint(5_000_000, 150_000_000) * coff
            else:
                sexpe += random.randint(100, 250) * coff
                
        elif case == 3:
            if prize in range(1, 5):
                spalladium += random.randint(1, 3)
            if prize in range(5, 30):
                smoney += random.randint(100_000_000_000_000_000, 1_000_000_000_000_000_000)
            elif prize in range(30, 60):
                srating += random.randint(5_000_000, 150_000_000)
            elif prize in range(60, 80):
                stitan += random.randint(30, 80)
            else:
                sexpe += random.randint(100, 250)
                
        elif case == 4:
            if prize in range(1, 30):
                smoney += random.randint(100_000_000_000_000_000, 1_000_000_000_000_000_000)
            elif prize in range(30, 60):
                srating += random.randint(5_000_000, 150_000_000)
            elif prize in range(60, 80):
                smatter += random.randint(30, 80)
            else:
                sexpe += random.randint(100, 250)
                
    if smoney > 0:
        await db.open_case_db(user.user_id, smoney, 'balance')
        txt += f'🔥 Итого денег - {tr(smoney)}$\n'

    if srating > 0:
        await db.open_case_db(user.user_id, srating, 'rating')
        txt += f'👑 Итого рейтинга - {tr(srating)}\n'

    if sexpe > 0:
        await db.open_case_db(user.user_id, sexpe, 'exp')
        txt += f'🏆 Итого опыта - {tr(sexpe)}шт\n'

    if stitan > 0:
        await db.open_case_db(user.user_id, stitan, 'titanium', table='mine')
        txt += f'⚙️ Итого титана - {tr(stitan)}шт\n'

    if spalladium > 0:
        await db.open_case_db(user.user_id, spalladium, 'palladium', table='mine')
        txt += f'⚗️ Итого палладия - {tr(spalladium)}шт\n'
        
    if smatter > 0:
        await db.open_case_db(user.user_id, smatter, 'matter', table='mine')
        txt += f'🌌 Итого материи - {tr(smatter)}шт\n'

    await db.open_case2_db(user.user_id, amount, f'case{case}')
    await message.answer(f'🎁 | {user.url}, вам выпало:\n\n{txt}\n\n{EtherionConst.ads}')


def reg(dp: Dispatcher):
    dp.register_message_handler(my_cases_cmd, lambda message: message.text.lower() == 'кейсы')
    dp.register_message_handler(buy_case_cmd, lambda message: message.text.lower().startswith('купить кейс'))
    dp.register_message_handler(open_case_cmd, lambda message: message.text.lower().startswith('открыть кейс'))
