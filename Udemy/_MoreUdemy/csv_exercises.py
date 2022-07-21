
import csv


def add_user(first_name, last_name):

    with open("users.csv", "a") as file_01_csv:
        writer = csv.writer(file_01_csv)
        writer.writerow([first_name, last_name])


def print_users():
    with open("users.csv", "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        users_l = list(csv_reader)
        for i in users_l:
            print("{} {}".format(i['First Name'], i['Last Name']))


def find_user(first_nm, last_nm):
    with open("users.csv", "r") as csv_file:
        csv_read = csv.DictReader(csv_file)
        csv_d = list(csv_read)
        for user_d in csv_d:
            if user_d["First Name"] == first_nm and user_d["Last Name"] == last_nm:
                return csv_d.index(user_d) + 1
        return "{} {} not found".format(first_nm, last_nm)


def find_user_colts_sol(first_name, last_name):
    with open("users.csv") as csv_file:
        csv_reader = csv.reader(csv_file)
        for (index, row) in enumerate(csv_reader):
            first_name_match = first_name == row[0]
            last_name_match = last_name == row[1]
            if first_name_match and last_name_match:
                return index
        return "{} {} not found.".format(first_name, last_name)

# For this exercise, you'll be working with a file called users.csv Each row of data
# consists of two columns, a user's first name, and a user's last name. Implement
# the following function: update_users() Takes in an old first name, an old last
# name, a new first name, and a new last name. Updates the users.csv file so that
# any user whose first and last names match the old first and last names are
# updated to the new first and last names. The function should return a count of
# how many users were updated.


def update_users(old_first, old_last, first_name, last_name):

    users_updated = 0


    with open("users.csv") as csv_file:
        read = csv.DictReader(csv_file)
        read_list = list(read)

        for name in read_list:
            if name["First Name"] == old_first and name["Last Name"] == old_last:
                name["First Name"] = first_name
                name["Last Name"] = last_name
                users_updated += 1

    with open("users.csv", "w") as new_file:
        headers = ["First Name", "Last Name"]
        write = csv.DictWriter(new_file, fieldnames=headers)
        write.writeheader()
        write.writerows(read_list)

    return f"Users updated: {users_updated}."


def update_users_colts_sol(old_first, old_last, new_first, new_last):

    with open("users.csv") as csv_file:
        csv_reader = csv.reader(csv_file)
        rows = list(csv_reader)

    count = 0

    with open("users.csv", "w") as csv_file:
        csv_writer = csv.writer(csv_file)

        for row in rows:
            if row[0] == old_first and row[1] == old_last:
                csv_writer.writerow([new_first, new_last])
                count += 1
            else:
                csv_writer.writerow(row)

    return "Users updated: {}.".format(count)


def delete_users(first_name, last_name):

    with open("users.csv") as csv_file:
        csv_reader = csv.reader(csv_file)
        rows = list(csv_reader)

    count = 0

    with open("users.csv", "w") as csv_file:
        csv_writer = csv.writer(csv_file)

        for row in rows:
            if row[0] == first_name and row[1] == last_name:
                count += 1
            else:
                csv_writer.writerow(row)

    return "Users deleted: {}.".format(count)


print(delete_users("Josh", "Aguilar"))