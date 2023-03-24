from django.test import TestCase
from datetime import datetime, timedelta

# Create your tests here.

def test_daw():
    now = datetime.now()
    print(now)

    for i in range(1, 4):
        delta = timedelta(days=i)
        date = now + delta
        date_str = date.strftime("%Y-%m-%d")
        print(date_str)


if __name__=="__main__":
    test_daw()
