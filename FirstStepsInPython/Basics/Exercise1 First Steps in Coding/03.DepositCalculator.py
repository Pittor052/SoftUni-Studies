deposit = float ( input () )
months = int ( input () )
yearly_interest = float ( input () )
interest = deposit * yearly_interest / 100
monthly_interest = interest / 12
total_sum = deposit +(months * monthly_interest)
print(total_sum)