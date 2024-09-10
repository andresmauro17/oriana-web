<template>
  <Modal :show="showmodal" @update:show="upDateShowModal($event)">
    <template v-slot:header>
      <h6 class="modal-title">
        Certificados de calibracion:
      </h6>
    </template>
    <div>
      <table class="table mb-0 align-items-center">
        <thead>
          <td class="text-uppercase text-dark text-xxs font-weight-bolder opacity-7">Fecha de calibracion</td>
          <td class="text-uppercase text-dark text-xxs font-weight-bolder opacity-7">Documento</td>
        </thead>
        <tbody>
          <tr v-for="certificate in certificates" :key="certificate.id">
            <td>{{certificate.calibration_date}}</td>
            <td>
              <a :href="certificate.url" target="_blank">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-file-pdf" viewBox="0 0 16 16">
                  <path d="M4 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2zm0 1h8a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1"/>
                  <path d="M4.603 12.087a.8.8 0 0 1-.438-.42c-.195-.388-.13-.776.08-1.102.198-.307.526-.568.897-.787a7.7 7.7 0 0 1 1.482-.645 20 20 0 0 0 1.062-2.227 7.3 7.3 0 0 1-.43-1.295c-.086-.4-.119-.796-.046-1.136.075-.354.274-.672.65-.823.192-.077.4-.12.602-.077a.7.7 0 0 1 .477.365c.088.164.12.356.127.538.007.187-.012.395-.047.614-.084.51-.27 1.134-.52 1.794a11 11 0 0 0 .98 1.686 5.8 5.8 0 0 1 1.334.05c.364.065.734.195.96.465.12.144.193.32.2.518.007.192-.047.382-.138.563a1.04 1.04 0 0 1-.354.416.86.86 0 0 1-.51.138c-.331-.014-.654-.196-.933-.417a5.7 5.7 0 0 1-.911-.95 11.6 11.6 0 0 0-1.997.406 11.3 11.3 0 0 1-1.021 1.51c-.29.35-.608.655-.926.787a.8.8 0 0 1-.58.029m1.379-1.901q-.25.115-.459.238c-.328.194-.541.383-.647.547-.094.145-.096.25-.04.361q.016.032.026.044l.035-.012c.137-.056.355-.235.635-.572a8 8 0 0 0 .45-.606m1.64-1.33a13 13 0 0 1 1.01-.193 12 12 0 0 1-.51-.858 21 21 0 0 1-.5 1.05zm2.446.45q.226.244.435.41c.24.19.407.253.498.256a.1.1 0 0 0 .07-.015.3.3 0 0 0 .094-.125.44.44 0 0 0 .059-.2.1.1 0 0 0-.026-.063c-.052-.062-.2-.152-.518-.209a4 4 0 0 0-.612-.053zM8.078 5.8a7 7 0 0 0 .2-.828q.046-.282.038-.465a.6.6 0 0 0-.032-.198.5.5 0 0 0-.145.04c-.087.035-.158.106-.196.283-.04.192-.03.469.046.822q.036.167.09.346z"/>
                </svg>
                ver
              </a>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <template v-slot:footer>
    </template>
  </Modal>
</template>

<script setup>
  import { defineProps, defineEmits, onMounted, ref } from 'vue';
  import Modal from "@/components/Modals/Modal.vue";
  import SensorService from "@/services/sensorservice.js";
  const props = defineProps(["showmodal", "sensor"]);
  const emit = defineEmits(["upDateShowModal"]);
  const upDateShowModal = (event)=>{
    emit("upDateShowModal", event);
  }
  const certificates = ref([]);
  onMounted(()=>{
    SensorService.getSensorCertificates(props.sensor.id, props.sensor.legacy).then((res)=>{
      certificates.value = res.data.data;
    })
  });
</script>

<style lang="scss" scoped>

</style>