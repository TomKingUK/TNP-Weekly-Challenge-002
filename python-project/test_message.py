from message import decode_message

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))

def success():
    print("TECHIO> success true")

def fail():
    print("TECHIO> success false")
    

def test_decode_message():
    try:
        message = decode_message(['.--.', '-.--', '-', '....', '---', '-.', '/', '..', '...', '/', '..-.', '..-', '-.', '-.-.--'])
        assert message == 'python is fun!', "decode_message(['.--.', '-.--', '-', '....', '---', '-.', '/', '..', '...', '/', '..-.', '..-', '-.', '-.-.--']) /
        ... Expected 'python is fun!', got {}".format(message)
        success()
        send_msg('🌟 Decoded message:', message)

    except AssertionError as e:
        fail()
        send_msg('Result:', message)
        send_msg("Oops, something's not right! 🐞", e)
        send_msg("Hint 💡", "Did you rememeber to include spaces and punctuation? 🤔")


if __name__ == "__main__":
    test_decode_message()
