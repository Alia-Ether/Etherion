from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import config as cfg
from utils.settings import get_setting


def help_menu(user_id):
    keyboards = InlineKeyboardMarkup()
    buttons = [
        InlineKeyboardButton("💡 Основные", callback_data=f"help_osn|{user_id}"),
        InlineKeyboardButton("🎲 Игры", callback_data=f"help_game|{user_id}"),
        InlineKeyboardButton("💥 Развлекательное", callback_data=f"help_rz|{user_id}"),
        InlineKeyboardButton("🏰 Кланы", callback_data=f"help_clans|{user_id}"),
        InlineKeyboardButton("🧩 Модули", callback_data=f"help_modules|{user_id}"),  # 👈 новая кнопка
    ]
    keyboards.add(buttons[0], buttons[1])
    keyboards.add(buttons[2], buttons[3])
    keyboards.add(buttons[4])  # 👈 добавляем отдельно
    return keyboards


def help_back(user_id):
    back_button = InlineKeyboardButton("Назад", callback_data=f"help_back|{user_id}")
    return InlineKeyboardMarkup().add(back_button)


# ==================== НОВЫЕ ФУНКЦИИ ДЛЯ МОДУЛЕЙ ====================
def modules_navigation_kb(user_id: int, current_page: int, total_pages: int) -> InlineKeyboardMarkup:
    """Клавиатура для навигации по страницам модулей"""
    keyboards = InlineKeyboardMarkup(row_width=3)
    
    prev_btn = InlineKeyboardButton("◀️ Назад", callback_data=f"modules_prev_{current_page}|{user_id}")
    close_btn = InlineKeyboardButton("❌ Закрыть", callback_data=f"modules_close_{current_page}|{user_id}")
    next_btn = InlineKeyboardButton("Вперёд ▶️", callback_data=f"modules_next_{current_page}|{user_id}")
    
    keyboards.add(prev_btn, close_btn, next_btn)
    return keyboards


# ==================== ВСЁ ОСТАЛЬНОЕ БЕЗ ИЗМЕНЕНИЙ ====================
def start():
    keyboards = InlineKeyboardMarkup()
    buttons = [
        InlineKeyboardButton("😄 Добавить в чат", url=f"https://t.me/{cfg.bot_username}?startgroup=true"),
        InlineKeyboardButton("👥 Общая беседа", url=f"https://{cfg.chat}"),
        InlineKeyboardButton("👥 Наш канал", url=f"https://{cfg.channel}"),
    ]
    keyboards.add(buttons[0], buttons[1])
    keyboards.add(buttons[2])
    return keyboards


def ferma(user_id):
    keyboards = InlineKeyboardMarkup()
    buttons = [
        InlineKeyboardButton("💰 Собрать прибыль", callback_data=f"ferma-sobrat|{user_id}"),
        InlineKeyboardButton("💸 Оплатить налоги", callback_data=f"ferma-nalog|{user_id}"),
        InlineKeyboardButton("⬆️ Купить видеокарту", callback_data=f"ferma-bycards|{user_id}"),
    ]
    keyboards.add(buttons[0], buttons[1])
    keyboards.add(buttons[2])
    return keyboards


def generator(user_id):
    keyboards = InlineKeyboardMarkup()
    buttons = [
        InlineKeyboardButton("💰 Собрать прибыль", callback_data=f"generator-sobrat|{user_id}"),
        InlineKeyboardButton("💸 Оплатить налоги", callback_data=f"generator-nalog|{user_id}"),
        InlineKeyboardButton("⬆️ Купить турбину", callback_data=f"generator-buy-turb|{user_id}"),
    ]
    keyboards.add(buttons[0], buttons[1])
    keyboards.add(buttons[2])
    return keyboards


def business(user_id):
    keyboards = InlineKeyboardMarkup()
    buttons = [
        InlineKeyboardButton("💰 Собрать прибыль", callback_data=f"business-sobrat|{user_id}"),
        InlineKeyboardButton("💸 Оплатить налоги", callback_data=f"business-nalog|{user_id}"),
        InlineKeyboardButton("⬆️ Увеличить территорию", callback_data=f"business-ter|{user_id}"),
        InlineKeyboardButton("⬆️ Увеличить бизнес", callback_data=f"business-bis|{user_id}"),
    ]
    keyboards.add(buttons[0], buttons[1])
    keyboards.add(buttons[2], buttons[3])
    return keyboards


def tree(user_id):
    keyboards = InlineKeyboardMarkup()
    buttons = [
        InlineKeyboardButton("💰 Собрать прибыль", callback_data=f"tree-sobrat|{user_id}"),
        InlineKeyboardButton("💸 Оплатить налоги", callback_data=f"tree-nalog|{user_id}"),
        InlineKeyboardButton("⬆️ Увеличить участок", callback_data=f"tree-ter|{user_id}"),
        InlineKeyboardButton("🆙 Увеличить дерево", callback_data=f"tree-tree|{user_id}"),
    ]
    keyboards.add(buttons[0], buttons[1])
    keyboards.add(buttons[2], buttons[3])
    return keyboards


def quarry(user_id):
    keyboards = InlineKeyboardMarkup()
    buttons = [
        InlineKeyboardButton("💰 Собрать прибыль", callback_data=f"quarry-sobrat|{user_id}"),
        InlineKeyboardButton("💸 Оплатить налоги", callback_data=f"quarry-nalog|{user_id}"),
        InlineKeyboardButton("⬆️ Купить установку", callback_data=f"quarry-bur|{user_id}"),
        InlineKeyboardButton("🆙 Увеличить территорию", callback_data=f"quarry-ter|{user_id}"),
        InlineKeyboardButton("🔧 Увеличить уровень", callback_data=f"quarry-lvl|{user_id}"),
        InlineKeyboardButton("📦 Текущий доход", callback_data=f"quarry-dox|{user_id}"),
    ]
    keyboards.add(buttons[0], buttons[1])
    keyboards.add(buttons[2], buttons[3])
    return keyboards


def garden(user_id):
    keyboards = InlineKeyboardMarkup()
    buttons = [
        InlineKeyboardButton("💰 Собрать прибыль", callback_data=f"garden-sobrat|{user_id}"),
        InlineKeyboardButton("💸 Оплатить налоги", callback_data=f"garden-nalog|{user_id}"),
        InlineKeyboardButton("⬆️ Купить дерево", callback_data=f"garden-buy-tree|{user_id}"),
        InlineKeyboardButton("💦 Полить сад", callback_data=f"garden-polit|{user_id}"),
    ]
    keyboards.add(buttons[0], buttons[1])
    keyboards.add(buttons[2], buttons[3])
    return keyboards


def profil(user_id):
    keyboards = InlineKeyboardMarkup(row_width=1)
    keyboards.add(InlineKeyboardButton("🏠 Имущество", callback_data=f"profil-property|{user_id}"))
    keyboards.add(InlineKeyboardButton("🏭 Бизнесы", callback_data=f"profil-busines|{user_id}"))
    return keyboards


def profil_back(user_id):
    keyboards = InlineKeyboardMarkup()
    keyboards.add(InlineKeyboardButton("⬅️ Назад", callback_data=f"profil-back|{user_id}"))
    return keyboards


def top(user_id, tab):
    keyboards = InlineKeyboardMarkup()
    buttons = [
        InlineKeyboardButton("👑 Топ рейтинга", callback_data=f"top-rating|{user_id}|{tab}"),
        InlineKeyboardButton("💰 Топ денег", callback_data=f"top-balance|{user_id}|{tab}"),
        InlineKeyboardButton("🧰 Топ ферм", callback_data=f"top-cards|{user_id}|{tab}"),
        InlineKeyboardButton("🗄 Топ бизнесов", callback_data=f"top-bsterritory|{user_id}|{tab}"),
        InlineKeyboardButton("🏆 Топ опыта", callback_data=f"top-exp|{user_id}|{tab}"),
        InlineKeyboardButton("💴 Топ йен", callback_data=f"top-yen|{user_id}|{tab}"),
        InlineKeyboardButton("📦 Топ обычных кейсов", callback_data=f"top-case1|{user_id}|{tab}"),
        InlineKeyboardButton("🏵 Топ золотых кейсов", callback_data=f"top-case2|{user_id}|{tab}"),
        InlineKeyboardButton("🏺 Топ рудных кейсов", callback_data=f"top-case3|{user_id}|{tab}"),
        InlineKeyboardButton("🌌 Топ материальных кейсов", callback_data=f"top-case4|{user_id}|{tab}"),
    ]
        
    keyboards.add(buttons[0], buttons[1])
    keyboards.add(buttons[2], buttons[3])
    keyboards.add(buttons[4], buttons[5])
    keyboards.add(buttons[6], buttons[7])
    keyboards.add(buttons[8], buttons[9])
    return keyboards


def wedlock(user_id, r_id):
    keyboards = InlineKeyboardMarkup(row_width=2)
    k1 = InlineKeyboardButton("😍 Согласиться", callback_data=f"wedlock-true|{r_id}|{user_id}")
    k2 = InlineKeyboardButton("😔 Отклонить", callback_data=f"wedlock-false|{r_id}|{user_id}")
    keyboards.add(k1, k2)
    return keyboards


def divorce(user_id):
    keyboards = InlineKeyboardMarkup(row_width=2)
    k1 = InlineKeyboardButton("😞 Развестись", callback_data=f"divorce-true|{user_id}")
    k2 = InlineKeyboardButton("😊 Отменить", callback_data=f"divorce-false|{user_id}")
    keyboards.add(k1, k2)
    return keyboards


def clan(user_id):
    print(user_id)
    user_id = int(user_id)
    keyboards = InlineKeyboardMarkup()
    buttons = [
        InlineKeyboardButton("🛡 О клане", callback_data=f"clan-info|{user_id}"),
        InlineKeyboardButton("👥 Участники", callback_data=f"clan-users|{user_id}"),
        InlineKeyboardButton("🛠 Настройким", callback_data=f"clan-settings|{user_id}"),
    ]
    print(3444444444)
    keyboards.add(buttons[0], buttons[1])
    keyboards.add(buttons[2])
    print(4354444444444)
    return keyboards


def new_own_clan(user_id, cid, user_id_2):
    keyboards = InlineKeyboardMarkup(row_width=2)
    k1 = InlineKeyboardButton("✅ Да, передать", callback_data=f"clan-new-owner_true|{user_id_2}|{cid}|{user_id}")
    k2 = InlineKeyboardButton("❌ Нет, отменить", callback_data=f"clan-new-owner_false|{user_id_2}|{cid}|{user_id}")
    keyboards.add(k1, k2)
    return keyboards


def dell_clan(user_id, cid):
    keyboards = InlineKeyboardMarkup(row_width=2)
    k1 = InlineKeyboardButton("✅ Да, удалить", callback_data=f"clan-dell_true|{cid}|{user_id}")
    k2 = InlineKeyboardButton("❌ Нет, оставить", callback_data=f"clan-dell_false|{cid}|{user_id}")
    keyboards.add(k1, k2)
    return keyboards


def donat_menu(user_id: int) -> InlineKeyboardMarkup:
    keyboards = InlineKeyboardMarkup()

    keyboards.add(InlineKeyboardButton(text="🛒 Наш магазин", callback_data=f"our-store|{user_id}"))

    if get_setting(key="stars_donat", default=False):
        keyboards.add(InlineKeyboardButton(text="⭐️ Донат через звёзды", callback_data=f"donat-stars|{user_id}"))

    if get_setting(key="refund", default=False):
        keyboards.add(InlineKeyboardButton(text="⚡️ Возврат средств", callback_data=f"refund|{user_id}"))

    keyboards.add(InlineKeyboardButton(text="🍀 Донат через админа", url=f"t.me/{cfg.admin_username.replace('@', '')}"))

    return keyboards


def donat_back(user_id: int) -> InlineKeyboardMarkup:
    keyboards = InlineKeyboardMarkup()
    keyboards.add(InlineKeyboardButton(text="🔙 Назад", callback_data=f"donat-menu|{user_id}"))
    return keyboards


def donat_select_amount(user_id: int) -> InlineKeyboardMarkup:
    keyboards = InlineKeyboardMarkup()

    keyboards.add(
        InlineKeyboardButton(text="100⭐️", callback_data=f"select-stars_100|{user_id}"),
        InlineKeyboardButton(text="250⭐️", callback_data=f"select-stars_250|{user_id}"),
    )

    keyboards.add(
        InlineKeyboardButton(text="500⭐️", callback_data=f"select-stars_500|{user_id}"),
        InlineKeyboardButton(text="750⭐️", callback_data=f"select-stars_750|{user_id}"),
    )

    keyboards.add(
        InlineKeyboardButton(text="1000⭐️", callback_data=f"select-stars_1000|{user_id}"),
        InlineKeyboardButton(text="1500⭐️", callback_data=f"select-stars_1500|{user_id}"),
    )

    keyboards.add(InlineKeyboardButton(text="🔙 Назад", callback_data=f"donat-menu|{user_id}"))

    return keyboards


def confirm_donat(user_id: int, stars: int) -> InlineKeyboardMarkup:
    keyboards = InlineKeyboardMarkup()
    keyboards.add(InlineKeyboardButton(text="✅ Подтвердить", callback_data=f"buy-stars_{stars}|{user_id}"))
    keyboards.add(InlineKeyboardButton(text="🔙 Назад", callback_data=f"donat-menu|{user_id}"))
    return keyboards