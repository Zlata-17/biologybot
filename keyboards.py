from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Науки о живой природе')],
                                     [KeyboardButton(text='Уровни организации живых систем')],
                                     [KeyboardButton(text='Вирусы и фаги (бактериофаги)')],
                                     [KeyboardButton(text='Бактерии'),
                                      KeyboardButton(text='Цианобактерии')],
                                     [KeyboardButton(text='Протисты')],
                                     [KeyboardButton(text='Грибы')],
                                     [KeyboardButton(text='Растения')],
                                     [KeyboardButton(text='Животные')],
                                     [KeyboardButton(text='Человек и его здоровье')],
                                     [KeyboardButton(text='Все темы')],],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню')


catalog_protists2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Амёба обыкновенная', callback_data='amoeba')],
    [InlineKeyboardButton(text='Инфузория-туфелька', callback_data='infusoria')]])

catalog_protists3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Эвглена зелёная', callback_data='euglena')],
    [InlineKeyboardButton(text='Хламидомонада', callback_data='сhlamydomonas')],
    [InlineKeyboardButton(text='Хлорелла', callback_data='chlorella')]])

catalog_mushrooms = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Шляпочные грибы', callback_data='cap_mushrooms')],
    [InlineKeyboardButton(text='Грибы-паразиты', callback_data='parasitic_fungi')],
    [InlineKeyboardButton(text='Лишайники', callback_data='lichens')]])

catalog_mould = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Мукор', callback_data='mukor')],
    [InlineKeyboardButton(text='Пеницилл и Аспергилл', callback_data='penicillium_aspergillus')],
    [InlineKeyboardButton(text='Дрожжевые грибы', callback_data='yeasts')]])

catalog_plants = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Водоросли', callback_data='seaweed')],
    [InlineKeyboardButton(text='Мхи', callback_data='mosses')],
    [InlineKeyboardButton(text='Папоротники', callback_data='ferns')],
    [InlineKeyboardButton(text='Хвощи', callback_data='horsetails')],
    [InlineKeyboardButton(text='Плауны', callback_data='plauns')],
    [InlineKeyboardButton(text='Голосеменные растения', callback_data='gymnosperms')],
    [InlineKeyboardButton(text='Покрытосеменные растения', callback_data='angiosperms')]])

catalog_vegetative = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Корень', callback_data='root')],
    [InlineKeyboardButton(text='Побег', callback_data='escape')],
    [InlineKeyboardButton(text='Почка', callback_data='bud')],
    [InlineKeyboardButton(text='Стебель', callback_data='stem')],
    [InlineKeyboardButton(text='Лист', callback_data='sheet')],
    [InlineKeyboardButton(text='Вегетативное размножение растений', callback_data='vegetative_reproduction')]])

catalog_generative = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Цветок', callback_data='flower')],
    [InlineKeyboardButton(text='Соцветия', callback_data='inflorescences')],
    [InlineKeyboardButton(text='Плоды', callback_data='fetuses')],
    [InlineKeyboardButton(text='Семя', callback_data='seed')],
    [InlineKeyboardButton(text='Опыление', callback_data='pollination')],
    [InlineKeyboardButton(text='Оплодотворение у цветковых растений', callback_data='fertilization_of_flowering')],
    [InlineKeyboardButton(text='Классификация цветковых растений', callback_data='classification')],
    [InlineKeyboardButton(text='Сравнительная характеристика классов цветковых растений',
                          callback_data='comparison_of_flowers')],
    [InlineKeyboardButton(text='Сравнительная характеристика семейств отдела Покрытосеменные',
                          callback_data='comparison_of_families')],
    [InlineKeyboardButton(text='Признаки покрытосеменных', callback_data='signs_of_angiosperms')]])

catalog_animals = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Тип Кишечнополостные', callback_data='coelenterates')],
    [InlineKeyboardButton(text='Тип Плоские черви', callback_data='flatworms')],
    [InlineKeyboardButton(text='Тип Круглые черви', callback_data='roundworms')],
    [InlineKeyboardButton(text='Тип Кольчатые черви', callback_data='annelid_worms')],
    [InlineKeyboardButton(text='Тип Моллюски', callback_data='shellfish')],
    [InlineKeyboardButton(text='Тип Членистоногие', callback_data='arthropods')],
    [InlineKeyboardButton(text='Тип Хордовые', callback_data='chordal')],
])

catalog_coelenterates = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Класс Гидроидные', callback_data='hydroidic')],
    [InlineKeyboardButton(text='Класс Сцифоидные', callback_data='scyphoid')],
    [InlineKeyboardButton(text='Класс Коралловые полипы', callback_data='coral_polyps')]])

catalog_flatworms = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Класс Ресничные черви', callback_data='ciliated')],
    [InlineKeyboardButton(text='Класс Сосальщики', callback_data='suckers')],
    [InlineKeyboardButton(text='Класс Ленточные черви', callback_data='ribbon')]])

catalog_roundworms = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Многообразие паразитических круглых червей', callback_data='variety_of_roundworms')]])

catalog_annelid_worms = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Класс Малощетинковые', callback_data='low_bristle')],
    [InlineKeyboardButton(text='Класс Многощетинковые', callback_data='polychaete')],
    [InlineKeyboardButton(text='Класс Пиявки', callback_data='leeches')]])

catalog_shellfish = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Класс Брюхоногие', callback_data='gastropods')],
    [InlineKeyboardButton(text='Класс Двустворчатые', callback_data='double_leaf')],
    [InlineKeyboardButton(text='Класс Головоногие', callback_data='cephalopods')]])

catalog_arthropods = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Класс Ракообразные', callback_data='crustaceans')],
    [InlineKeyboardButton(text='Класс Паукообразные', callback_data='arachnids')],
    [InlineKeyboardButton(text='Класс Насекомые', callback_data='insects')]])

catalog_chordal = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Подтип Бесчерепные. Подтип Черепные', callback_data='headless')],
    [InlineKeyboardButton(text='Надкласс Рыбы', callback_data='fishes')],
    [InlineKeyboardButton(text='Класс Земноводные', callback_data='amphibians')],
    [InlineKeyboardButton(text='Класс Пресмыкающиеся', callback_data='reptiles')],
    [InlineKeyboardButton(text='Класс Птицы', callback_data='birds')],
    [InlineKeyboardButton(text='Класс Млекопитающие', callback_data='mammals')]
])

catalog_human = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Эндокринная система (железы внутренней секреции)', callback_data='endocrine')],
    [InlineKeyboardButton(text='Нервная система', callback_data='nervous')],
    [InlineKeyboardButton(text='Опорно-двигательный аппарат', callback_data='motor')],
    [InlineKeyboardButton(text='Кровь', callback_data='blood')],
    [InlineKeyboardButton(text='Сердечно-сосудистая система. Кровообращение', callback_data='heart')],
    [InlineKeyboardButton(text='Дыхательная система', callback_data='respiratory')],
    [InlineKeyboardButton(text='Пищеварительная система', callback_data='digestive')],
    [InlineKeyboardButton(text='Обмен веществ и энергии', callback_data='energy')],
    [InlineKeyboardButton(text='Выделительная система. Мочевыделение', callback_data='excretory')],
    [InlineKeyboardButton(text='Покровная система. Кожа', callback_data='skin')],
    [InlineKeyboardButton(text='Репродуктивная система. Индивидуальная развитие человека',
                          callback_data='reproductive')],
    [InlineKeyboardButton(text='Анализаторы. Сенсорные системы. ', callback_data='analyzers')],
    [InlineKeyboardButton(text='Высшая нервная деятельность (ВНД)', callback_data='higher_nervous')]
])


catalog_themes_protists = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Амёба обыкновенная', callback_data='amoeba')],
    [InlineKeyboardButton(text='Инфузория-туфелька', callback_data='infusoria')],
    [InlineKeyboardButton(text='Эвглена зелёная', callback_data='euglena')],
    [InlineKeyboardButton(text='Хламидомонада', callback_data='сhlamydomonas')],
    [InlineKeyboardButton(text='Хлорелла', callback_data='chlorella')]])

catalog_themes_mushrooms = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Шляпочные грибы', callback_data='cap_mushrooms')],
    [InlineKeyboardButton(text='Грибы-паразиты', callback_data='parasitic_fungi')],
    [InlineKeyboardButton(text='Лишайники', callback_data='lichens')],
    [InlineKeyboardButton(text='Мукор', callback_data='mukor')],
    [InlineKeyboardButton(text='Пеницилл и Аспергилл', callback_data='penicillium_aspergillus')],
    [InlineKeyboardButton(text='Дрожжевые грибы', callback_data='yeasts')]])
