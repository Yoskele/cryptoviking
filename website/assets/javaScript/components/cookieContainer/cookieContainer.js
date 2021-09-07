function setCookie(cname, cvalue, exdays) {
  var d = new Date();
  d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
  var expires = "expires="+d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}
function getCookie(cname) {
  var name = cname + "=";
  var ca = document.cookie.split(';');
  for(var i = 0; i < ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}
function checkCookie(){
	var value = getCookie("CookieCryptoViking");
 	if (value != "") {
 		//Not Empty
	} else {
	    value = 'CookieCryptoViking';
	    countValue = "";
	    if (value != "" && value != null) {
	    	setCookie("CookieCryptoViking", value, 1);
	    	setCookie("CookieCryptoViking", countValue, 1);
	    }
	}
	countValue = getCookie("CookieCryptoViking");
	if(countValue === 'allowed'){
		cookieLabel = document.getElementById('cookie_container');
  		cookieLabel.remove();
	}
}
const removeCookieContainer = () =>{
	console.log('inside.')
	countValue = getCookie("CookieCryptoViking");
	if(countValue == ""){
		cookieLabel = document.getElementById('cookie_container');
  		cookieLabel.remove();
  		setCookie("CookieCryptoViking", 'allowed', 1);
	}
}
checkCookie();