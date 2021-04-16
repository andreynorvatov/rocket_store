/*----input validation----*/

let	reg__username = /^[a-zA-Zа-яёА-ЯЁ]+$/,
		reg__userphone = /^((8|\+7|7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$/;
		reg__useremail = /^.+@.+\..+$/;

let inp_username = document.querySelector('#username');
let inp_userphone = document.querySelector('#userphone');
let inp_useremail = document.querySelector('#useremail');
let username__warning = document.querySelector('.username__warning');
let userphone__warning = document.querySelector('.userphone__warning');
let useremail__warning = document.querySelector('.useremail__warning');


document.querySelector('.order__btn').onclick = function(e){
		e.preventDefault();

		if(!validate(reg__username, inp_username.value)) {
			notValid(inp_username, username__warning, 'Не верный формат имени');
		}else{
			notValid(inp_username, username__warning, '');
		};
		
		if(!validate(reg__userphone, inp_userphone.value)) {
			notValid(inp_userphone, userphone__warning, 'Не верный формат телефона');
		}else{
			notValid(inp_userphone, userphone__warning, '');
		}

		if(!validate(reg__useremail, inp_useremail.value)) {
			notValid(inp_useremail, useremail__warning, 'Не верный формат Email');
		} else{
			notValid(inp_useremail, useremail__warning, '');
		}
};


function validate(regex, inp){
	return regex.test(inp);
};

function notValid(inp, el, mess){
	inp.classList.add('is-invalid');
	el.innerHTML = mess;
};

function valid(inp, el, mess){
	inp.classList.remove('is-invalid');
	inp.classList.add('is-valid');
	el.innerHTML = mess;
};


/*----order__btn disabled----*/
/*
let orderForm = document.querySelector('#order__form');

orderForm.addEventListener('input', ()=>{

	if (username.value.length > 1 &&
		userphone.value.length > 9 &&
		useremail.value.length > 4) {
		order__btn.removeAttribute('disabled');


	} else {
		order__btn.setAttribute('disabled', 'disabled');
	}
					
});
*/