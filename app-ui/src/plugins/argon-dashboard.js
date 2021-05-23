import GlobalComponents from "./globalComponents";
import GlobalDirectives from "./globalDirectives";
import ViewsComponents from "./viewsComponents";

import "../assets/css/nucleo/css/nucleo.css";
import "../assets/sass/argon.scss";
import SidebarPlugin from "../components/SidebarPlugin";

import "bootstrap/dist/js/bootstrap.min.js";

export default {
  install(app) {
    app.use(SidebarPlugin);
    app.use(GlobalComponents);
    app.use(GlobalDirectives);
    app.use(ViewsComponents);
  },
};
