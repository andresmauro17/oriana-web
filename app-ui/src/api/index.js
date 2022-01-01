import axios from "axios";
import cookiesService from "@/services/cookiesService.js";

var urlIn = window.location.href;
var arr = urlIn.split("/");
var currentUrl = arr[0] + "//" + arr[2] + "/api";
var csrftoken = cookiesService.getCookieByName("csrftoken"); // django csrftoken

let instance = axios.create({
  baseURL: currentUrl,
  headers: { "X-CSRFToken": csrftoken },
  //send a pseudo params for the browser doesnt take past cache when back
  params: {
    pseudoParam: new Date().getTime(),
  },
});

export default instance;
