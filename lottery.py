"""Viết một script kiểm tra xem các số argument đầu vào có trúng lô không
(2 số cuối trùng với một giải nào đó). Nếu không có argument nào thì print
ra tất cả các giải từ đặc biệt -> giải 7
"""

import requests
from bs4 import BeautifulSoup
import sys


def lottery():
    """Trả về list chứa kết quả xổ số từ giải đặc biệt đến giải 7"""

    r = requests.get("http://ketqua.net")
    tree = BeautifulSoup(markup=r.text, features="html.parser")
    note = [
        "rs_0_0",
        "rs_1_0",
        "rs_2_0",
        "rs_2_1",
        "rs_3_0",
        "rs_3_1",
        "rs_3_2",
        "rs_3_3",
        "rs_3_4",
        "rs_3_5",
        "rs_4_0",
        "rs_4_1",
        "rs_4_2",
        "rs_4_3",
        "rs_5_0",
        "rs_5_1",
        "rs_5_2",
        "rs_5_3",
        "rs_5_4",
        "rs_5_5",
        "rs_6_0",
        "rs_6_1",
        "rs_6_2",
        "rs_7_0",
        "rs_7_1",
        "rs_7_2",
        "rs_7_3",
    ]
    result = []
    for i in note:
        t = tree.find(name="div", attrs={"id": i})
        result.append(t.text)

    return result


def check_lottery(input_data):
    """Kiểm tra xem các số ở input_data có trúng lô(2 số cuối của các giải) không
    :param input_data: các số cần kiểm tra ( số chơi lô có 2 chữ số)
    """

    last_2_numbers = [int(i[-2:]) for i in lottery()]
    print(last_2_numbers)
    numbers_in_lottery = []
    for number in input_data:
        if int(number) in last_2_numbers:
            numbers_in_lottery.append(number)

    if numbers_in_lottery:
        result = "Trúng lô rồi!!!\nSố trúng: ", numbers_in_lottery
    else:
        note = lottery()
        result = []
        prize_lottery = [
            ["Giải đặc biệt: ", note[0]],
            ["Giải nhất: ", note[1]],
            note[2:4],
            note[4:10],
            note[10:14],
            note[14:20],
            note[20:23],
            note[23:27],
        ]

        for i in prize_lottery:
            result.append(" ".join(i))

        result = (
            "Tạch!!! Không sao còn thở là còn gỡ\nKết quả hôm nay:\n",
            result,
        )
    return result


def main():
    input_data = sys.argv[1:]
    result = check_lottery(input_data)
    print(result[0])
    for i in result[1]:
        print(i)


if __name__ == "__main__":
    main()
