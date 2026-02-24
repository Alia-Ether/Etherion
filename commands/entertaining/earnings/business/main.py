from aiogram import Dispatcher, types
from assets import kb
from assets.transform import transform_int as tr
from assets.antispam import antispam_earning, new_earning, antispam
from commands.entertaining.earnings.business import db
from user import EtherionUser, EtherionConst


@antispam
async def business_info(message: types.Message, user: EtherionUser):
    await message.answer(f'''{user.url}, теперь ты можешь принимать решения сам и влиять на свой бизнес.

🪓 Для начала я проведу тебе маленький инструктаж по поводу данных бизнесов, ты не можешь просто купить бизнес и начать зарабатывать на нём. Теперь вам предоставлена возможность самому влиять на доход, увеличить территорию бизнеса, закупать продукты и платить налоги в казну штата.

🏗 Для начала вам потребуется построить площадку для того чтобы возвести на ней свой бизнес. Для этого используйте команду "Построить бизнес", после этого вами будет куплена маленькая территория под бизнес.

💫 Далее вы можете при помощи команд управлять бизнесом, увеличивать его доход, покупать улучшения и прочее. Чтобы узнать все команды введите команду "Помощь" и выберите соответствующую кнопку.''')


@antispam
async def my_business(message: types.Message, user: EtherionUser):
    business = user.business
    win, lose = EtherionConst.emj()
    
    if not business:
        await message.answer(f'{user.url}, у вас нет своего бизнеса чтобы построить введите команду "Построить бизнес" {lose}')
        return

    await upd_business_text(message, user, action='send')


async def upd_business_text(call: types.CallbackQuery | types.Message, user: EtherionUser, action='edit'):
    business = user.business
    
    if action == 'edit':
        await user.update()

    dox = int(90000000 * business.bsterritory.get() / 15)
    ch = int(22000000 * (1 + 0.15) ** (business.territory.get() - 4))
    ch2 = int(22000000 * (1 + 0.15) ** (business.bsterritory.get() - 1))

    txt = f'''{user.url}, информация о вашем бизнесе "Бизнес":
🧱 Территория: {business.territory.tr()} м²
🆙 для следующего уровня: {tr(ch)}$
🏢 Территория бизнеса: {business.bsterritory.tr()} м²
🆙 для следующего уровня: {tr(ch2)}$

💷 Доход: {tr(dox)}$
💸 Налоги: {business.nalogs.tr()}$/5.000.000$
💰 Прибыль: {business.balance.tr()}$'''
    
    try:
        if action == 'edit':
            await call.message.edit_text(text=txt, reply_markup=kb.business(user.id))
        else:
            msg = await call.answer(text=txt, reply_markup=kb.business(user.id))
            await new_earning(msg)
    except:
        return


@antispam
async def buy_business(message: types.Message, user: EtherionUser):
    win, lose = EtherionConst.emj()
    business = user.business

    if business:
        await message.answer(f'{user.url}, у вас уже есть построенная территория под бизнес. Чтобы узнать подробнее, введите "Мой бизнес" {lose}')
        return

    if int(user.balance) < 500_000_000:   # при изменении стоимости, меняйте ее также в бд...
        await message.answer(f'{user.url}, у вас недостаточно денег для постройки территории бизнеса. Её стоимость 500 млн$ {lose}')
        return

    await db.buy_business(user.id)  # <- тута
    await message.answer(f'{user.url}, вы успешно построили свой бизнес для подробностей введите "Мой бизнес" {win}')


@antispam_earning
async def buy_territory(call: types.CallbackQuery, user: EtherionUser):
    win, lose = EtherionConst.emj()
    business = user.business

    if not business:
       return

    ch = int(22000000 * (1 + 0.15) ** (business.territory.get() - 4))

    if int(user.balance) < ch:
        await call.answer(f'{user.name}, у вас недостаточно денег на балансе чтобы увеличить территорию бизнеса {lose}')
        return
        
    await db.buy_territory(user.id, ch)
    await call.answer(f'{user.name}, вы успешно увеличили территорию бизнеса на 1 м² за {tr(ch)}$ {win}')
    await upd_business_text(call, user)


@antispam_earning
async def buy_bsterritory(call: types.CallbackQuery, user: EtherionUser):
    win, lose = EtherionConst.emj()
    business = user.business

    if not business:
        return

    if business.territory.get() <= business.bsterritory.get():
        await call.answer(f'{user.name}, чтобы увеличить бизнес для начала увеличьте его территорию {lose}')
        return

    ch = int(22000000 * (1 + 0.15) ** (business.bsterritory.get() - 1))

    if int(user.balance) < ch:
        await call.answer(f'{user.name}, у вас недостаточно денег на балансе чтобы увеличить бизнес {lose}')
        return

    await db.buy_bsterritory(user.id, ch)
    await call.answer(f'{user.name}, вы успешно увеличили бизнес на 1 м² за {tr(ch)}$ {win}')
    await upd_business_text(call, user)


@antispam_earning
async def withdraw_profit(call: types.CallbackQuery, user: EtherionUser):
    win, lose = EtherionConst.emj()
    business = user.business

    if not business:
        return

    if business.balance.get() == 0:
        await call.answer(f'{user.name}, на данный момент на балансе вашего бизнеса нет прибыли {lose}')
        return

    await db.withdraw_profit(user.id, business.balance.get())
    await call.answer(f'{user.name}, вы успешно сняли {business.balance.tr()}$ с баланса вашего бизнеса {win}')
    await upd_business_text(call, user)


@antispam_earning
async def payment_taxes(call: types.CallbackQuery, user: EtherionUser):
    win, lose = EtherionConst.emj()
    business = user.business
    
    if not business:
        return

    if int(user.balance) < int(business.nalogs):
        await call.answer(f'{user.name}, у вас недостаточно денег чтоб оплатить налоги {lose}')
        return

    if business.nalogs.get() == 0:
        await call.answer(f'{user.name}, у вас нет налогов чтобы их оплатить {win}')
        return

    await db.payment_taxes(user.id, business.nalogs.get())
    await call.answer(f'{user.name}, вы успешно оплатили налоги на сумму {business.nalogs.tr()}$ с вашего игрового баланса {win}')
    await upd_business_text(call, user)
    
    
@antispam
async def sell_business(message: types.Message, user: EtherionUser):
    win, lose = EtherionConst.emj()
    business = user.business
    
    if not business:
        await message.answer(f'{user.url}, у вас нет своего бизнеса чтобы построить введите команду "Построить бизнес" {lose}')
        return
    
    summ = 250_000_000  # Половина стоимости бизнеса
    
    for i in range(6, business.territory.get() + 1):  # Компенсация за территорию (50%)
        summ += int(22_000_000 * (1 + 0.15) ** (i - 4)) // 2
        
    for i in range(6, business.bsterritory.get() + 1):  # Компенсация за территорию бизнеса (50%)
        summ += int(22_000_000 * (1 + 0.15) ** (i - 1))
    
    await db.sell_business(user.id, summ)
    await message.answer(f'{user.url}, Вы успешно продали свой бизнес за {tr(summ)}$ {win}')


def reg(dp: Dispatcher):
    dp.register_message_handler(my_business, lambda message: message.text.lower() == 'мой бизнес')
    dp.register_message_handler(business_info, lambda message: message.text.lower() == 'бизнес')
    dp.register_message_handler(buy_business, lambda message: message.text.lower() == 'построить бизнес')
    dp.register_callback_query_handler(withdraw_profit, text_startswith='business-sobrat')
    dp.register_callback_query_handler(buy_territory, text_startswith='business-ter')
    dp.register_callback_query_handler(buy_bsterritory, text_startswith='business-bis')
    dp.register_callback_query_handler(payment_taxes, text_startswith='business-nalog')
    dp.register_message_handler(sell_business, lambda message: message.text.lower() == 'продать бизнес')
