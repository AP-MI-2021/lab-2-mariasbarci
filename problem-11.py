# list when we put all leap years
all_leap_years =[];

def get_leap_years( year_start, year_end):
  print("Leap years:");
  for value in range(year_start,year_end+1):
      if check_leap_year(value):
          all_leap_years.append(value);

  return (all_leap_years)


# this function return true if year is leap / false if year is not leap
def check_leap_year (year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def test_get_leap_years():

    year_start = int(input("Introduceti anul de pornire: "))
    year_end = int(input("Introduceti anul de oprire: "))

    print(get_leap_years( year_start, year_end));

test_get_leap_years();
