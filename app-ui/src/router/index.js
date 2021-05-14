import { createRouter, createWebHashHistory } from "vue-router";

import DashboardLayout from "@/views/Layout/DashboardLayout";
import AuthLayout from "@/views/Pages/AuthLayout";

// Dashboard pages
import Dashboard from "../views/Dashboard/Dashboard.vue";
import Alternative from "../views/Dashboard/AlternativeDashboard.vue";
import Widgets from "../views/Widgets.vue";
import Charts from "../views/Charts.vue";
import Calendar from "../views/Calendar/Calendar.vue";

// Pages
import Pricing from "../views/Pages/Pricing.vue";
import Login from "../views/Pages/Login.vue";
import Register from "../views/Pages/Register.vue";
import Lock from "../views/Pages/Lock.vue";
import Profile from "../views/Pages/UserProfile.vue";
import Timeline from "../views/Pages/TimeLinePage.vue";

// Components pages
import Buttons from "../views/Components/Buttons.vue";
import Cards from "../views/Components/Cards.vue";
import Grid from "../views/Components/GridSystem.vue";
import Notifications from "../views/Components/Notifications.vue";
import Icons from "../views/Components/Icons.vue";
import Typography from "../views/Components/Typography.vue";

// Tables pages
import RegularTables from "../views/Tables/RegularTables.vue";
import SortableTables from "../views/Tables/SortableTables.vue";
import PaginatedTables from "../views/Tables/PaginatedTables.vue";

// Maps pages
import GoogleMaps from "../views/Maps/GoogleMaps.vue";
import VectorMaps from "../views/Maps/VectorMaps.vue";

// Forms pages
import FormElements from "../views/Forms/FormElements.vue";
import FormComponents from "../views/Forms/FormComponents.vue";
import FormValidation from "../views/Forms/FormValidation.vue";

let componentsMenu = {
  path: "/components",
  component: DashboardLayout,
  redirect: "/components/buttons",
  name: "Components",
  children: [
    {
      path: "buttons",
      name: "Buttons",
      components: { default: Buttons },
    },
    {
      path: "cards",
      name: "Cards",
      components: { default: Cards },
    },
    {
      path: "grid-system",
      name: "Grid",
      components: { default: Grid },
    },
    {
      path: "notifications",
      name: "Notifications",
      components: { default: Notifications },
    },
    {
      path: "icons",
      name: "Icons",
      components: { default: Icons },
    },
    {
      path: "typography",
      name: "Typography",
      components: { default: Typography },
    },
  ],
};

let tablesMenu = {
  path: "/tables",
  component: DashboardLayout,
  redirect: "/tables/regular",
  name: "Tables menu",
  children: [
    {
      path: "regular",
      name: "Tables",
      components: { default: RegularTables },
    },
    {
      path: "sortable",
      name: "Sortable",
      components: { default: SortableTables },
    },
    {
      path: "paginated",
      name: "Paginated",
      components: { default: PaginatedTables },
    },
  ],
};

let mapsMenu = {
  path: "/maps",
  component: DashboardLayout,
  redirect: "/maps/google",
  name: "Maps",
  children: [
    {
      path: "google",
      name: "Google Maps",
      components: { default: GoogleMaps },
    },
    {
      path: "vector",
      name: "Vector Map",
      components: { default: VectorMaps },
    },
  ],
};

let formsMenu = {
  path: "/forms",
  component: DashboardLayout,
  redirect: "/forms/elements",
  name: "Forms",
  children: [
    {
      path: "elements",
      name: "Forms elements",
      components: { default: FormElements },
    },
    {
      path: "components",
      name: "Forms Components",
      components: { default: FormComponents },
    },
    {
      path: "validation",
      name: "Forms Validation",
      components: { default: FormValidation },
    },
  ],
};

const routes = [
  {
    path: "/",
    redirect: "/dashboard",
    component: DashboardLayout,
    name: "Dashboards",
    children: [
      {
        path: "/dashboard",
        name: "Dashboard",
        components: { default: Dashboard },
      },
      {
        path: "/alternative",
        name: "Alternative",
        components: { default: Alternative },
        meta: {
          navbarType: "light",
        },
      },
      {
        path: "/widgets",
        name: "Widgets",
        components: { default: Widgets },
      },
      {
        path: "/charts",
        name: "Charts",
        components: { default: Charts },
      },
      {
        path: "/calendar",
        name: "Calendar",
        components: { default: Calendar },
      },
      {
        path: "/pages/user",
        name: "Profile",
        components: { default: Profile },
      },
      {
        path: "/pages/timeline",
        name: "Timeline",
        components: { default: Timeline },
      },
    ],
  },
  {
    path: "/",
    redirect: "/",
    component: AuthLayout,
    children: [
      {
        path: "/pricing",
        name: "Pricing",
        components: { default: Pricing },
      },
      {
        path: "/login",
        name: "Login",
        components: { default: Login },
      },
      {
        path: "/register",
        name: "Register",
        components: { default: Register },
      },
      {
        path: "/lock",
        name: "Lock",
        components: { default: Lock },
      },
    ],
  },
  componentsMenu,
  tablesMenu,
  mapsMenu,
  formsMenu,
];

const router = createRouter({
  history: createWebHashHistory(),
  linkActiveClass: "active",
  routes,
});

export default router;
