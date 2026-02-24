from datetime import datetime
from aiogram import Dispatcher, types

from assets.antispam import antispam
from commands.db import getban
from assets.classes import CustomEvent
from assets import kb
import random
import config as cfg
from user import EtherionUser

CONFIG = {
    "hello_text": f'''🤖 Добро пожаловать на борт, Кто-то! Меня зовут Etherion, твой верный игровой бот.

🎮 У меня есть множество интересных команд и игр, чтобы скрасить твоё время, будь ты один или в компании друзей! (Кстати, вместе всегда веселее) 💙
🔍 Познакомиться со всеми моими возможностями ты можешь, введя команду «помощь».

<a href="{cfg.channel}">🔈 Наш канал</a>
<a href="{cfg.chat}">💬 Наш чат</a>''',
    
    "hello_text2": f"🚀 Не уверен, с чего начать своё приключение?\nПрисоединяйся к нашему официальному чату {cfg.bot_name}: {cfg.chat}",
    
    "sticker_id": ["CAACAgQAAxkBAAEKs6JlSQUtGTtSzXGVcJGBe0PwnWkI9QACRwkAAm0NeFIe5FE9nk15XTME"]
}


async def on_start(message: types.Message):
    if len(message.text) >= 2:
        await CustomEvent.emit('start_event', {'message': message})

    ban = await getban(message.from_user.id)
    
    if ban:
        dtime = datetime.fromtimestamp(ban[1]).strftime('%Y-%m-%d в %H:%M:%S')
        await message.answer(f'⛔️ Вы заблокированы в боте до <b>{dtime}</b>\nПричина: <i>{ban[2]}</i>')
        return
    
    sticker = random.choice(CONFIG['sticker_id'])
    await message.answer_sticker(sticker=sticker)
    await message.answer(CONFIG['hello_text'], disable_web_page_preview=True, reply_markup=kb.start())
    await message.answer(CONFIG['hello_text2'], disable_web_page_preview=True)


async def terms_cmd(message: types.Message):
    await message.answer("""📄 <b>Пользовательское соглашение</b>

1. <b>Общие положения</b>
1.1. Настоящее соглашение регулирует отношения между владельцем бота (далее «Бот» или «Администрация») и Пользователем.
1.2. Используя Бота, вы соглашаетесь с условиями данного соглашения.
1.3. Запрещено копирование информации с сайта в коммерческих целях.

2. <b>Права и обязанности</b>
2.1. Администрация обязуется поддерживать работу бота.
2.2. Гарантируется бесплатное использование бота.
2.3. Администрация имеет право изменять правила, удалять аккаунты и проводить тех.работы.
2.4. Пользователь обязуется соблюдать соглашение и не нарушать работу бота.
2.5. Запрещено использовать скрипты и ботов.

3. <b>Пожертвования</b>
3.1. Все пожертвования добровольны и не подлежат возврату.
3.2. Вознаграждение за пожертвование выдается в течение суток.
3.3. В случае ошибки — обратитесь к Администрации в течение 24 часов.

4. <b>Действие соглашения</b>
4.1. Соглашение действует с момента начала использования бота.
4.2. Администрация может изменять соглашение в одностороннем порядке.
4.3. Срок действия — бессрочно.
4.4. Изменения могут сопровождаться уведомлением.""")


@antispam
async def new_message(message: types.Message, user: EtherionUser):
    # Для вызова в модулях с помощью FunEvent.subscribe("new_message", ваша_функция)
    pass


def reg(dp: Dispatcher):
    dp.register_message_handler(on_start, commands=['start'])
    dp.register_message_handler(terms_cmd, commands=['terms'])
    dp.register_message_handler(new_message)
