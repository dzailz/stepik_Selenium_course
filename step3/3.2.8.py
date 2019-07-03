def test_input_text(expected_result, actual_result):
    try:
        assert expected_result == actual_result
    except AssertionError:
        print("expected {}, got {}".format(expected_result, actual_result))
test_input_text(8, 11)