import schwab_to_google_fin

def test_open_csv():
    assert schwab_to_google_fin.open_csv() == \
        ["Date","Action","Symbol","Description","Quantity","Price","Fees & Comm","Amount"]

