#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_bill(name, data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2
	sous_total = 0
	for items in data:
		sous_total += items[INDEX_PRICE] * items[INDEX_QUANTITY]
	taxes = sous_total * 15/100
	total = sous_total + taxes
	return """
	%s
	SOUS TOTAL %.2f $
	TAXES %.2f $
	TOTAL %.2f $""" %(name,sous_total,taxes,total)


def format_number(number, num_decimal_digits):
	decimal_part = abs(number) % 1.0
	whole_part = int(abs(number))
	decimal_str = str(int(round(decimal_part * 10**num_decimal_digits)))
	decimal_str = '.' + decimal_str + "0" * (num_decimal_digits - len(decimal_str))
	whole_part_str = ""
	while whole_part >= 1000:
		digits = whole_part % 1000
		digits_str = f" {digits :0>3}"
		whole_part_str = digits_str + whole_part_str
		whole_part //= 1000
	whole_part_str = str(whole_part) + whole_part_str
	return whole_part_str + decimal_str

def get_triangle(num_rows):
	border_char = "+"
	triangle_char = "A"
	largeur = 1 + 2 * (num_rows - 1)
	border_row = border_char * (largeur +2)
	result = border_row
	for i in range(num_rows):
		triangle_chars = triangle_char * (i*2 +1)
		result += "\n" + f"{border_char}{triangle_chars: ^{largeur}}{border_char}"
	result += "\n" + border_row
	return result


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-12345.678, 2))

	print(get_triangle(2))
	print(get_triangle(5))
