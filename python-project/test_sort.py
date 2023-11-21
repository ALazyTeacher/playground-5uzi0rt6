from sort import mySort


def success():
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test_sort_all():
    try:
        data1 = [5,6,2,3,7,11,1,15]
        count1 = mySort(data1)
        data1 = data1.sort()
        assert count1 == data1, "It worked!"
        success()

    except AssertionError as e:
        fail()
        send_msg("Oops! 🐞", e)
        send_msg("Git gud")


if __name__ == "__main__":
    test_sort_all()

