def max_new_people(seats):
    n = len(seats)
    count = 0

    for i in range(n):
        # only check empty seats
        if seats[i] == 0:
            # check left side (two seats back)
            left_ok = (i - 1 < 0 or seats[i - 1] == 0) and (i - 2 < 0 or seats[i - 2] == 0)
            # check right side (two seats forward)
            right_ok = (i + 1 >= n or seats[i + 1] == 0) and (i + 2 >= n or seats[i + 2] == 0)

            if left_ok and right_ok:
                seats[i] = 1   # place new person
                count += 1
    return count

# Example
seats = [0,0,0,1,0,0,1,0,0,0]
print(max_new_people(seats))  # Output: 2
