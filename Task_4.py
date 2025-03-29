def magic_ticket():
    ticket = input("Введите номер билета: ")
    if len(ticket) %2 != 0:
        print("error")
        return
    half = len(ticket) // 2
    first_half = ticket[:half]
    second_half = ticket[half:]
    sum_first = sum(int(digit) for digit in first_half)
    sum_second = sum(int(digit) for digit in second_half)

    if sum_first == sum_second:
       print("Счатсливый билет")
    else:
       print("Билет не счастливый...")

magic_ticket()

