const CookiesService = {};

// this service method return a cookie https://www.w3schools.com/js/js_cookies.asp
CookiesService.getCookieByName = function (cname) {
  var name = cname + "=";
  var decodedCookie = decodeURIComponent(document.cookie);
  var ca = decodedCookie ? decodedCookie.split(";"):[];
  for (var i = 0; i < ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == "") {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
};

export default CookiesService;
