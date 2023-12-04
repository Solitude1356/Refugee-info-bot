from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from sheetsApi import sheet_values

inline_sheet_countries = InlineKeyboardMarkup(row_width=2,
                                            inline_keyboard=[
                                                [
                                                    InlineKeyboardButton(text=sheet_values[0][0], callback_data=f'0 country'),
                                                    InlineKeyboardButton(text=sheet_values[0][2], callback_data=f'2 country')
                                                ]
                                            ])

inline_keyboard = []            # Список тем

for i in range(len(sheet_values[1])):
    inline_keyboard.append([])
    inline_keyboard[i].append(InlineKeyboardButton(text=sheet_values[1][i][0], callback_data=f'{str(i)} theme'))

inline_sheet_themes = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard)

inline_keyboard = []
 # Список питань (інфо)
 


# for j in range(len(sheet_values[2])):
#     inline_keyboard.append([])
#     for i in range(sheet_values[1][j][1]):
#         inline_keyboard[j].append([])
#         if sheet_values[2][i][1].find('t.me/') == -1:
#             inline_keyboard[j][i].append(InlineKeyboardButton(text=sheet_values[2][i][0], callback_data=f"{str(j), ' ', str(i)} issue"))
#             print(str(j), ' ', str(i))
#         else:
#             inline_keyboard[j][i].append(InlineKeyboardButton(text=sheet_values[2][i][0], url=sheet_values[2][i][1]))
            


inline_sheet_issues_0 = InlineKeyboardMarkup(row_width=1,
                                            inline_keyboard=[
                                                [
                                                    InlineKeyboardButton(text=sheet_values[2][0][0], url=sheet_values[2][0][1]),
                                                ],
                                                [
                                                    InlineKeyboardButton(text=sheet_values[2][1][0], url=sheet_values[2][1][1]),
                                                ],
                                                [
                                                    InlineKeyboardButton(text=sheet_values[2][2][0], url=sheet_values[2][2][1]),
                                                ],
                                                [
                                                    InlineKeyboardButton(text=sheet_values[2][3][0], url=sheet_values[2][3][1]),
                                                ],
                                                [
                                                    InlineKeyboardButton(text=sheet_values[2][4][0], url=sheet_values[2][4][1]),
                                                ],
                                                [
                                                    InlineKeyboardButton(text=sheet_values[2][5][0], url=sheet_values[2][5][1]),
                                                ],
                                                [
                                                    InlineKeyboardButton(text=sheet_values[2][6][0], url=sheet_values[2][6][1]),
                                                ],
                                                [
                                                    InlineKeyboardButton(text=sheet_values[2][7][0], url=sheet_values[2][7][1]),
                                                ],
                                                [
                                                    InlineKeyboardButton(text=sheet_values[2][8][0], url=sheet_values[2][8][1]),
                                                ],
                                                [
                                                    InlineKeyboardButton(text=sheet_values[2][9][0], url=sheet_values[2][9][1]),
                                                ]
                                            ])

inline_sheet_issues_1 = InlineKeyboardMarkup(row_width=1,
                                            inline_keyboard=[
                                                [
                                                    InlineKeyboardButton(text=sheet_values[2][10][0], url=sheet_values[2][10][1]),
                                                ]
                                            ])

inline_sheet_issues_2 = InlineKeyboardMarkup(row_width=1,
                                            inline_keyboard=[
                                                [
                                                    InlineKeyboardButton(text=sheet_values[2][11][0], url=sheet_values[2][11][1]),
                                                ],
                                                [
                                                    InlineKeyboardButton(text=sheet_values[2][12][0], url=sheet_values[2][12][1]),
                                                ],
                                                [
                                                    InlineKeyboardButton(text=sheet_values[2][13][0], url=sheet_values[2][13][1]),
                                                ],
                                                [
                                                    InlineKeyboardButton(text=sheet_values[2][14][0], url=sheet_values[2][14][1]),
                                                ],
                                                [
                                                    InlineKeyboardButton(text=sheet_values[2][15][0], url=sheet_values[2][15][1]),
                                                ],
                                                [
                                                    InlineKeyboardButton(text=sheet_values[2][16][0], url=sheet_values[2][16][1]),
                                                ]
                                            ])

inline_sheet_issues_3 = InlineKeyboardMarkup(row_width=1,
                                            inline_keyboard=[
                                                [
                                                    InlineKeyboardButton(text=sheet_values[2][17][0], url=sheet_values[2][17][1]),
                                                ],
                                                [
                                                    InlineKeyboardButton(text=sheet_values[2][18][0], url=sheet_values[2][18][1]),
                                                ],
                                                [
                                                    InlineKeyboardButton(text=sheet_values[2][19][0], url=sheet_values[2][19][1]),
                                                ],
                                                [
                                                    InlineKeyboardButton(text=sheet_values[2][20][0], url=sheet_values[2][20][1]),
                                                ]
                                            ])

inline_sheet_issues_4 = InlineKeyboardMarkup(row_width=1,
                                            inline_keyboard=[
                                                [
                                                    InlineKeyboardButton(text=sheet_values[2][21][0], url=sheet_values[2][21][1]),
                                                ],
                                                [
                                                    InlineKeyboardButton(text=sheet_values[2][22][0], url=sheet_values[2][22][1]),
                                                ],
                                                [
                                                    InlineKeyboardButton(text=sheet_values[2][23][0], url=sheet_values[2][23][1]),
                                                ],
                                                [
                                                    InlineKeyboardButton(text=sheet_values[2][24][0], url=sheet_values[2][24][1]),
                                                ],
                                                [
                                                    InlineKeyboardButton(text=sheet_values[2][25][0], url=sheet_values[2][25][1]),
                                                ],
                                                [
                                                    InlineKeyboardButton(text=sheet_values[2][26][0], url=sheet_values[2][26][1]),
                                                ],
                                                [
                                                    InlineKeyboardButton(text=sheet_values[2][27][0], url=sheet_values[2][27][1]),
                                                ],
                                                [
                                                    InlineKeyboardButton(text=sheet_values[2][28][0], url=sheet_values[2][28][1]),
                                                ], 
                                                [
                                                    InlineKeyboardButton(text=sheet_values[2][29][0], url=sheet_values[2][29][1]),
                                                ]
                                            ])

inline_sheet_issues_5 = InlineKeyboardMarkup(row_width=1,
                                            inline_keyboard=[
                                                [
                                                    InlineKeyboardButton(text=sheet_values[2][30][0], url=sheet_values[2][30][1]),
                                                ]
                                            ])

inline_sheet_issues_6 = InlineKeyboardMarkup(row_width=1,
                                            inline_keyboard=[
                                                [
                                                    InlineKeyboardButton(text=sheet_values[2][31][0], url=sheet_values[2][31][1]),
                                                ]
                                            ])

inline_sheet_issues_7 = InlineKeyboardMarkup(row_width=1,
                                            inline_keyboard=[
                                                [
                                                    InlineKeyboardButton(text=sheet_values[2][32][0], url=sheet_values[2][32][1]),
                                                ]
                                            ])

inline_sheet_issues_8 = InlineKeyboardMarkup(row_width=1,
                                            inline_keyboard=[
                                                [
                                                    InlineKeyboardButton(text=sheet_values[2][33][0], url=sheet_values[2][33][1]),
                                                ],
                                                [
                                                    InlineKeyboardButton(text=sheet_values[2][34][0], url=sheet_values[2][34][1]),
                                                ]
                                            ])

inline_sheet_issues_9 = InlineKeyboardMarkup(row_width=1,
                                            inline_keyboard=[
                                                [
                                                    InlineKeyboardButton(text=sheet_values[2][35][0], url=sheet_values[2][35][1]),
                                                ],
                                                [
                                                    InlineKeyboardButton(text=sheet_values[2][36][0], url=sheet_values[2][36][1]),
                                                ]
                                            ])

inline_sheet_issues_10 = InlineKeyboardMarkup(row_width=1,
                                            inline_keyboard=[
                                                [
                                                    InlineKeyboardButton(text=sheet_values[2][37][0], url=sheet_values[2][37][1]),
                                                ]
                                            ])

inline_sheet_issues_11 = InlineKeyboardMarkup(row_width=1,
                                            inline_keyboard=[
                                                [
                                                    InlineKeyboardButton(text=sheet_values[2][38][0], url=sheet_values[2][38][1]),
                                                ],
                                                [
                                                    InlineKeyboardButton(text=sheet_values[2][39][0], url=sheet_values[2][39][1]),
                                                ]
                                            ])

# inline_sheet_issues_0 = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard[0])
# inline_sheet_issues_1 = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard[1])
# inline_sheet_issues_2 = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard[2])
# inline_sheet_issues_3 = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard[3])
# inline_sheet_issues_4 = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard[4])
# inline_sheet_issues_5 = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard[5])
# inline_sheet_issues_6 = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard[6])
# inline_sheet_issues_7 = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard[7])
# inline_sheet_issues_8 = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard[8])
# inline_sheet_issues_9 = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard[9])
# inline_sheet_issues_10 = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard[10])
# inline_sheet_issues_11 = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard[11])
# inline_sheet_issues_2 = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard[12])
# inline_sheet_issues_3 = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard[13])
# inline_sheet_issues_4 = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard[14])
# inline_sheet_issues_5 = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard[15])
# inline_sheet_issues_6 = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard[16])
# inline_sheet_issues_7 = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard[17])
# inline_sheet_issues_8 = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard[18])
# inline_sheet_issues_9 = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard[19])
# inline_sheet_issues_10 = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard[20])
# inline_sheet_issues_11 = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard[21])
# inline_sheet_issues_2 = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard[22])
# inline_sheet_issues_3 = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard[23])
# inline_sheet_issues_4 = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard[24])
# inline_sheet_issues_5 = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard[25])
# inline_sheet_issues_6 = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard[26])
# inline_sheet_issues_7 = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard[27])
# inline_sheet_issues_8 = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard[28])
# inline_sheet_issues_9 = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard[29])
# inline_sheet_issues_10 = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard[30])
# inline_sheet_issues_11 = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard[31])
# inline_sheet_issues_2 = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard[32])
# inline_sheet_issues_3 = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard[33])
# inline_sheet_issues_4 = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard[34])
# inline_sheet_issues_5 = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard[35])
# inline_sheet_issues_6 = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard[36])
# inline_sheet_issues_7 = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard[37])
# inline_sheet_issues_8 = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard[38])
# inline_sheet_issues_9 = InlineKeyboardMarkup(row_width=1, inline_keyboard=inline_keyboard[39])