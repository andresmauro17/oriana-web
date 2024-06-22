import { api }  from "@/api/index.js";

const LoginService = {};

LoginService.login = function (email, password) {
  const params = {
    //token: this.model.token,
    email: email,
    password: password,
  };

  return api.post("users/login", params).then((res) => res);
};

export default LoginService;
