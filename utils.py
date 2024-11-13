from kavenegar import *

def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('65676B6D4F4C485652676F426E7577386A734D4D6A427835544943706168715841785A2F3036397A7733493D')
        params = {
            'sender': '',
            'receptor': phone_number,
            'message': f'{code} کد تایید شما '
        }
        responses = api.sms_send(params)
        print(responses)
    except APIException as e:
        print(e)
    except Exception as e:
        print(e)