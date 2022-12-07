# Calculating moving averages 

closing_price_sum = 0 

with open('data/spy.csv') as f:
    content = f.readlines()[-200:]
    
    for line in content:
        print(line)

        # splitting to get closing price 
        tokens = line.split(',')
        close = tokens[4]

        closing_price_sum += float(close)

print(closing_price_sum / 200)