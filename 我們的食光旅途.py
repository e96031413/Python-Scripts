import random
toEat =  ['早午餐(咖啡廳)', '咖哩飯', '粽子','泰式料理', '韓式料理', '碗粿/粽子/米糕/肉燥飯', '北方麵食(小籠包/捲餅/餃子/牛肉麵)', '牛肉湯', '拉麵/丼飯', '居酒屋', '烤鴨', '美式料理(漢堡)', 
          '牛排', '燒肉', '燒烤/串燒', '義式料理(Pizza/焗烤/義大利麵)', '港式料理', '日式料理', '墨西哥料理', '德國料理', '西班牙料理', '火鍋/壽喜燒/沙茶爐/羊肉爐/牛肉火鍋', 'Buffet自助餐', 
          '印度料理','中東料理','南美洲料理', '法式料理', '英式料理','鐵板燒', '南洋料理', '越南料理', '甜點', '大腸香腸/黑白切', '台菜熱炒/合菜', 
          '鱔魚意麵', '麵店/滷味', '海產粥/鹹粥/虱目魚', '藥膳/薑母鴨', '黑輪/關東煮/麻辣燙', '炸物類', '王品集團餐廳', '客家菜']
lunch, dinner = random.sample(toEat, 2)
print(f'午餐: {lunch}')
print(f'晚餐: {dinner}')