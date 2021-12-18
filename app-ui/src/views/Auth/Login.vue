<template>
  <div>
    <!-- Header -->
    <div class="header bg-gradient-info py-7 py-lg-8 pt-lg-9">
      <div class="container">
        <div class="header-body text-center mb-4">
          <div class="row justify-content-center">
            <div class="col-xl-5 col-lg-6 col-md-8 px-5">
              <h1 class="text-white">Bienvenido a Gthux!</h1>
              <p class="text-lead text-white">
                Sistema de monitoreo continuo para ambientes criticos.
              </p>
            </div>
          </div>
        </div>
      </div>
      <div class="separator separator-bottom separator-skew zindex-100">
        <svg
          x="0"
          y="0"
          viewBox="0 0 2560 100"
          preserveAspectRatio="none"
          version="1.1"
          xmlns="http://www.w3.org/2000/svg"
        >
          <polygon
            class="fill-body-bg"
            points="2560 0 2560 100 0 100"
          ></polygon>
        </svg>
      </div>
    </div>
    <!-- Page content -->
    <div class="container mt--8 pb-5">
      <div class="row justify-content-center">
        <div class="col-lg-5 col-md-7">
          <div class="card bg-secondary border-0 mb-0">
            <div class="card-header bg-transparent pb-2">
              <div class="text-muted text-center mt-2 mb-3">
                <small>ingresar al sistema</small>
              </div>
            </div>
            <div class="card-body px-lg-5 py-lg-5">
              <Form @submit="onSubmit" :validation-schema="schema">
                <base-input
                  alternative
                  name="email"
                  addon-left-icon="ni ni-email-83"
                  placeholder="Correo electronico"
                >
                </base-input>

                <base-input
                  alternative
                  name="password"
                  addon-left-icon="ni ni-lock-circle-open"
                  type="password"
                  placeholder="Contraseña"
                >
                </base-input>

                <base-checkbox v-model="model.rememberMe">
                  recordar
                </base-checkbox>

                <div class="text-center">
                  <base-button type="primary" native-type="submit" class="my-4">
                    Ingresar
                  </base-button>
                </div>
              </Form>
            </div>
          </div>
          <div class="row mt-3">
            <div class="col-6">
              <a to="/dashboard">
                <small>olvido su contraseña?</small>
              </a>
            </div>
            <div class="col-6 text-right">
              <a href="/register">
                <small>crear nueva cuenta</small>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { Form } from "vee-validate";
import * as Yup from "yup";

export default {
  components: {
    Form,
  },
  data() {
    return {
      model: {
        email: "",
        password: "",
        rememberMe: false,
      },
    };
  },
  setup() {
    function onSubmit(values) {
      alert(JSON.stringify(values, null, 2));
    }

    const schema = Yup.object().shape({
      fullName: Yup.string().required().label("The Full Name"),
      email: Yup.string().email().required().label("The Email"),
      password: Yup.string().min(5).required().label("The Password"),
    });

    return {
      onSubmit,
      schema,
    };
  },
};
</script>
