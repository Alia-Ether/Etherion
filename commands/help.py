from aiogram import types, Dispatcher

from assets.antispam import antispam, admin_only, antispam_earning, new_earning_msg
from user import EtherionUser
from assets import kb
import config as cfg
from commands.admin.module_manager import MODULES

adm_us = cfg.admin_username.replace('@', '')
adm = f'<a href="t.me/{adm_us}">{cfg.admin_username}</a>'

help_msg = {}


CONFIG = {
    "help_cmd": '''{}, выберите категорию:
   1️⃣ Основное
   2️⃣ Игры
   3️⃣ Развлекательное
   4️⃣ Кланы
   5️⃣ Модули

💬 Так же у нас есть общая беседа №1 и общая беседа №2
🆘 По всем вопросам - ''' + adm,

    "help_osn": '''{}, основные команды:
   💡 Разное:
   📒 Профиль
   💫 Мой лимит
   👑 Рейтинг
   👑 Продать рейтинг
   ⚡ Энергия
   ⛏ Шахта
   🚗 Машины
   📱 Телефоны
   ✈ Самолёты
   🛥 Яхты
   🚁 Вертолёты
   🏠 Дома
   💸 Б/Баланс
   📦 Инвентарь
   📊 Курс руды
   🏢 Ограбить мэрию
   💰 Банк [положить/снять] [сумма/всё]
   💵 Депозит [положить/снять] [сумма/всё]
   🤝 Дать [сумма]
   🌐 Биткоин курс/купить/продать [кол-во]
   ⚱ Биткоины
   💈 Ежедневный бонус
   💷 Казна
   💢 Сменить ник [новый ник]
   👨 Мой ник - узнать ник
   ⚖ РП Команды - узнать РП команды
   🏆 Мой статус
   🔱 Статусы️
   💭 !Беседа - беседа бота''',

    "help_game": '''{}, игровые команды:
   🚀 Игры:
   🎮 Спин [ставка]
   🎲 Кубик [число] [ставка]
   🏀 Баскетбол [ставка]
   🎯 Дартс [ставка]
   ⚽️ Футбол [ставка]
   🎳️ Боулинг [ставка]
   📉 Трейд [вверх/вниз] [ставка]
   🎰 Казино [ставка]''',

    'help_rz': '''{}, развлекательные команды:
   🔮 Шар [фраза]
   💬 Выбери [фраза] или [фраза2]
   📊 Инфа [фраза]

💒 Браки:
   💖 Свадьба [ID пользователя]
   💖 Развод
   💌 Мой брак

📦 Кейсы:
   🛒 Купить кейс [номер] [количество]
   🔐 Открыть кейс [номер] [количество]

🗄 Бизнес:
   💰 Мой бизнес/бизнес
   💸 Продать бизнес

🏭Генератор
   🏭 Мой генератор/генератор
   💷 Продать генератор

🧰 Майнинг ферма:
   🔋 Моя ферма/ферма
   💰 Продать ферму

⚠️ Карьер:
   🏗 Мой карьер/карьер
   💰 Продать карьер
   
🏡 Денежное дерево:
   🌳 Моё дерево
   💰 Продать участок

🌳 Сады:
   🪧 Мой сад/сад
   💰 Продать сад
   💦 Сад полить
   🍸 Зелья
   🔮 Создать зелье [номер]''',

    'help_clans': '''{}, клановые команды:
🗂 Общие команды:
   💡 Мой клан - общая информация
   🏆 Клан топ - общий рейтинг кланов(Недоступно)
   ✅ Клан пригласить [ID] - пригласить игрока в клан
   🙋‍♂ Клан вступить [ID клана] - вступить в клан
   📛 Клан исключить [ID] - исключает игрока
   🚷 Клан выйти - выйти из клана
   💰 Клан казна - состояние казны
   💵 Клан казна [сумма] - снять деньги с казны

⚙ Создание и настройка кланов:
   ⚙ Клан создать [название] - стоимость 250.000.000.000$
   ⤴ Клан настройки - информация о настройках
   📥 Клан настройки приглашениие [1-4]
   💢 Клан настройки кик [1-4]
   🔰 Клан настройки ранги [1-4]
   💵 Клан настройки казна [1-4]
   💰 Клан настройки ограбление [1-4]
   ⚔ Клан настройки война [1-4]
   ✏ Клан настройки название [1-4]
   🔐 Клан настройки тип [закрытый/открытый]

🔎 Управление кланом:
   ✏ Клан название [название] - изменить название клана
   ⤴ Клан повысить [ID] - повысить игрока
   ⤵ Клан понизить [ID] - понизить игрока
   📛 Клан удалить - удалить клан

🛡 Клановые захваты:
   👮‍♀ Клан ограбление (недоступно) - ограбление казны штата

📜 Будьте осторожнее с командами повышения и понижения, повысив игрока до определенного статуса он сможет изменять название клана и управлять им.''',

    'help_adm': '''{}, админ команды:
   🔄 /restartb
   ⬆️ /updateb
   ⚠️ /loadmodb [raw ссылка]
   🚀 /sql [запрос]
   📛 /banb [id] [время] [причина]
   ✅ /unbanb [id]
   🎩 Выдать [сумма]
   🐙 Забрать [сумма]
   😶 Обнулить [сумма]''',

    'help_modules': '''{}, загруженные модули:\n\n{}''',
}


# ==================== ПАГИНАЦИЯ МОДУЛЕЙ ====================
MODULES_PER_PAGE = 5

def get_modules_page(page: int):
    """Возвращает список модулей для конкретной страницы"""
    module_list = list(MODULES.items())
    total_pages = (len(module_list) + MODULES_PER_PAGE - 1) // MODULES_PER_PAGE
    
    start = (page - 1) * MODULES_PER_PAGE
    end = start + MODULES_PER_PAGE
    current_modules = module_list[start:end]
    
    return current_modules, total_pages


@antispam
async def help_cmd(message: types.Message, user: EtherionUser):
    msg = await message.answer(CONFIG['help_cmd'].format(user.url), reply_markup=kb.help_menu(user.user_id))
    await new_earning_msg(msg.chat.id, msg.message_id)


@admin_only(private=False)
async def help_adm(message: types.Message):
    await message.answer(CONFIG['help_adm'].format('Admin'))
    

@antispam
async def help_game_msg(message: types.Message, user: EtherionUser):
    await message.answer(CONFIG['help_game'].format(user.url))


@antispam_earning
async def help_back(call: types.CallbackQuery, user: EtherionUser):
    await call.message.edit_text(text=CONFIG['help_cmd'].format(user.url), reply_markup=kb.help_menu(user.user_id))


@antispam_earning
async def help_callback(call: types.CallbackQuery, user: EtherionUser):
    data = call.data.split('_')[1].split('|')[0]
    
    txt = {
        'osn': CONFIG['help_osn'],
        'game': CONFIG['help_game'],
        'rz': CONFIG['help_rz'],
        'clans': CONFIG['help_clans'],
        'modules': CONFIG['help_modules'],
    }.get(data)
    
    if data == 'modules':
        # Показываем первую страницу модулей
        await show_modules_page(call, user, page=1)
        return
    else:
        txt = txt.format(user.url)
    
    await call.message.edit_text(text=txt, reply_markup=kb.help_back(user.user_id))


@antispam_earning
async def modules_navigation(call: types.CallbackQuery, user: EtherionUser):
    """Навигация по страницам модулей"""
    data = call.data.split('_')[1]
    page = int(call.data.split('_')[2].split('|')[0])
    
    if data == 'next':
        page += 1
    elif data == 'prev':
        page -= 1
    elif data == 'close':
        await call.message.delete()
        return
    
    await show_modules_page(call, user, page)


async def show_modules_page(call: types.CallbackQuery, user: EtherionUser, page: int):
    """Показывает страницу с модулями"""
    current_modules, total_pages = get_modules_page(page)
    
    modules_text = ""
    for mod_name, mod_info in current_modules:
        modules_text += f"🧩 <b>{mod_info['name']}</b>\n  <i>{mod_info['description']}</i>\n\n"
    
    text = CONFIG['help_modules'].format(user.url, modules_text)
    text += f"\n📄 Страница {page} из {total_pages}"
    
    await call.message.edit_text(
        text=text,
        reply_markup=kb.modules_navigation_kb(user.user_id, page, total_pages)
    )


def reg(dp: Dispatcher):
    dp.register_message_handler(help_adm, commands='help_adm')
    dp.register_message_handler(help_cmd, lambda message: message.text.lower() in ['/help', 'помощь'])
    dp.register_message_handler(help_game_msg, lambda message: message.text.lower() == 'игры')
    dp.register_callback_query_handler(help_back, text_startswith='help_back')
    dp.register_callback_query_handler(help_callback, text_startswith='help_')
    dp.register_callback_query_handler(modules_navigation, text_startswith='modules_')