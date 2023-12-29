try{
    var cpasseye= document.getElementById('cpasseye');}
    catch{
    }
let passeye= document.getElementById('passeye');
let password= document.getElementById('password');
let confirmpassword= document.getElementById('confirmpassword');
passeye.addEventListener('click',function(){
    if(passeye.classList.contains('closed')){
        passeye.classList.remove('closed');
        passeye.classList.add('open');
        password.type="text";
    }
    else{
        passeye.classList.remove('open');
        passeye.classList.add('closed');
        password.type="password";
    }
})
try{

cpasseye.addEventListener('click',function(){
    if(cpasseye.classList.contains('closed')){
        cpasseye.classList.remove('closed');
        cpasseye.classList.add('open');
        confirmpassword.type="text";

    }
    else{
        cpasseye.classList.remove('open');
        cpasseye.classList.add('closed');
        confirmpassword.type="password";
    }
})}
catch{

}