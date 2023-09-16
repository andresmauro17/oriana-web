import { api } from "@/api/index.js";
// import { FakeEndPoint } from "@/api/index.js";

const UserService = {};

UserService.getCurrentUser = function () {
  return api.get("/users/current").then((res) => res);
};



export default UserService;
