# TODO Найдите количество книг, которое можно разместить на дискете

v_disc = 1.44
count_page = 100
count_str_in_page = 50
count_symbol_in_str = 25
weight_symbol = 4

v_disc_b = v_disc * 1024 * 1024
book = count_page * count_str_in_page * count_symbol_in_str
v_book = book * weight_symbol

count_book = v_disc_b // v_book

print("Количество книг, помещающихся на дискету:", int(count_book))
