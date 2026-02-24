from aiogram import Dispatcher, types

from assets import kb
from assets.transform import transform_int as tr
from assets.antispam import antispam_earning, new_earning, antispam
from commands.entertaining.earnings.farm import db
from user import EtherionUser, EtherionConst


@antispam
async def ferma_list_cmd(message: types.Message, user: EtherionUser):
    await message.answer(f'''{user.url}, с данного момента ты можешь сам построить свою ферму и улучшать её. Это очень весело и облегчит тебе работу.

🪓 Для начала тебе нужно будет создать свою ферму, цена постройки 500.000.000$. Введите команду "Построить ферму" и после через команду "Моя ферма" вы сможете настраивать её и улучшать повышая свою прибыль.

📎 Чтобы узнать все команды ферм введите команду "Помощь" и выберите соответствующую кнопку.''')


@antispam
async def my_ferma_cmd(message: types.Message, user: EtherionUser):
    win, lose = EtherionConst.emj()
    ferma = user.ferma

    if not ferma:
        await message.answer(f'{user.url}, у вас нет своей фермы чтобы построить введите команду "Построить ферму" {lose}')
        return
    
    await upd_ferma_text(message, user, action='send')


async def upd_ferma_text(call: types.CallbackQuery | types.Message, user: EtherionUser, action='edit') -> None:
    ferma = user.ferma
    
    if action == 'edit':
        await user.update()

    dox = int(3000 * (ferma.cards.get() ** 2.5)) if ferma.cards.get() != 0 else 3000
    ch = int(500000000 * (1 + 0.15) ** ferma.cards.get())

    txt = f'''{user.url}, информация о вашей "Майнинг ферма":
💷 Доход: {tr(dox)}฿/час
📝 Видеокарты: {ferma.cards.tr()} шт./♾️ шт.
🆙 для следующего уровня: {tr(ch)}$

💸 Налоги: {ferma.nalogs.tr()}$/5.000.000$
💰 На счету: {ferma.balance.tr()}฿'''
    
    try:
        if action == 'edit':
            await call.message.edit_text(text=txt, reply_markup=kb.ferma(user.id))
        else:
            msg = await call.answer(text=txt, reply_markup=kb.ferma(user.id))
            await new_earning(msg)
    except:
        return


@antispam
async def buy_ferma_cmd(message: types.Message, user: EtherionUser):
    win, lose = EtherionConst.emj()
    ferma = user.ferma
    
    if ferma:
        await message.answer(f'{user.url}, у вас уже есть построенная ферма. Чтобы узнать подробнее, введите "Моя ферма" {lose}')
        return
    
    if int(user.balance) < 500_000_000:
        await message.answer(f'{user.url}, у вас недостаточно денег для постройки фермы. Её стоимость 500.000.000$ {lose}')
        return
        
    await db.buy_ferma(user.id)
    await message.answer(f'{user.url}, вы успешно купили ферму для подробностей введите "Моя ферма" {win}')


@antispam_earning
async def buy_cards_cmd(call: types.CallbackQuery, user: EtherionUser):
    win, lose = EtherionConst.emj()
    ferma = user.ferma

    if not ferma:
        return

    ch = int(500_000_000 * (1 + 0.15) ** (ferma.cards.get() - 1))
    
    if int(user.balance) < ch:
        await call.answer(f'{user.name}, у вас недостаточно денег для увеличения видеокарт. Её стоимость {tr(ch)}$ {lose}')
        return
    
    await db.buy_cards(user.id, ch)
    await call.answer(f'{user.name}, вы успешно увеличили количество видеокарт в ферме за {tr(ch)}$ {win}')
    await upd_ferma_text(call, user)


@antispam_earning
async def withdraw_profit_cmd(call: types.CallbackQuery, user: EtherionUser):
    win, lose = EtherionConst.emj()
    ferma = user.ferma

    if not ferma:
        return

    if int(ferma.balance) == 0:
        await call.answer(f'{user.name}, на данный момент на балансе вашей фермы нет прибыли {lose}')
        return
    
    await db.withdraw_profit(user.id, ferma.balance.get())
    await call.answer(f'{user.name}, вы успешно сняли {ferma.balance.tr()}฿ с баланса вашей фермы {win}')
    await upd_ferma_text(call, user)


@antispam_earning
async def payment_taxes_cmd(call: types.CallbackQuery, user: EtherionUser):
    win, lose = EtherionConst.emj()
    ferma = user.ferma

    if not ferma:
        return

    if int(user.balance) < int(ferma.nalogs):
        await call.answer(f'{user.name}, у вас недостаточно денег чтоб оплатить налоги {lose}')
        return

    if int(ferma.nalogs) == 0:
        await call.answer(f'{user.name}, у вас нет налогов чтобы их оплатить {win}')
        return

    await db.pay_taxes(user.id, ferma.nalogs.get())
    await call.answer(f'{user.name}, вы успешно оплатили налоги на сумму {ferma.nalogs.tr()}$ с вашего игрового баланса {win}')
    await upd_ferma_text(call, user)


@antispam
async def sell_ferma_cmd(message: types.Message, user: EtherionUser):
    win, lose = EtherionConst.emj()
    ferma = user.ferma
    
    if not ferma:
        await message.answer(f'{user.url}, у вас нет своей фермы чтобы построить введите команду "Построить ферму" {lose}')
        return
    
    summ = 250_000_000  # Половина стоимости фермы
    
    for i in range(1, ferma.cards.get() + 1):  # Компенсация за видеокарты (50%)
        summ += int(500_000_000 * (1 + 0.15) ** (i - 1)) // 2
        
    await db.sell_ferma(user.id, summ)
    await message.answer(f'{user.url}, Вы успешно продали свою ферму за {tr(summ)}$ {win}')
    

def reg(dp: Dispatcher):
    dp.register_message_handler(my_ferma_cmd, lambda message: message.text.lower() == 'моя ферма')
    dp.register_message_handler(ferma_list_cmd, lambda message: message.text.lower() == ('ферма', 'фермы'))
    dp.register_message_handler(buy_ferma_cmd, lambda message: message.text.lower() == 'построить ферму')
    dp.register_callback_query_handler(buy_cards_cmd, text_startswith='ferma-bycards')
    dp.register_callback_query_handler(withdraw_profit_cmd, text_startswith='ferma-sobrat')
    dp.register_callback_query_handler(payment_taxes_cmd, text_startswith='ferma-nalog')
    dp.register_message_handler(sell_ferma_cmd, lambda message: message.text.lower() == 'продать ферму')
