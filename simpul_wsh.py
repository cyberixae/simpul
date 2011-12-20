def web_socket_do_extra_handshake(request):
    pass

def web_socket_transfer_data(request):
    while True:
        msg = request.ws_stream.receive_message()
        request.ws_stream.send_message(msg)
