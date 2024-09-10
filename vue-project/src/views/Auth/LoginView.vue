<template>
  <main class="main-content mt-0">
    <div
      class="page-header align-items-start min-vh-50 pt-7 pb-9 bg-gradient-info"
    >
      <span class="mask bg-gradient opacity-6"></span>
      
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-lg-5 text-center mx-auto">
            <h1 class="text-white mb-2 mt-5">Bienvenido a Gthux!</h1>
            <p class="text-lead text-white">
              Sistema de monitoreo continuo para ambientes criticos.
            </p>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      <div class="row mt-lg-n10 mt-md-n11 mt-n10 justify-content-center">
        <div class="col-xl-4 col-lg-5 col-md-7 mx-auto">
          
          <div class="card mt-5">
            <div class="card-header pb-0 text-start">
              <h3 class="font-weight-bolder">Ingresar al sistema</h3>
              <p class="mb-0">Ingrese su correo electronico y contraseña</p>
            </div>
            <div class="card-body">
              <form role="form" class="text-start" @submit.prevent="onSubmit">
                <label>Correo electronico</label>
                <argon-input
                  id="email"
                  type="email"
                  placeholder="Email"
                  aria-label="Email"
                  @input="email = $event.target.value"
                  :error="showAlert"
                />
                <label>Contraseña</label>
                <argon-input
                  id="password"
                  type="password"
                  placeholder="Password"
                  aria-label="Password"
                  @input="password = $event.target.value"
                  :error="showAlert"
                />
                <!-- <argon-switch id="rememberMe" name="rememberMe">
                  Remember me
                </argon-switch> -->
                <div class="text-center">
                <ArgonBadge v-if="showAlert" color="danger" size="lg">{{alertText}}</ArgonBadge>
              </div>

                <div class="text-center"><button class="btn mb-0 btn-info btn-md w-100 null mt-4 mb-0">Ingresar</button></div>
              </form>
            </div>
            <div class="card-footer text-center pt-0 px-lg-2 px-1">
              <p class="text-sm mx-auto">
                Olvido su contraseña
                <a href="/accounts/password-reset/" class="text-info font-weight-bold"> Recordar</a>
              </p>
              <!-- <p class="mb-4 text-sm mx-auto">
                No tienes una cuenta?
                <a href="#" class="text-info font-weight-bold"> Crear</a>
              </p> -->
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  name: "SigninIllustration",
};

</script>

<script setup>
import { ref } from "vue";
import loginService from "@/services/auth/loginService.js";

import ArgonInput from "@/components/ArgonInput.vue";
import ArgonAlert from "@/components/ArgonAlert.vue";
import ArgonBadge from "@/components/ArgonBadge.vue";


const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
let nextParam = urlParams.get("next");
let alertText = ref("");
let showAlert = ref(false);

const email = ref(''); // Initialize email as an empty string
const password = ref(''); // Initialize password as an empty string


const onSubmit = ()=>{
  loginService
    .login(email.value, password.value)
    .then((res) => {
      if (res.status == 201) {
        window.location = nextParam ? nextParam : "/";
      }
    })
    .catch((error) => {
      if (error.response.status === 401) {
        alertText.value = error.response.data.error;
        showAlert.value = true;
      }
    });
}



</script>
