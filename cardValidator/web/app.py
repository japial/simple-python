from bottle import route, run, template, request, view, response

from card_validator.validator import get_issuer


@route('/')
@view('index')
def index():
    return {
        'message': request.query.get('message', 'Validate Your Card')
    }


@route('/validate')
def validate():
    card_number = request.query.get('card', '').strip()
    if card_number:
        try:
            issuer = get_issuer(card_number)
        except ValueError:
            response.status = 500
            return {
                'card_number': card_number,
                'result': "This is not a valid credit card!"
            }

        response.status = 200
        return {
            'card_number': card_number,
            'issuer': issuer,
            'message': 'This is a Valid Card'
        }

    response.status = 202
    return {
        'message': "Please provide card number to validate credit card!"
    }


run(host='localhost', port=8080)
