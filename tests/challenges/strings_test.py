from src.hacker_rank.challenges.strings import *


def test_swap_case():
    res = swap_case('Www.HackerRank.com')
    assert res == 'wWW.hACKERrANK.COM'

    res = swap_case('Pythonist 2')
    assert res == 'pYTHONIST 2'

    res = swap_case(
        "OzD0ro.7xwq A.MqhqT7'evgaVjpQ36OjSwfhuMaME'SDlyjPttjr6knZURciDARzAZ.3hQeIvX'IPe875zS3su6dajlMnbQOiH37U3YG0uzy6vW4v.onodBDDREYOf3CqeHfGcCeWV0dXrmTWAUsuw'jVwFO'5n.jvKLwXaDsam'y5sVQqB5O16bn1ug1XFeg3kmOGQFjxQ524k Z0yv76b4kkaC YuW9cw8Sfjf4 ynhe N88N3N2pfJF.I4ec5PgTp0Mp6VKawzg7GctsbPmU73aERqHxvWOMxDGZI9XWnJV6Aumecv0bHopAmfeD1K vTcxkzmdypHOGcdELdXjINde.ICPhEnpr9nJVL M7uY'L0BDX0i7CNCjIt9OiE2xjXt7JkK7vdUFlp6qn3Zua5vfP'nJcbviLrwj3.VlDDkd4VQ6zV1G2sGMmTVYkzaR9z5CDujAl'zYw8jw 9VOb5dP'zT'UTLMX2u8OG5YrGrvcENXF'QhBC8Ti'KRuhuO'SLlDKuRPHxFtnXW27YY1BMN9YkQww9kloEb43'loYiSFpIPiA0f1.3RYNUEN4QSbNQMpwQPZXsVKhc.uGvGJHiU80gcvOufOI2A0LdPcwGBWjTDl4TBZaycMfCmOceYqPj gqV7wTfSkY1F4INWqlKez.Vzbf84htDJg6D4MUt 2cGy8gMQolE 3gLR.rh3s5nbzN8hqKJr4c0L48zm2Hm7ObgsDu8dlrHnDaVKLQ65a7oTyz D6MLYD.q2AQXnQHKuTxKu5Fq7iNIRZKYyYeZo8n8JwHXtDbOaEnu'4'vmAsf2XR2q0ozLdw2FVsVpKEm4KzigoxY2GOpZq3OYW8cboQoD7STPJ8B'yEGZgk0vT mBABj0xeckqn6'Ouo99aTq'LKILUYjJ3DrduZj6Gq25kHUhfskez4LjZ21jduxXVXa8EmBNQeMf1A4R1v3fqGl W4Aw2UZ0t62TM fDGTqWgfvTb1RP7wyJ")
    assert res == "oZd0RO.7XWQ a.mQHQt7'EVGAvJPq36oJsWFHUmAme'sdLYJpTTJR6KNzurCIdarZaz.3HqEiVx'ipE875Zs3SU6DAJLmNBqoIh37u3yg0UZY6Vw4V.ONODbddreyoF3cQEhFgCcEwv0DxRMtwauSUW'JvWfo'5N.JVklWxAdSAM'Y5SvqQb5o16BN1UG1xfEG3KMogqfJXq524K z0YV76B4KKAc yUw9CW8sFJF4 YNHE n88n3n2PFjf.i4EC5pGtP0mP6vkAWZG7gCTSBpMu73AerQhXVwomXdgzi9xwNjv6aUMECV0BhOPaMFEd1k VtCXKZMDYPhogCDelDxJinDE.icpHeNPR9Njvl m7Uy'l0bdx0I7cncJiT9oIe2XJxT7jKk7VDufLP6QN3zUA5VFp'NjCBVIlRWJ3.vLddKD4vq6Zv1g2SgmMtvyKZAr9Z5cdUJaL'ZyW8JW 9voB5Dp'Zt'utlmx2U8og5yRgRVCenxf'qHbc8tI'krUHUo'slLdkUrphXfTNxw27yy1bmn9yKqWW9KLOeB43'LOyIsfPipIa0F1.3rynuen4qsBnqmPWqpzxSvkHC.UgVgjhIu80GCVoUFoi2a0lDpCWgbwJtdL4tbzAYCmFcMoCEyQpJ GQv7WtFsKy1f4inwQLkEZ.vZBF84HTdjG6d4muT 2CgY8GmqOLe 3Glr.RH3S5NBZn8HQkjR4C0l48ZM2hM7oBGSdU8DLRhNdAvklq65A7OtYZ d6mlyd.Q2aqxNqhkUtXkU5fQ7InirzkyYyEzO8N8jWhxTdBoAeNU'4'VMaSF2xr2Q0OZlDW2fvSvPkeM4kZIGOXy2goPzQ3oyw8CBOqOd7stpj8b'YegzGK0Vt MbabJ0XECKQN6'oUO99AtQ'lkiluyJj3dRDUzJ6gQ25KhuHFSKEZ4lJz21JDUXxvxA8eMbnqEmF1a4r1V3FQgL w4aW2uz0T62tm FdgtQwGFVtB1rp7WYj"


def test_string_validators(capsys):
    string_validators('qA2')

    captured = capsys.readouterr()
    spliced_captured_out = captured.out.split("\n")[:5]

    assert spliced_captured_out[0] == 'True'
    assert spliced_captured_out[1] == 'True'
    assert spliced_captured_out[2] == 'True'
    assert spliced_captured_out[3] == 'True'
    assert spliced_captured_out[4] == 'True'

    string_validators('#$%@^&*')

    captured = capsys.readouterr()
    spliced_captured_out = captured.out.split("\n")[:5]

    assert spliced_captured_out[0] == 'False'
    assert spliced_captured_out[1] == 'False'
    assert spliced_captured_out[2] == 'False'
    assert spliced_captured_out[3] == 'False'
    assert spliced_captured_out[4] == 'False'


def test_string_formatting(capsys):
    string_formatting(2)

    captured = capsys.readouterr()
    spliced_captured_out = captured.out.split("\n")[:2]

    assert spliced_captured_out[0] == '1 1 1 1'


def test_wrap(capsys):
    wrap('ABCDEFGHIJKLIMNOQRSTUVWXYZ', 4)

    captured = capsys.readouterr()
    spliced_captured_out = captured.out.split("\n")[:7]

    assert spliced_captured_out[0] == 'ABCD'
    assert spliced_captured_out[1] == 'EFGH'
    assert spliced_captured_out[2] == 'IJKL'
    assert spliced_captured_out[3] == 'IMNO'
    assert spliced_captured_out[4] == 'QRST'
    assert spliced_captured_out[5] == 'UVWX'
    assert spliced_captured_out[6] == 'YZ'
