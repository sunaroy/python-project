users = [
	{
		'id': 1,
		'username': 'bob',
		'password': 'asdf'
	}
]

user_name_mapping ={ 'bob': {
	'id': 1,
	'username': 'bob',
	'password': 'asdf'
	}
}

user_id_mapping ={ 1: {
	'id': 1,
	'username': 'bob',
	'password': 'asdf'
	
	}
}

def authenticate(username, password):
	user = user_name_mapping.get(username, None)
	if user && user['password'] == password:
		return user

def identity(payload):
	user_id = payload['identity']
	return user_id_mapping.get(user_id, None)
