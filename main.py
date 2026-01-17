# 1. 1-1000 შუალედიდან 7-ის ჯერადები
multiples_of_7 = [i for i in range(1, 1001) if i % 7 == 0]
print("7-ის ჯერადები:", multiples_of_7)

# 2. რიცხვები, რომელშიც ციფრი 3 შედის
numbers_with_3 = [i for i in range(1, 1001) if '3' in str(i)]
print("რიცხვები რომელშიც 3 არის:", numbers_with_3)

# 3. lorem ipsum ტექსტში სფეისების რაოდენობა
text = "lorem ipsum dolor sit amet consectetur adipiscing elit"
spaces_count = len([c for c in text if c == ' '])
print("სფეისების რაოდენობა:", spaces_count)
