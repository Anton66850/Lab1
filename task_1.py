numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

count_of_numbers = len(numbers)

numbers[4] = 0 #неизвестное

sum_of_numbers = sum(numbers) #sum

average_of_numbers = (sum_of_numbers/count_of_numbers)

numbers[4] = average_of_numbers

print("Измененный список:", numbers)