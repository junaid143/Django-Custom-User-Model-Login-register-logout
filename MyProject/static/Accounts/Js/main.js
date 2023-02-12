
    function ShowPass(){

        var pass1 = document.getElementById('password');

        if (pass1.type == 'password'){
            pass1.style.width = '100%';
            pass1.style.height = '40px';
            pass1.style.borderRadius = '5px'
            pass1.type = 'text';
        }

        else{
            pass1.type = 'password';
        }
    }
