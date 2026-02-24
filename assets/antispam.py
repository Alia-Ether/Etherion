import inspect
from aiogram import types
from functools import wraps
import time
from aiogram.types import ChatMemberOwner, ChatMemberAdministrator
import config as cfg
import commands.db as db
from bot import bot
from user import EtherionUser
from assets.classes import FunEvent

earning_msg = {}

def admin_only(private=False):
    def decorator(func):
        @wraps(func)
        async def wrapper(message: types.Message, *args, **kwargs):
            if message.from_user.id not in cfg.admin:
                return
            if private and message.chat.type != "private":
                return
            return await func(message, *args, **kwargs)
        return wrapper
    return decorator

def antispam(func):
    async def wrapper(message: types.Message):
        if message.forward_from:
            return
        if message.chat.type == "supergroup":
            await db.upd_chat_db(message.chat.id)
        uid = message.from_user.id
        ban = await check_ban(uid)
        if ban:
            return
        kwargs = {"message": message}
        sig = inspect.signature(func)
        if "user" in sig.parameters:
            user = EtherionUser(message=message)
            await user.update()
            kwargs["user"] = user
        await FunEvent.emit(func.__name__, message, kwargs.get("user"), "message")
        await func(**kwargs)
    return wrapper

def antispam_earning(func):
    async def wrapper(call: types.CallbackQuery):
        uid = int(call.from_user.id)
        mid = call.data.split("|")
        mid = mid[1] if len(mid) > 1 else None
        if mid and uid != int(mid):
            await bot.answer_callback_query(call.id, text="❌ Это не Ваша кнопка!")
            return
        ban = await check_ban(uid)
        if ban:
            return
        chat = call.message.chat.id
        msg = call.message.message_id
        current_time = time.time()

        data = earning_msg.get((chat, msg))
        if data:
            # Защита от флуда – не чаще 1 раза в секунду
            if current_time - data[1] < 1:
                await bot.answer_callback_query(call.id, text="⏳ Не так быстро! (1 сек)")
                return

            # Если сообщение старше 4 часов – игнорируем, но не удаляем
            if current_time - data[2] > 14400:  # 4 часа
                await bot.answer_callback_query(call.id, text="⌛️ Игра устарела, создайте новую.")
                return

            # Всё ок – просто обновляем время последнего нажатия
            earning_msg[(chat, msg)] = (data[0] + 1, current_time, data[2])

            kwargs = {"call": call}
            sig = inspect.signature(func)
            if "user" in sig.parameters:
                user = EtherionUser(call=call)
                await user.update()
                kwargs["user"] = user
            await func(**kwargs)
            return

        # Первый вызов для этого сообщения
        earning_msg[(chat, msg)] = (1, current_time, current_time)
        kwargs = {"call": call}
        sig = inspect.signature(func)
        if "user" in sig.parameters:
            user = EtherionUser(call=call)
            await user.update()
            kwargs["user"] = user
        await func(**kwargs)

    return wrapper

def moderation(func):
    async def wrapper(message: types.Message, user: EtherionUser):
        if message.forward_from:
            return
        if message.chat.type != "supergroup":
            await message.answer("👇 <b>Эту команду можно использовать только в чатах.</b>")
            return
        member = await message.bot.get_chat_member(message.chat.id, message.from_user.id)
        if member.status not in ["creator", "administrator"]:
            await message.reply(f"😨 <b>Эту команду могут использовать только администраторы чата.</b>")
            return
        bot_info = await message.chat.get_member(user_id=message.bot.id)
        text = ""
        if not isinstance(bot_info, (ChatMemberOwner, ChatMemberAdministrator)):
            await message.reply("⚠️ <b>Боту необходимы права администратора в чате.</b>")
            return
        if not bot_info.can_delete_messages:
            text += "- 🗑️ Удаление сообщений\n"
        if not bot_info.can_restrict_members:
            text += "- 📛 Блокировка пользователей\n"
        if text:
            await message.reply(f"⚠️ <b>Боту необходимы права администратора в чате:</b>\n\n{text}")
            return
        await func(message, user)
    return wrapper

async def check_ban(user_id: int) -> bool:
    await db.reg_user(user_id=user_id)
    ban_time = await db.getban(user_id=user_id)
    if ban_time and time.time() < ban_time[1]:
        return True
    return False

async def new_earning_msg(chat_id: int, message_id: int) -> None:
    earning_msg[chat_id, message_id] = (0, time.time()-2, time.time()-2)

async def new_earning(msg: types.Message) -> None:
    earning_msg[msg.chat.id, msg.message_id] = (0, time.time()-2, time.time()-2)
