<template>
  <base-nav
    container-classes="container-fluid"
    class="navbar-top border-bottom navbar-expand"
    :class="{ 'bg-info navbar-dark': type === 'default' }"
  >
    <!-- Navbar links -->
    <ul class="navbar-nav align-items-center ml-md-auto">
      <base-dropdown
        class="nav-item"
        tag="li"
        title-classes="nav-link"
        title-tag="a"
        icon="ni ni-bell-55"
        menu-classes="dropdown-menu-xl dropdown-menu-right py-0 overflow-hidden"
      >
        <!-- Dropdown header -->
        <div class="px-3 py-3">
          <h6 class="text-sm text-muted m-0">
            You have <strong class="text-primary">13</strong> notifications.
          </h6>
        </div>
        <!-- List group -->
        <div class="list-group list-group-flush">
          <a href="#!" class="list-group-item list-group-item-action">
            <div class="row align-items-center">
              <div class="col-auto">
                <!-- Avatar -->
                <img
                  alt="Image placeholder"
                  :src="appSettings.STATIC_URL + 'img/theme/team-1.jpg'"
                  class="avatar rounded-circle"
                />
              </div>
              <div class="col ml--2">
                <div class="d-flex justify-content-between align-items-center">
                  <div>
                    <h4 class="mb-0 text-sm">John Snow</h4>
                  </div>
                  <div class="text-right text-muted">
                    <small>2 hrs ago</small>
                  </div>
                </div>
                <p class="text-sm mb-0">
                  Let's meet at Starbucks at 11:30. Wdyt?
                </p>
              </div>
            </div>
          </a>
          <a href="#!" class="list-group-item list-group-item-action">
            <div class="row align-items-center">
              <div class="col-auto">
                <!-- Avatar -->
                <img
                  alt="Image placeholder"
                  :src="appSettings.STATIC_URL + 'img/theme/team-2.jpg'"
                  class="avatar rounded-circle"
                />
              </div>
              <div class="col ml--2">
                <div class="d-flex justify-content-between align-items-center">
                  <div>
                    <h4 class="mb-0 text-sm">John Snow</h4>
                  </div>
                  <div class="text-right text-muted">
                    <small>3 hrs ago</small>
                  </div>
                </div>
                <p class="text-sm mb-0">
                  A new issue has been reported for Argon.
                </p>
              </div>
            </div>
          </a>
          <a href="#!" class="list-group-item list-group-item-action">
            <div class="row align-items-center">
              <div class="col-auto">
                <!-- Avatar -->
                <img
                  alt="Image placeholder"
                  :src="appSettings.STATIC_URL + 'img/theme/team-3.jpg'"
                  class="avatar rounded-circle"
                />
              </div>
              <div class="col ml--2">
                <div class="d-flex justify-content-between align-items-center">
                  <div>
                    <h4 class="mb-0 text-sm">John Snow</h4>
                  </div>
                  <div class="text-right text-muted">
                    <small>5 hrs ago</small>
                  </div>
                </div>
                <p class="text-sm mb-0">Your posts have been liked a lot.</p>
              </div>
            </div>
          </a>
          <a href="#!" class="list-group-item list-group-item-action">
            <div class="row align-items-center">
              <div class="col-auto">
                <!-- Avatar -->
                <img
                  alt="Image placeholder"
                  :src="appSettings.STATIC_URL + 'img/theme/team-4.jpg'"
                  class="avatar rounded-circle"
                />
              </div>
              <div class="col ml--2">
                <div class="d-flex justify-content-between align-items-center">
                  <div>
                    <h4 class="mb-0 text-sm">John Snow</h4>
                  </div>
                  <div class="text-right text-muted">
                    <small>2 hrs ago</small>
                  </div>
                </div>
                <p class="text-sm mb-0">
                  Let's meet at Starbucks at 11:30. Wdyt?
                </p>
              </div>
            </div>
          </a>
          <a href="#!" class="list-group-item list-group-item-action">
            <div class="row align-items-center">
              <div class="col-auto">
                <!-- Avatar -->
                <img
                  alt="Image placeholder"
                  :src="appSettings.STATIC_URL + 'img/theme/team-5.jpg'"
                  class="avatar rounded-circle"
                />
              </div>
              <div class="col ml--2">
                <div class="d-flex justify-content-between align-items-center">
                  <div>
                    <h4 class="mb-0 text-sm">John Snow</h4>
                  </div>
                  <div class="text-right text-muted">
                    <small>3 hrs ago</small>
                  </div>
                </div>
                <p class="text-sm mb-0">
                  A new issue has been reported for Argon.
                </p>
              </div>
            </div>
          </a>
        </div>
        <!-- View all -->
        <a
          href="#!"
          class="dropdown-item text-center text-primary font-weight-bold py-3"
          >View all</a
        >
      </base-dropdown>
    </ul>
    <ul class="navbar-nav align-items-center ml-auto ml-md-0">
      <base-dropdown
        menu-on-right
        class="nav-item"
        tag="li"
        title-tag="a"
        title-classes="nav-link pr-0"
      >
        <template v-slot:title-container>
          <a href="#" class="nav-link pr-0" @click.prevent>
            <div class="media align-items-center">
              <span class="avatar avatar-sm rounded-circle">
                <img
                  alt="Image placeholder"
                  :src="appSettings.STATIC_URL + 'img/theme/team-4.jpg'"
                />
              </span>
              <div class="media-body ml-2 d-none d-lg-block">
                <span class="mb-0 text-sm font-weight-bold">John Snow</span>
              </div>
            </div>
          </a>
        </template>

        <div class="dropdown-header noti-title">
          <h6 class="text-overflow m-0">Bienvenido!</h6>
        </div>
        <a href="#!" class="dropdown-item">
          <i class="ni ni-single-02"></i>
          <span>Mi perfil</span>
        </a>
        <a href="#!" class="dropdown-item">
          <i class="ni ni-settings-gear-65"></i>
          <span>Configuracion</span>
        </a>
        <a href="#!" class="dropdown-item">
          <i class="ni ni-support-16"></i>
          <span>Soporte</span>
        </a>
        <div class="dropdown-divider"></div>
        <a href="/logout" class="dropdown-item">
          <i class="ni ni-user-run"></i>
          <span>Salir</span>
        </a>
      </base-dropdown>
    </ul>
  </base-nav>
</template>
<script>
import { mapState } from "vuex";
import BaseNav from "@/components/Navbar/BaseNav";

export default {
  components: {
    BaseNav,
  },
  props: {
    type: {
      type: String,
      default: "default", // default|light
      description:
        "Look of the dashboard navbar. Default (Green) or light (gray)",
    },
  },
  computed: {
    ...mapState(["appSettings"]),
    routeName() {
      const { name } = this.$route;
      return this.capitalizeFirstLetter(name);
    },
  },
  data() {
    return {
      activeNotifications: false,
      showMenu: false,
      searchModalVisible: false,
      searchQuery: "",
    };
  },
  methods: {
    capitalizeFirstLetter(string) {
      return string.charAt(0).toUpperCase() + string.slice(1);
    },
    toggleNotificationDropDown() {
      this.activeNotifications = !this.activeNotifications;
    },
    closeDropDown() {
      this.activeNotifications = false;
    },
    toggleSidebar() {
      this.$sidebar.displaySidebar(!this.$sidebar.showSidebar);
    },
    hideSidebar() {
      this.$sidebar.displaySidebar(false);
    },
  },
};
</script>
