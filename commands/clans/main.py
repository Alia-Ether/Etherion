import re

from aiogram import Dispatcher, types

from assets.transform import transform_int as tr
from assets.antispam import antispam
from user import EtherionUser, EtherionConst
from commands.db import url_name
from commands.clans import db
import commands.clans.clan
import commands.clans.settings


@antispam
async def new_clan(message: types.message, user: EtherionUser):
	win, lose = EtherionConst.emj()

	if user.clan:
		await message.answer(f'{user.url}, вы уже состоите в клане, вы не можете создать новый {lose}')
		return

	try:
		name = " ".join(message.text.split()[2:])
	except:
		await message.answer(f'{user.url}, вы не указали имя для будущего клана {lose}')
		return

	if len(name) < 5:
		await message.answer(f'{user.url}, название клана не может быть меньше чем 5 символов {lose}')
		return

	if len(name) > 25:
		await message.answer(f'{user.url}, название клана не может быть длинее чем 25 символов {lose}')
		return

	if re.search(r'<|>|@|t\.me|http', name):
		await message.answer(f'{user.url}, название вашего клана содержит запрещённые символы {lose}')
		return

	if int(user.balance) < 250_000_000_000:
		await message.answer(f'{user.url}, у вас недостаточно денег для создания клана {lose}')
		return

	await db.new_clan_db(user.id, name)
	await message.answer(f'{user.url}, вы успешно создали клан под названием "{name}".\n\n⚙️ Для управления кланом используйте команды с пункта "Кланы"')


@antispam
async def clan_join(message: types.message, user: EtherionUser):
	win, lose = EtherionConst.emj()

	if user.clan:
		await message.answer(f'{user.url}, вы уже состоите в клане. Вы не можете присоединиться к новому {lose}')
		return

	try:
		cid = int(message.text.split()[2])
	except:
		await message.answer(f'{user.url}, вы не ввели ID клана в который хотите вступить {lose}')
		return

	res = await db.join_clan_db(user.id, cid)

	if res == '<no_clan>':
		await message.answer(f'{user.url}, клана с таким ID не существует')
		return

	if res == '<private>':
		await message.answer(f'❌ Вы не можете вступить в приватный клан')
		return

	await message.answer(f'''<b>[Успех]</b>
🤩 Вы успешно вступили в клан <b>[{res}]</b>

✅ Для просмотра информации о клане введите команду [Мой клан]''')


@antispam
async def clan_leave(message: types.message, user: EtherionUser):
	win, lose = EtherionConst.emj()

	if user.clan:
		await message.answer(f'{user.url}, вы не состоите в клане {lose}')
		return

	if user.clan.rank == 4:
		await message.answer(f'{user.url}, к сожалению вы не можете покинуть клан, так как являетесь его основателем {lose}')
		return

	await db.leave_clan_db(user.id)
	await message.answer(f'{user.url}, вы успешно покинули клан <b>[{user.clan.name}]</b> {win}')


@antispam
async def clan_kick(message: types.message, user: EtherionUser):
	win, lose = EtherionConst.emj()

	if not user.clan:
		await message.answer(f'{user.url}, вы не состоите в клане {lose}')
		return

	try:
		uid = int(message.text.split()[2])
	except:
		await message.answer(f'{user.url}, данного игрока не существует {lose}')
		return

	if user.id == uid:
		await message.answer(f'{user.url}, вы не можете исключить самого себя {lose}')
		return

	res = await db.clan_kick_db(uid, user.clan.id, user.clan.rank)

	if res == '<small rank>':
		await message.answer(f'{user.url}, ваш ранг слишком мал, для того чтобы исключить данного игрока {lose}')
	elif res == '<no user>':
		await message.answer(f'{user.url}, данный игрок не находиться в вашем клане, вы не можете его исключить {lose}')
	else:
		uname = await url_name(uid)
		await message.answer(f'{user.url}, вы успешно исключили игрока <b>[{uname}]</b> из клана <b>[{user.clan.name}]</b> {win}')


@antispam
async def clan_kazna(message: types.message, user: EtherionUser):
	win, lose = EtherionConst.emj()

	if not user.clan:
		await message.answer(f'{user.url}, вы не состоите в клане {lose}')
		return

	await message.answer(f'🤑 На данный момент казна клана <b>[{user.clan.name}]</b> составляет - {tr(user.clan.balance)}$')


@antispam
async def clan_kazna_up(message: types.message, user: EtherionUser):
	win, lose = EtherionConst.emj()

	if not user.clan:
		await message.answer(f'{user.url}, вы не состоите в клане {lose}')
		return

	try:
		if message.text.split()[2].lower() in ['все', 'всё']:
			summ = int(user.balance)
		else:
			summ = message.text.split()[2].replace('е', 'e')
			summ = int(float(summ))
	except:
		return

	if summ < 2_000_000_000_000:
		await message.answer(f'{user.url}, минимальная сумма чтобы положить в казну клана - 2.000.000.000.000$ {lose}')
		return

	if summ > int(user.balance):
		await message.answer(f'{user.url}, на Вашем балансе недостаточно средств {lose}')
		return

	await db.clan_kazna_up_db(user.id, summ, user.clan.id)
	await message.answer(f'{user.url}, Вы успешно пополнили казну Вашего клана на {tr(summ)}$')


@antispam
async def clan_increase_rank(message: types.message, user: EtherionUser):
	win, lose = EtherionConst.emj()

	if not user.clan.id:
		await message.answer(f'{user.url}, вы не состоите в клане {lose}')
		return

	try:
		uid = int(message.text.split()[2])
	except:
		await message.answer(f'{user.url}, данного игрока не существует {lose}')
		return

	if user.id == uid:
		await message.answer(f'{user.url}, вы не можете повысить самого себя {lose}')
		return

	data = await db.clan_info(uid)

	if not data or data[1] != user.clan.id:
		await message.answer(f'{user.url}, данного игрока не существует {lose}')
		return

	if user.clan.rank < user.clan.settings['ranks'] or (data[2] + 1) >= user.clan.rank:
		await message.answer(f'{user.url}, ваш ранг слишком мал, для того чтобы повышать членов клана {lose}')
		return

	if data[2] >= 3:
		await message.answer(f'{user.url}, вы не можете повысить человека выше 3 ранга {lose}')
		return

	await db.clan_up_rank(uid)
	name = await url_name(uid)
	await message.answer(f'{user.url}, вы успешно повысили игрока <b>[{name}]</b> на один ранг {win}')


@antispam
async def clan_lower_rank(message: types.message, user: EtherionUser):
	win, lose = EtherionConst.emj()

	if not user.clan:
		await message.answer(f'{user.url}, вы не состоите в клане {lose}')
		return

	try:
		uid = int(message.text.split()[2])
	except:
		await message.answer(f'{user.url}, данного игрока не существует {lose}')
		return

	if user.id == uid:
		await message.answer(f'{user.url}, вы не можете понизить самого себя {lose}')
		return

	data = await db.clan_info(uid)

	if not data or data[1] != user.clan.id:
		await message.answer(f'{user.url}, данного игрока не существует {lose}')
		return

	if user.clan.rank < user.clan.settings['ranks']:
		await message.answer(f'{user.url}, ваш ранг слишком мал, для того чтобы понижать членов клана {lose}')
		return

	if data[2] <= 1:
		await message.answer(f'{user.url}, вы не можете понизить человека ниже 1 ранга {lose}')
		return

	await db.clan_down_rank(uid)
	name = await url_name(uid)
	await message.answer(f'{user.url}, вы успешно понизили игрока <b>[{name}]</b> на один ранг {win}')


def reg(dp: Dispatcher):
	dp.register_message_handler(new_clan, lambda message: message.text.lower().startswith('клан создать'))
	dp.register_message_handler(clan_join, lambda message: message.text.lower().startswith('клан вступить'))
	dp.register_message_handler(clan_leave, lambda message: message.text.lower().startswith('клан выйти'))
	dp.register_message_handler(clan_kick, lambda message: message.text.lower().startswith('клан исключить'))
	dp.register_message_handler(clan_kazna, lambda message: message.text.lower() == 'клан казна')
	dp.register_message_handler(clan_kazna_up, lambda message: message.text.lower().startswith('клан казна'))
	dp.register_message_handler(clan_increase_rank, lambda message: message.text.lower().startswith('клан повысить'))
	dp.register_message_handler(clan_lower_rank, lambda message: message.text.lower().startswith('клан понизить'))

	commands.clans.clan.reg(dp)
	commands.clans.settings.reg(dp)
