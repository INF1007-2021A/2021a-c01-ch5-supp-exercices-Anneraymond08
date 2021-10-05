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
	return ""

def get_triangle(num_rows):
	return ""


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-12345.678, 2))

	print(get_triangle(2))
	print(get_triangle(5))
