import time, json, sys, os, shutil, requests, subprocess, tempfile
from assets.antispam import admin_only
from commands.admin import keyboards as kb
from install import update_db
from aiogram import types, Dispatcher
import config as cfg
from bot import bot, dp
import asyncio

if_notification = False


async def check_updates() -> None:
	if os.path.exists("updates.json"):
		with open("updates.json", "r") as json_file:
			data = json.load(json_file)
			
		os.remove("updates.json")
		ctime = time.time() - data["time"]
		
		if data["type"] == "update":
			txt = f"<b>🏖 Обновление загружено!</b>\n<i>Обновление заняло {ctime:.1f}сек</i>\n\n<tg-spoiler>Официальный канал разработки бота - @FrontendLed</tg-spoiler>"
			await update_db()
		else:
			txt = f"<b>💫 Бот перезагружен!</b>\n\n<i>Перезагрузка заняла {ctime:.1f}сек</i>"
		
		await bot.edit_message_text(chat_id=data["message"][0], message_id=data["message"][1], text=txt)
	

async def search_update(force: bool = False, check: bool = False) -> bool:
	global if_notification
	try:
		if not check and if_notification and not force:
			return False
		
		response = requests.get("https://raw.githubusercontent.com/Alia-Ether/Etherion/refs/heads/V.2.3/bot.py")
		response.raise_for_status()
		
		content = response.text
		last_version = content.splitlines()[0].strip().split(": ")[1]
		
		with open("bot.py", "r", encoding="utf-8") as file:
			version = file.readline().strip().split(": ")[1]
		
		last_version_int = float(last_version.replace(".", "").replace(",", "."))
		version_int = float(version.replace(".", "").replace(",", "."))

		if last_version_int <= version_int or last_version_int >= 3:
			if_notification = False
			return False
		
		if check:
			return True
		
		if_notification = True
		
		response = requests.get("https://raw.githubusercontent.com/Alia-Ether/Etherion/refs/heads/V.2.3/update_list.txt")
		
		txt = f"<b>🔍 Доступно обновление 🛎</b>\nЧто нового?\n\n<i>{response.text}</i>"
		
		for admin in cfg.admin:
			try:
				await bot.send_message(admin, txt, reply_markup=kb.update_bot())
			except:
				pass

		return False
				
	except Exception as e:
		print(f"Ошибка при попытке найти обновление: {e}")
		return False
		

@admin_only(private=True)
async def update_bot(message: types.Message):
	force = False
	check = await search_update(check=True)

	if not check and "-f" not in message.text:
		await message.answer(f"<b>😄 У вас установлена последняя версия бота!</b>\n Вы также можете попробовать <a href='https://github.com/Alia-Ether/Etherion'>обновиться вручную</a>")
		return
	
	if not check:
		txt = "⚠️ У вас уже установлена последняя версия бота.\n<i>Нажмите на кнопку ниже, если вы хотите</i> <a href='https://github.com/Alia-Ether/Etherion'>обновить файлы бота</a>"
		force = True
	else:
		response = requests.get("https://raw.githubusercontent.com/Alia-Ether/Etherion/refs/heads/V.2.3/update_list.txt")
		txt = f"<b>🔍 Доступно обновление 🛎</b>\nЧто нового?\n\n<i>{response.text}</i>"

	await message.answer(txt, reply_markup=kb.update_bot(force=force))
	
	
async def bot_update(call: types.CallbackQuery) -> None:
	global if_notification
	if call.from_user.id not in cfg.admin:
		return
	
	check = await search_update(check=True)
	force = int(call.data.split("_")[1])
	if_notification = False
	
	if not check and force == 0:
		await bot.answer_callback_query(call.id, show_alert=True, text="🤩 У вас уже установлена последняя версия.")
		return
	
	with open("users.db", "rb") as file:
		await bot.send_document(call.message.chat.id, file, caption=f"🛡 Резервная копия базы данных")
	
	await call.message.edit_text("<i>🎩 Установка обновления...</i>")
	
	with tempfile.TemporaryDirectory() as temp_dir:
		subprocess.run(["git", "clone", "https://github.com/Alia-Ether/Etherion.git", temp_dir], check=True)

		for item in os.listdir(temp_dir):
			if item in ["config_ex.py", "modules"]:
				continue

			src_path = os.path.join(temp_dir, item)
			dest_path = os.path.join(os.getcwd(), item)

			if os.path.isdir(src_path):
				shutil.rmtree(dest_path, ignore_errors=True)
				shutil.copytree(src_path, dest_path)
			else:
				shutil.copy2(src_path, dest_path)

	with open("updates.json", "w") as json_file:
		data = {"type": "update", "message": (call.message.chat.id, call.message.message_id), "time": time.time()}
		json.dump(data, json_file, indent=4)

	os.execv(sys.executable, [sys.executable] + sys.argv)


@admin_only()
async def restart_bot(message: types.Message):
	msg = await message.answer("<i>🔄 Перезагрузка бота...</i>")
	
	with open("updates.json", "w") as json_file:
		data = {"type": "restart", "message": (msg.chat.id, msg.message_id), "time": time.time()}
		json.dump(data, json_file, indent=4)
	
	await asyncio.sleep(2)
	await bot.close()
	await dp.storage.close()
	
	os.execl(sys.executable, sys.executable, *sys.argv)


def reg(dp: Dispatcher):
	dp.register_message_handler(restart_bot, lambda message: message.text in ["🔄 Перезагрузка", "/restartb"])
	dp.register_message_handler(update_bot, lambda message: message.text in ["/updateb", "/updateb -f"])
	dp.register_callback_query_handler(bot_update, text_startswith="update-bot")
