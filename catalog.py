def catalog():
	item = {
		'name' : 'laptop',
		'harga' : '2000',
		'qty'	: '10',
		'catagories' :{
			'name' : 'komputer',
			'komputer' : {
				'sub_categories' : 'Acer'
			}
		}
	}

	print(item['catagories']['name'], item['name'], item['catagories']['komputer']['sub_categories'])

catalog()